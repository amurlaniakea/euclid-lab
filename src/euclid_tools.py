"""Small, educational utilities for exploring astronomical images.

These helpers do not implement the Euclid science pipeline. Always preserve
FITS metadata, units, masks and provenance in scientific work.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np


def image_summary(data: Any) -> dict[str, float | int]:
    """Return basic finite-pixel statistics for a 2-D image array."""
    array = np.asarray(data, dtype=float)
    if array.ndim != 2:
        raise ValueError("Expected a 2-D image array.")
    finite = array[np.isfinite(array)]
    if finite.size == 0:
        raise ValueError("Image contains no finite pixels.")
    return {
        "n_pixels": int(finite.size),
        "minimum": float(np.min(finite)),
        "maximum": float(np.max(finite)),
        "mean": float(np.mean(finite)),
        "median": float(np.median(finite)),
        "std": float(np.std(finite)),
    }


def load_fits_image(path: str | Path, hdu: int = 0):
    """Load a FITS HDU and return (data copy, header copy).

    Requires Astropy. Copying detaches the array/header from the open file.
    """
    from astropy.io import fits

    with fits.open(path, memmap=False) as hdul:
        data = np.array(hdul[hdu].data, copy=True)
        header = hdul[hdu].header.copy()
    if data.ndim != 2:
        raise ValueError(f"Expected a 2-D FITS image, got shape {data.shape}.")
    return data, header
