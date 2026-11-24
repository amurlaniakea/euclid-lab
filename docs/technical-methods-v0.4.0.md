# v0.4.0 — technical methods / métodos técnicos

## Source detection / Detección de fuentes

The detector estimates one global background as the median of finite pixels. Its noise scale is `1.4826 × MAD`, where MAD is the median absolute deviation; standard deviation is used if MAD is zero. Pixels above `background + threshold_sigma × noise` are grouped with 8-connectivity. Groups smaller than `min_pixels` are discarded. Centroids are weighted by positive pixel excess above the global background.

El detector estima un único fondo global mediante la mediana de los píxeles finitos. La escala de ruido es `1.4826 × MAD` (desviación absoluta mediana); si MAD es cero, utiliza la desviación típica. Agrupa con conectividad de 8 los píxeles por encima de `fondo + threshold_sigma × ruido`. Descarta grupos menores que `min_pixels`. Los centroides se ponderan con el exceso positivo respecto al fondo global.

## Aperture photometry / Fotometría de apertura

The aperture flux is the sum of pixel values inside a circular aperture minus the median value measured in a concentric background annulus multiplied by the aperture pixel count. The optional instrumental magnitude is `-2.5 log10(net_flux)` for positive net flux only.

El flujo de apertura es la suma de los valores de píxel dentro de un círculo menos la mediana del anillo de fondo concéntrico multiplicada por el número de píxeles de la apertura. La magnitud instrumental opcional es `-2.5 log10(net_flux)` y solo se calcula si el flujo neto es positivo.

## Catalogue handling / Catálogos

The FITS catalogue reader scans HDUs for table-like extensions and returns column names and row values. It does not interpret column units, coordinate frames, masks or survey-specific conventions.

El lector recorre las HDU buscando extensiones de tipo tabla y devuelve nombres de columnas y valores por fila. No interpreta unidades, sistemas de coordenadas, máscaras ni convenciones específicas de cada sondeo.

## Limitations / Limitaciones

No source deblending, spatial background model, PSF fitting, gain/noise model, exposure correction, photometric zero point, aperture correction, variance propagation, mask handling or WCS conversion is implemented. This software is not an official ESA product and is not intended for publication-grade measurements.
