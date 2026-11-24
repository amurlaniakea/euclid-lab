<div align="center">

# 🌌 Euclid Lab
### Exploring the dark Universe with ESA's Euclid mission

<p><strong><a href="https://euclid-lab.streamlit.app/">🚀 Live Demo: https://euclid-lab.streamlit.app/</a></strong></p>

[![Tests](https://github.com/amurlaniakea/euclid-lab/actions/workflows/tests.yml/badge.svg)](https://github.com/amurlaniakea/euclid-lab/actions/workflows/tests.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Version](https://img.shields.io/badge/version-0.4.0-6c63ff)](https://github.com/amurlaniakea/euclid-lab/releases)
[![License: AGPL-3.0-or-later](https://img.shields.io/badge/License-AGPL--3.0--or--later-blue.svg)](LICENSE)

**A bilingual (English / Español) educational observatory for Euclid imagery, FITS image analysis, source detection and catalogue exploration.**

[Live app](https://euclid-lab.streamlit.app/) · [Project website](https://amurlaniakea.github.io/euclid-lab/) · [English](#english) · [Español](#español)

</div>

> **Live application:** [euclid-lab.streamlit.app](https://euclid-lab.streamlit.app/). The interactive Python application runs on Streamlit Community Cloud; the project website is published separately as a static GitHub Pages site.

<a id="english"></a>
## English

Euclid Lab is an open-source learning project about ESA's Euclid space telescope and the dark Universe. It combines a bilingual Streamlit interface, introductory science notes, notebooks and reusable Python utilities.

### Features in v0.4.0

- **Observatory and gallery:** curated links to official Euclid imagery.
- **Science notes:** dark matter, dark energy, gravitational lensing and spectroscopy.
- **FITS image laboratory:** 2-D image inspection, statistics, histogram, FITS header and linear/log/asinh display stretches.
- **Source detection:** configurable threshold in robust background sigma and connected-pixel footprint; centroids and simple source measurements.
- **Aperture photometry:** circular aperture and local annulus background estimate.
- **FITS catalogue explorer:** inspect binary-table extensions and preview rows.
- **Export:** detected-source tables as CSV or FITS.
- **Bilingual interface:** Spanish and English.

### Quick start — Linux / WSL

```bash
git clone https://github.com/amurlaniakea/euclid-lab.git
cd euclid-lab

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

pytest -q
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

### Windows PowerShell

```powershell
git clone https://github.com/amurlaniakea/euclid-lab.git
cd euclid-lab

py -3 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt

pytest -q
streamlit run app.py
```

If PowerShell blocks activation, use `.\.venv\Scripts\python.exe -m pip install -r requirements.txt` and `.\.venv\Scripts\streamlit.exe run app.py`.

### Update an existing clone

```bash
cd euclid-lab
git switch main
git pull --ff-only
source .venv/bin/activate   # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -q
```

### Repository layout

```text
euclid-lab/
├── .github/workflows/       # CI tests and GitHub Pages deployment
├── app.py                  # Streamlit application
├── assets/                 # image-source register; no unlicensed image copies
├── docs/                   # science notes and release notes
├── notebooks/              # exploratory notebooks
├── site/                   # static GitHub Pages website
├── src/euclid_tools.py     # FITS, detection, photometry and catalogue helpers
├── tests/                  # automated tests
├── requirements.txt
└── README.md
```

### Scientific scope and limitations

This is an educational prototype, not the Euclid science pipeline. Source detection uses a global median/MAD background and connected components; it does not deblend sources or model spatially varying backgrounds. Aperture photometry is not calibrated and does not apply gain, exposure time, zero point, aperture corrections, masks, variance propagation or WCS conversion. Instrumental magnitudes are not calibrated magnitudes. Pixel coordinates are zero-based `(x, y)` positions. Inspect FITS metadata, units and product documentation before interpreting measurements scientifically.

See [v0.4.0 release notes](docs/release-notes-v0.4.0.md).

---

<a id="español"></a>
## Español

Euclid Lab es un proyecto educativo de código abierto sobre el telescopio espacial Euclid de la ESA y el universo oscuro. Reúne una aplicación Streamlit bilingüe, notas científicas introductorias, cuadernos Jupyter y utilidades Python reutilizables.

### Novedades de v0.4.0

- **Observatorio y galería:** enlaces seleccionados a imágenes oficiales de Euclid.
- **Notas científicas:** materia oscura, energía oscura, lentes gravitacionales y espectroscopia.
- **Laboratorio FITS:** inspección de imágenes 2D, estadísticas, histogramas, cabeceras y escalas lineal/log/asinh.
- **Detección de fuentes:** umbral configurable respecto al fondo robusto y tamaño mínimo de píxel conectado; centroides y medidas básicas.
- **Fotometría de apertura:** apertura circular y estimación del fondo mediante un anillo local.
- **Explorador de catálogos FITS:** lectura de extensiones de tablas binarias y vista previa de filas.
- **Exportación:** tablas de fuentes detectadas en CSV o FITS.
- **Interfaz bilingüe:** español e inglés.

### Inicio rápido — Linux / WSL

```bash
git clone https://github.com/amurlaniakea/euclid-lab.git
cd euclid-lab

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt

pytest -q
streamlit run app.py
```

Abre `http://localhost:8501` en el navegador.

### Windows PowerShell

```powershell
git clone https://github.com/amurlaniakea/euclid-lab.git
cd euclid-lab

py -3 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt

pytest -q
streamlit run app.py
```

Si PowerShell impide activar el entorno, puedes usar directamente `.\.venv\Scripts\python.exe -m pip install -r requirements.txt` y `.\.venv\Scripts\streamlit.exe run app.py`.

### Actualizar una copia existente

```bash
cd euclid-lab
git switch main
git pull --ff-only
source .venv/bin/activate   # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -q
```

### Alcance y limitaciones científicas

Es un prototipo educativo, no el pipeline científico de Euclid. La detección emplea un fondo global mediana/MAD y componentes conectados; no separa fuentes solapadas ni modela fondos espaciales variables. La fotometría no está calibrada: no aplica ganancia, tiempo de exposición, punto cero, correcciones de apertura, máscaras, propagación de varianza ni conversión WCS. Las magnitudes instrumentales no son magnitudes astronómicas calibradas. Las coordenadas de píxel `(x, y)` empiezan en cero. Antes de interpretar resultados, comprueba las unidades, metadatos y documentación del producto FITS.

Consulta las [notas de versión v0.4.0](docs/release-notes-v0.4.0.md).

---

## Deployment

### 1. Streamlit Community Cloud — interactive Python app

1. Push this repository to GitHub.
2. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/) with the GitHub account that can access this repository.
3. Choose **Create app**, repository `amurlaniakea/euclid-lab`, branch `main`, main file `app.py`.
4. Deploy. The service installs dependencies from `requirements.txt`.
5. The public application is available at [https://euclid-lab.streamlit.app/](https://euclid-lab.streamlit.app/). If you change the app subdomain, update the Live Demo links in this README and in `site/index.html`.

The app is not hosted by GitHub Pages.

### 2. GitHub Pages — static project website

1. Push the repository including `site/` and `.github/workflows/pages.yml`.
2. In GitHub open **Settings → Pages**.
3. Under **Build and deployment → Source**, select **GitHub Actions**.
4. Open the **Actions** tab and check the `Deploy GitHub Pages` workflow.
5. When it completes successfully, the static site should be available at `https://amurlaniakea.github.io/euclid-lab/`.

The Pages workflow deploys only the static files in `site/`; it does not run Streamlit.

## Tests

```bash
pytest -q
```

GitHub Actions runs the test suite on pushes and pull requests to `main`.

## Official mission and data links

- [ESA — Euclid mission](https://www.esa.int/Science_Exploration/Space_Science/Euclid)
- [Euclid NASA/IPAC image archive](https://euclid.caltech.edu/images)
- [ESA Euclid Archive / Euclid Data Space](https://eas.esa.int/)
- [Astropy documentation](https://docs.astropy.org/)
- [Astropy FITS documentation](https://docs.astropy.org/en/stable/io/fits/)

## Image credits and licence

Image URLs are linked from the official archive; this repository does not relicense third-party imagery. Check each image record for its specific credit and licence. Source code is licensed under the **GNU Affero General Public License v3.0 or any later version (AGPL-3.0-or-later)**; see [LICENSE](LICENSE) and the [official licence text](https://www.gnu.org/licenses/agpl-3.0.html). This licence does not apply to third-party images, logos or mission data.

## Contributing

Issues and pull requests are welcome. Include source URLs, image credits, licences, units, coordinate systems and enough detail to reproduce any analysis.
