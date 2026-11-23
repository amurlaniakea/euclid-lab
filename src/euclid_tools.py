"""Educational utilities for inspecting astronomical FITS images.

These helpers are not a replacement for the Euclid science pipeline. Preserve
units, masks, WCS metadata, calibration and provenance in scientific work.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np


def _finite_2d(data: Any) -> tuple[np.ndarray, np.ndarray]:
    """Convert input to a 2-D float array and return its finite-pixel mask."""
    array = np.asarray(data, dtype=float)
    if array.ndim != 2:
        raise ValueError(f"Expected a 2-D image array, got {array.ndim}-D data.")
    finite = np.isfinite(array)
    if not finite.any():
        raise ValueError("Image contains no finite pixels.")
    return array, finite


def image_summary(data: Any) -> dict[str, float | int]:
    """Return robust descriptive statistics for finite pixels in a 2-D image."""
    array, finite = _finite_2d(data)
    values = array[finite]
    p1, p5, p25, p75, p95, p99 = np.percentile(values, [1, 5, 25, 75, 95, 99])
    return {
        "n_pixels": int(values.size),
        "n_invalid": int(array.size - values.size),
        "minimum": float(np.min(values)),
        "maximum": float(np.max(values)),
        "mean": float(np.mean(values)),
        "median": float(np.median(values)),
        "std": float(np.std(values)),
        "p01": float(p1),
        "p05": float(p5),
        "p25": float(p25),
        "p75": float(p75),
        "p95": float(p95),
        "p99": float(p99),
    }


def display_limits(
    data: Any, lower_percentile: float = 1.0, upper_percentile: float = 99.0
) -> tuple[float, float]:
    """Calculate finite-pixel display limits from two percentiles."""
    if not (0 <= lower_percentile < upper_percentile <= 100):
        raise ValueError("Percentiles must satisfy 0 <= lower < upper <= 100.")
    array, finite = _finite_2d(data)
    low, high = np.percentile(array[finite], [lower_percentile, upper_percentile])
    if not np.isfinite(low) or not np.isfinite(high):
        raise ValueError("Could not calculate finite display limits.")
    if high <= low:
        # Constant-valued images still need a non-zero display interval.
        delta = max(abs(float(low)) * 1e-6, 1e-12)
        return float(low - delta), float(high + delta)
    return float(low), float(high)


def stretch_image(
    data: Any,
    stretch: str = "linear",
    vmin: float | None = None,
    vmax: float | None = None,
    asinh_a: float = 0.1,
) -> np.ndarray:
    """Normalize an image to [0, 1] using linear, log or asinh stretch.

    Non-finite pixels remain NaN. Values outside vmin/vmax are clipped.
    The logarithmic stretch is applied to the clipped normalized interval.
    """
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
    """Load a 2-D FITS image HDU and return detached (data, header) copies.

    Requires Astropy. The FITS file is closed before the arrays are returned.
    """
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
