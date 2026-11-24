# Euclid Lab v0.4.0

## Source detection and catalogue exploration

- Added robust global background estimation using the median and MAD (with a standard-deviation fallback).
- Added connected-component source detection with configurable significance threshold and minimum footprint.
- Added source centroids, peak values, pixel counts and threshold-excess flux estimates.
- Added circular-aperture photometry with a local median annulus background and instrumental magnitude when net flux is positive.
- Added FITS binary-table catalogue inspection.
- Added CSV and FITS exports for detected-source tables.
- Added a bilingual Streamlit page for source analysis and catalogue browsing.
- Added automated tests for synthetic source detection, aperture photometry and FITS table reading.

## Scientific limitations

This release is an educational prototype. Detection uses a single global background estimate, 8-connected pixels and no deblending; crowded fields, gradients, artifacts and extended sources can produce biased results. Aperture photometry is not calibrated: no gain, exposure-time, zero-point, aperture correction, variance map, masking, correlated-noise correction or WCS transformation is applied. The reported instrumental magnitude is only `-2.5 log10(net_flux)` and is not a calibrated astronomical magnitude. Coordinates are zero-based pixel positions, not sky coordinates.

The FITS catalogue explorer displays table extensions; it does not query the Euclid archive or infer column semantics. Always inspect units, masks, metadata, provenance and the original product documentation before scientific use.
