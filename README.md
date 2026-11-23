
<div align="center">

# 🌌 euclid-lab
### Exploring the dark Universe with ESA's Euclid mission

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/Code%20license-MIT-green.svg)](LICENSE)
[![Mission](https://img.shields.io/badge/Mission-ESA%20Euclid-172554)](https://www.esa.int/Science_Exploration/Space_Science/Euclid)

**A bilingual (English / Español) open-science project combining an image gallery, scientific notes and reproducible Python experiments.**

[English](#english) · [Español](#español) · [Image credits](#image-credits) · [Data sources](#data--official-sources)

</div>

<a id="english"></a>
## English

`euclid-lab` is an educational and exploratory repository about the **Euclid space telescope** and its mission to investigate the dark Universe: dark matter, dark energy and the large-scale structure of the cosmos.

The project starts with ESA's **DR1-Foundation**, released on **12 November 2026**. This first major release covers approximately **1,900 square degrees**, includes observations of more than **900 million galaxies**, around **15,000 strong-lensing candidates**, and spectra for more than **160 million sources**. These are release-level figures; they are not measurements produced by this repository.

### What is inside?

- **Image gallery:** selected official Euclid images, with source links and attribution. Images are linked from the official archive rather than copied into this repository.
- **Interactive app:** a small Streamlit gallery with source links and bilingual descriptions.
- **Scientific notes:** concise introductions to the mission, dark matter, dark energy, gravitational lensing and spectroscopy.
- **Python notebooks:** starter workflows for image inspection and simple measurements.
- **Reusable code:** helpers to load 2-D FITS images, inspect robust pixel statistics, calculate percentile display limits and apply linear, logarithmic or asinh intensity stretches.

### Quick start

```bash
git clone https://github.com/<YOUR-GITHUB-USERNAME>/euclid-lab.git
cd euclid-lab

python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

Open the local URL printed by Streamlit (usually `http://localhost:8501`).

### Explore the official imagery

The following previews are served by the official Euclid image archive. If an archive endpoint changes, use the linked source page to find the current image download.

| Subject | Preview | Official source |
|---|---|---|
| Messier 81 galaxy group | ![Euclid M81 group](https://euclid.caltech.edu/download/AvmImage/86/binary/larger) | [Image record](https://euclid.caltech.edu/images) |
| Ring galaxy NGC 1291 | ![Euclid NGC 1291](https://euclid.caltech.edu/download/AvmImage/85/binary/larger) | [Image record](https://euclid.caltech.edu/images) |
| DR1 strong-lens candidates | ![Euclid lens candidates](https://euclid.caltech.edu/download/AvmImage/90/binary/larger) | [Image record](https://euclid.caltech.edu/images) |
| Northern sky mosaic | ![Euclid northern mosaic](https://euclid.caltech.edu/download/AvmImage/87/binary/larger) | [Image record](https://euclid.caltech.edu/images) |

> **Image rights:** the images above are not relicensed by this repository. Check the licence and credit line on each official image record before downloading, redistributing, modifying or rehosting it. This project links to the archive to preserve provenance and avoid silently changing image terms.

### Suggested workflow

1. Browse the image archive and select a science target.
2. Read the relevant note in `docs/`.
3. Open a notebook in `notebooks/`.
4. Record the image identifier, filter/band, units, pixel scale and archive query alongside any measurement.
5. Separate observations from interpretation; cite the paper or data product behind every scientific claim.

### Current version: v0.3.0

FITS Lab now includes percentile-based contrast controls, linear/log/asinh display stretches, expanded pixel statistics, a histogram and FITS header inspection. See [release notes](docs/release-notes-v0.3.0.md).

## Project status

This is a **starter release**. It does not reproduce the Euclid pipeline, infer dark matter directly from a colour image, or claim new astronomical discoveries. The notebooks are educational starting points, not validated scientific pipelines.

---

<a id="español"></a>
## Español

`euclid-lab` es un repositorio educativo y experimental dedicado al **telescopio espacial Euclid** y a su misión de investigar el universo oscuro: materia oscura, energía oscura y estructura a gran escala del cosmos.

La primera versión toma como punto de partida **DR1-Foundation**, publicada el **12 de noviembre de 2026**. Esta primera gran entrega cubre aproximadamente **1.900 grados cuadrados**, incluye observaciones de más de **900 millones de galaxias**, alrededor de **15.000 candidatos a lentes gravitacionales fuertes** y espectros de más de **160 millones de fuentes**. Son cifras de la publicación de datos, no resultados calculados por este repositorio.

### ¿Qué contiene?

- **Galería de imágenes:** selección de imágenes oficiales de Euclid con enlaces y créditos. Se enlazan desde el archivo oficial; no se copian al repositorio.
- **Aplicación interactiva:** pequeña galería Streamlit con descripciones bilingües y enlaces a las fuentes.
- **Notas científicas:** introducciones a la misión, materia oscura, energía oscura, lentes gravitacionales y espectroscopia.
- **Cuadernos Python:** primeros pasos para inspeccionar imágenes y realizar medidas sencillas.
- **Código reutilizable:** funciones para cargar imágenes FITS 2D, consultar estadísticas robustas, calcular límites de contraste por percentiles y aplicar escalas lineal, logarítmica o asinh.

### Inicio rápido

```bash
git clone https://github.com/<TU-USUARIO-DE-GITHUB>/euclid-lab.git
cd euclid-lab

python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

Abre la dirección local que indique Streamlit (normalmente `http://localhost:8501`).

### Estructura

```text
euclid-lab/
├── app.py
├── README.md
├── LICENSE
├── CITATION.cff
├── requirements.txt
├── assets/
│   ├── images/                 # No se redistribuyen imágenes sin verificar licencia
│   └── image_sources.csv       # Registro de fuentes y atribuciones
├── docs/
│   ├── mission.md
│   ├── dark-matter.md
│   ├── dark-energy.md
│   ├── gravitational-lensing.md
│   └── spectroscopy.md
├── notebooks/
│   ├── 01_image_exploration.ipynb
│   └── 02_fits_image_analysis.ipynb
├── src/
│   └── euclid_tools.py
└── tests/
    └── test_euclid_tools.py
```

### Versión actual: v0.3.0

El FITS Lab incorpora controles de contraste por percentiles, escalas lineal/log/asinh, estadísticas ampliadas, histograma e inspección de cabecera FITS. Consulta las [notas de versión](docs/release-notes-v0.3.0.md).

## Próximos hitos

- [x] Añadir controles de visualización y estadísticas ampliadas para imágenes FITS 2D.
- [ ] Conectar consultas reproducibles al archivo científico de Euclid.
- [ ] Incorporar productos FITS públicos y análisis con unidades físicas.
- [ ] Añadir visualización de catálogos y coordenadas celestes.
- [ ] Preparar una versión publicada de la app.

---

## Image credits

The selected image records are from the **Euclid NASA/IPAC image archive**, which presents imagery from ESA's Euclid mission and the Euclid Consortium.

Known image credit line used on the DR1-Foundation imagery includes:

> ESA/Euclid/Euclid Consortium/NASA, image processing by J.-C. Cuillandre and E. Bertin.

**Important:** credit lines and licences can differ by image. Always use the exact credit and licence shown on the individual archive record. Some DR1-Foundation material is marked **CC BY-SA 3.0 IGO or ESA Standard Licence**; the Euclid Consortium's NGC 1291 record has also displayed **CC BY-NC 3.0**. Do not assume one licence applies to every image.

## Data & official sources

- [ESA — Euclid mission](https://www.esa.int/Science_Exploration/Space_Science/Euclid)
- [ESA — DR1-Foundation announcement (12 Nov 2026)](https://www.esa.int/articles/about-us/directorates/science/euclid/euclid-lays-the-foundation-for-its-best-ever-3d-map-of-the-universe)
- [ESA — 500-gigapixel northern mosaic](https://www.esa.int/media/about-us/directorates/science/euclid/zoom-into-euclid-s-500-gigapixel-mosaic-of-the-universe)
- [Euclid NASA/IPAC — image archive](https://euclid.caltech.edu/images)
- [Euclid Consortium — DR1-Foundation](https://euclid-ec.net/)
- [ESA — Euclid Data Space](https://eas.esac.esa.int/)
- [Astropy documentation](https://docs.astropy.org/)
- [Astropy FITS documentation](https://docs.astropy.org/en/stable/io/fits/)

## Contributing

Issues and pull requests are welcome. Please include source URLs, image credits, licences, units, coordinate systems and enough information to reproduce any analysis.

## Licence

The **source code** in this repository is released under the MIT License. This does **not** grant rights to third-party images, logos, catalogues or mission data. Their original terms remain in force.
