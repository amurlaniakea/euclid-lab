# SPDX-FileCopyrightText: 2026 Pedro Sordo Martínez <amurlaniakea@gmail.com>
#
# SPDX-License-Identifier: AGPL-3.0-or-later
#
# Copyright (C) 2026 Pedro Sordo Martínez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with this program. If not, see
# <https://www.gnu.org/licenses/>.

"""Educational FITS image and catalogue utilities for Euclid Lab v0.4.0.

Source detection and aperture photometry are exploratory estimates, not a
calibrated scientific pipeline. Preserve masks, units, WCS, calibration and
uncertainty provenance for research-grade measurements.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np


def _finite_2d(data: Any) -> tuple[np.ndarray, np.ndarray]:
    array = np.asarray(data, dtype=float)
    if array.ndim != 2:
        raise ValueError(f"Expected a 2-D image array, got {array.ndim}-D data.")
    finite = np.isfinite(array)
    if not finite.any():
        raise ValueError("Image contains no finite pixels.")
    return array, finite


def image_summary(data: Any) -> dict[str, float | int]:
    array, finite = _finite_2d(data)
    values = array[finite]
    p1, p5, p25, p75, p95, p99 = np.percentile(values, [1, 5, 25, 75, 95, 99])
    return {
        "n_pixels": int(values.size), "n_invalid": int(array.size - values.size),
        "minimum": float(np.min(values)), "maximum": float(np.max(values)),
        "mean": float(np.mean(values)), "median": float(np.median(values)),
        "std": float(np.std(values)), "p01": float(p1), "p05": float(p5),
        "p25": float(p25), "p75": float(p75), "p95": float(p95), "p99": float(p99),
    }


def display_limits(data: Any, lower_percentile: float = 1.0,
                   upper_percentile: float = 99.0) -> tuple[float, float]:
    if not (0 <= lower_percentile < upper_percentile <= 100):
        raise ValueError("Percentiles must satisfy 0 <= lower < upper <= 100.")
    array, finite = _finite_2d(data)
    low, high = np.percentile(array[finite], [lower_percentile, upper_percentile])
    if not np.isfinite(low) or not np.isfinite(high):
        raise ValueError("Could not calculate finite display limits.")
    if high <= low:
        delta = max(abs(float(low)) * 1e-6, 1e-12)
        return float(low - delta), float(high + delta)
    return float(low), float(high)


def stretch_image(data: Any, stretch: str = "linear", vmin: float | None = None,
                  vmax: float | None = None, asinh_a: float = 0.1) -> np.ndarray:
    array, finite = _finite_2d(data)
    if vmin is None or vmax is None:
        auto_low, auto_high = display_limits(array)
        vmin = auto_low if vmin is None else float(vmin)
        vmax = auto_high if vmax is None else float(vmax)
    if not np.isfinite(vmin) or not np.isfinite(vmax) or vmax <= vmin:
        raise ValueError("Display limits must be finite and vmax must exceed vmin.")
    clipped = np.clip((array - vmin) / (vmax - vmin), 0.0, 1.0)
    result = np.full(array.shape, np.nan, dtype=float)
    if stretch == "linear":
        transformed = clipped
    elif stretch == "log":
        transformed = np.log1p(1000.0 * clipped) / np.log1p(1000.0)
    elif stretch == "asinh":
        if not np.isfinite(asinh_a) or asinh_a <= 0:
            raise ValueError("asinh_a must be a finite positive number.")
        transformed = np.arcsinh(clipped / asinh_a) / np.arcsinh(1.0 / asinh_a)
    else:
        raise ValueError("stretch must be 'linear', 'log' or 'asinh'.")
    result[finite] = transformed[finite]
    return result


def load_fits_image(path: str | Path, hdu: int = 0):
    from astropy.io import fits
    with fits.open(path, memmap=False) as hdul:
        if hdu < 0 or hdu >= len(hdul):
            raise IndexError(f"HDU index {hdu} is out of range (0..{len(hdul) - 1}).")
        if hdul[hdu].data is None:
            raise ValueError(f"FITS HDU {hdu} does not contain image data.")
        data = np.array(hdul[hdu].data, copy=True)
        header = hdul[hdu].header.copy()
    if data.ndim != 2:
        raise ValueError(f"Expected a 2-D FITS image, got shape {data.shape}.")
    return data, header


def detect_sources(data: Any, threshold_sigma: float = 5.0,
                   min_pixels: int = 3) -> list[dict[str, float | int]]:
    """Detect connected pixels above median + threshold_sigma * robust_sigma.

    Uses scipy.ndimage for 8-connected components. Coordinates are zero-based
    pixel-centre positions (x=column, y=row); flux is a simple sum above global
    median background. It is not deblended and is sensitive to image artifacts.
    """
    from scipy import ndimage
    array, finite = _finite_2d(data)
    if threshold_sigma <= 0 or min_pixels < 1:
        raise ValueError("threshold_sigma must be > 0 and min_pixels must be >= 1.")
    background = float(np.median(array[finite]))
    mad = float(np.median(np.abs(array[finite] - background)))
    sigma = 1.4826 * mad
    if sigma <= 0:
        sigma = float(np.std(array[finite]))
    if not np.isfinite(sigma) or sigma <= 0:
        raise ValueError("Image has no measurable background variation.")
    mask = finite & (array > background + threshold_sigma * sigma)
    labels, count = ndimage.label(mask, structure=np.ones((3, 3), dtype=int))
    objects = ndimage.find_objects(labels)
    sources = []
    for label_id, slices in enumerate(objects, start=1):
        if slices is None:
            continue
        yy, xx = np.nonzero(labels[slices] == label_id)
        if len(xx) < min_pixels:
            continue
        yy = yy + slices[0].start
        xx = xx + slices[1].start
        weights = np.clip(array[yy, xx] - background, 0, None)
        flux = float(weights.sum())
        if flux <= 0:
            continue
        sources.append({
            "source_id": len(sources) + 1,
            "xcentroid": float(np.sum(xx * weights) / flux),
            "ycentroid": float(np.sum(yy * weights) / flux),
            "npix": int(len(xx)),
            "peak": float(np.max(array[yy, xx])),
            "threshold_flux": flux,
        })
    return sources


def aperture_photometry(data: Any, x: float, y: float, radius: float = 4.0,
                        annulus_inner: float | None = None,
                        annulus_outer: float | None = None) -> dict[str, float | int]:
    """Circular-aperture flux with median local annulus background subtraction."""
    array, finite = _finite_2d(data)
    if radius <= 0:
        raise ValueError("radius must be positive.")
    rin = float(annulus_inner if annulus_inner is not None else radius * 1.5)
    rout = float(annulus_outer if annulus_outer is not None else radius * 2.5)
    if rin <= radius or rout <= rin:
        raise ValueError("Require radius < annulus_inner < annulus_outer.")
    yy, xx = np.indices(array.shape)
    r2 = (xx - float(x)) ** 2 + (yy - float(y)) ** 2
    aperture = (r2 <= radius ** 2) & finite
    annulus = (r2 >= rin ** 2) & (r2 <= rout ** 2) & finite
    if not aperture.any() or not annulus.any():
        raise ValueError("Aperture or background annulus contains no valid pixels.")
    local_background = float(np.median(array[annulus]))
    raw_flux = float(np.sum(array[aperture]))
    net_flux = float(np.sum(array[aperture] - local_background))
    return {
        "x": float(x), "y": float(y), "aperture_radius": float(radius),
        "aperture_pixels": int(aperture.sum()), "annulus_pixels": int(annulus.sum()),
        "local_background": local_background, "raw_flux": raw_flux,
        "net_flux": net_flux,
        "instrumental_magnitude": float(-2.5 * np.log10(net_flux)) if net_flux > 0 else float("nan"),
    }


def read_fits_catalogues(path: str | Path) -> list[dict[str, Any]]:
    """Read binary/table HDUs from a FITS file as serializable row dictionaries."""
    from astropy.io import fits
    from astropy.table import Table
    catalogues = []
    with fits.open(path, memmap=False) as hdul:
        for index, hdu in enumerate(hdul):
            if getattr(hdu, "columns", None) is None or hdu.data is None:
                continue
            table = Table(hdu.data)
            rows = []
            for row in table:
                record = {}
                for name in table.colnames:
                    value = row[name]
                    if np.ma.is_masked(value):
                        record[name] = None
                    elif isinstance(value, np.ndarray):
                        record[name] = value.tolist()
                    elif isinstance(value, np.generic):
                        record[name] = value.item()
                    else:
                        record[name] = value
                rows.append(record)
            catalogues.append({"hdu_index": index, "name": hdu.name, "columns": table.colnames,
                               "rows": rows, "n_rows": len(rows)})
    return catalogues


def sources_to_table(sources: list[dict[str, Any]]):
    from astropy.table import Table
    return Table(rows=sources) if sources else Table(names=("source_id", "xcentroid", "ycentroid",
        "npix", "peak", "threshold_flux"), dtype=("i4", "f8", "f8", "i4", "f8", "f8"))
