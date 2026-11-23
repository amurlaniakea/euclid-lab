# Euclid Lab v0.3.0

## FITS exploration upgrade

- Expanded finite-pixel statistics with invalid-pixel counts and percentiles.
- Added percentile-based display limits.
- Added linear, logarithmic and asinh intensity stretches.
- Added selectable colour maps and a pixel-value histogram in the Streamlit FITS Lab.
- Added FITS header inspection and selected metadata display.
- Expanded unit tests for statistics, limits and image stretches.

## Scope and scientific caveats

The laboratory accepts two-dimensional FITS image HDUs. It is an exploratory educational interface, not a calibrated Euclid processing pipeline. It does not apply masks, background subtraction, flat-fielding, astrometric calibration, variance propagation or WCS-aware reprojection. Display stretches alter visualization only; they do not modify the source FITS data.
