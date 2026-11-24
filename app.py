from __future__ import annotations

from pathlib import Path

import streamlit as st

ROOT = Path(__file__).parent
DOCS = ROOT / "docs"

st.set_page_config(
    page_title="EUCLID LAB · Exploring the dark Universe",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Visual system ----------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;500;600;700;800&display=swap');

    :root {
      --ink: #edf3ff;
      --muted: #9eacc4;
      --line: rgba(167, 190, 230, .16);
      --panel: rgba(14, 25, 47, .76);
      --cyan: #78e4ee;
      --violet: #a9a0ff;
    }
    html, body, [class*="css"] { font-family: 'Manrope', sans-serif; }
    .stApp {
      background:
        radial-gradient(ellipse at 82% 0%, rgba(75, 82, 160, .22), transparent 36%),
        radial-gradient(ellipse at 4% 18%, rgba(29, 137, 164, .13), transparent 30%),
        linear-gradient(145deg, #050b17 0%, #091326 48%, #070d1b 100%);
      color: var(--ink);
    }
    [data-testid="stHeader"] { background: rgba(5, 11, 23, .72); }
    [data-testid="stSidebar"] {
      background: linear-gradient(180deg, #0a1427 0%, #080f1e 100%);
      border-right: 1px solid var(--line);
    }
    [data-testid="stSidebar"] * { color: var(--ink); }
    .block-container { padding-top: 2.2rem; padding-bottom: 4rem; max-width: 1420px; }
    h1, h2, h3 { letter-spacing: -.035em; color: #f4f7ff; }
    h1 { font-weight: 800; }
    p, li { color: #c3cee1; }
    a { color: var(--cyan) !important; }
    .eyebrow {
      color: var(--cyan); font: 500 .72rem 'DM Mono', monospace;
      letter-spacing: .18em; text-transform: uppercase;
    }
    .hero {
      position: relative; overflow: hidden; padding: 2.6rem 2.8rem;
      border: 1px solid rgba(151, 181, 235, .22); border-radius: 24px;
      background:
        linear-gradient(105deg, rgba(8, 18, 37, .97) 0%, rgba(14, 29, 57, .88) 54%, rgba(28, 31, 72, .66) 100%),
        url('https://euclid.caltech.edu/download/AvmImage/87/binary/larger') center 42% / cover;
      box-shadow: 0 24px 80px rgba(0,0,0,.28);
      min-height: 290px;
    }
    .hero:after {
      content: ""; position:absolute; inset:0; pointer-events:none;
      background: linear-gradient(90deg, rgba(5,11,23,.12), transparent 75%);
    }
    .hero-content { position:relative; z-index:1; max-width: 760px; }
    .hero h1 { font-size: clamp(2.5rem, 5vw, 4.7rem); line-height: .98; margin: .65rem 0 1rem; }
    .hero p { font-size: 1.05rem; line-height: 1.7; max-width: 660px; color: #d1dbed; }
    .hero-tag {
      display:inline-block; border:1px solid rgba(120,228,238,.42);
      color:var(--cyan); border-radius:999px; padding:.38rem .75rem;
      font: .68rem 'DM Mono', monospace; letter-spacing:.08em;
      background:rgba(8,26,43,.5);
    }
    .metric {
      background: linear-gradient(145deg, rgba(19,34,61,.9), rgba(11,21,40,.78));
      border:1px solid var(--line); border-radius:17px; padding:1.1rem 1.2rem;
      min-height:112px;
    }
    .metric-value { font-size:1.8rem; font-weight:800; color:#f4f7ff; letter-spacing:-.04em; }
    .metric-label { color:var(--muted); font-size:.77rem; margin-top:.25rem; }
    .section-kicker {
      color:var(--cyan); font: .7rem 'DM Mono', monospace; letter-spacing:.16em;
      text-transform:uppercase; margin-bottom:.45rem;
    }
    .section-title { font-size:1.8rem; font-weight:800; margin:0 0 .35rem; color:#f4f7ff; }
    .section-sub { color:var(--muted); margin-bottom:1.25rem; }
    .glass-card {
      background:var(--panel); border:1px solid var(--line); border-radius:18px;
      padding:1.1rem 1.2rem; height:100%;
    }
    .glass-card h3 { font-size:1.05rem; margin:.25rem 0 .5rem; }
    .glass-card p { font-size:.9rem; line-height:1.6; color:#aebbd1; }
    .mono { font-family:'DM Mono',monospace; color:var(--cyan); font-size:.72rem; letter-spacing:.08em; }
    .stButton > button, .stLinkButton > a {
      border-radius:999px !important; border:1px solid rgba(120,228,238,.38) !important;
      background:rgba(25,64,84,.48) !important; color:#dffcff !important;
    }
    [data-testid="stImage"] img { border-radius:14px; border:1px solid var(--line); }
    hr { border-color:var(--line); }
    [data-testid="stMetric"] {
      background:var(--panel); padding:1rem; border:1px solid var(--line); border-radius:16px;
    }
    [data-testid="stMetricLabel"] { color:var(--muted); }
    .footer { color:#71819d; font: .68rem 'DM Mono',monospace; letter-spacing:.06em; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown('<div class="eyebrow">MISSION CONTROL</div>', unsafe_allow_html=True)
    st.markdown("## 🌌 EUCLID LAB")
    st.caption("A digital observatory · Un observatorio digital")
    language = st.selectbox("Language / Idioma", ["Español", "English"], index=0)
    es = language == "Español"
    pages = ["Observatorio", "Galería", "Ciencia", "Laboratorio", "Fuentes y catálogos"] if es else [
        "Observatory", "Gallery", "Science", "Laboratory", "Sources & catalogues"
    ]
    page = st.radio("Navegación / Navigation", pages, label_visibility="collapsed")
    st.divider()
    st.markdown('<div class="mono">ESA · EUCLID MISSION</div>', unsafe_allow_html=True)
    st.caption("Mapping the geometry of the dark Universe.")
    st.caption("Explorando la geometría del universo oscuro.")

# ---------- Content helpers ----------
def heading(kicker: str, title: str, subtitle: str) -> None:
    st.markdown(
        f'<div class="section-kicker">{kicker}</div>'
        f'<div class="section-title">{title}</div>'
        f'<div class="section-sub">{subtitle}</div>',
        unsafe_allow_html=True,
    )

images = [
    {
        "title": "Messier 81 galaxy group",
        "title_es": "Grupo de galaxias Messier 81",
        "url": "https://euclid.caltech.edu/download/AvmImage/86/binary/larger",
        "source": "https://euclid.caltech.edu/images",
        "description": "Euclid's view of the core of the Messier 81 galaxy group.",
        "description_es": "Vista de Euclid de la región central del grupo de galaxias Messier 81.",
        "tag": "GALAXY GROUP",
    },
    {
        "title": "Ring galaxy NGC 1291",
        "title_es": "Galaxia anular NGC 1291",
        "url": "https://euclid.caltech.edu/download/AvmImage/85/binary/larger",
        "source": "https://euclid.caltech.edu/images",
        "description": "A ring galaxy with an inner bar and outer ring structure.",
        "description_es": "Una galaxia anular con barra interior y estructura de anillo exterior.",
        "tag": "GALAXY MORPHOLOGY",
    },
    {
        "title": "Strong gravitational-lens candidates",
        "title_es": "Candidatos a lentes gravitacionales fuertes",
        "url": "https://euclid.caltech.edu/download/AvmImage/90/binary/larger",
        "source": "https://euclid.caltech.edu/images",
        "description": "Examples of strong-lensing candidates identified in Euclid observations.",
        "description_es": "Ejemplos de candidatos a lente gravitacional fuerte identificados en observaciones de Euclid.",
        "tag": "GRAVITATIONAL LENSING",
    },
    {
        "title": "Northern sky mosaic",
        "title_es": "Mosaico del cielo del hemisferio norte",
        "url": "https://euclid.caltech.edu/download/AvmImage/87/binary/larger",
        "source": "https://euclid.caltech.edu/images",
        "description": "A large mosaic assembled from Euclid observations.",
        "description_es": "Un gran mosaico compuesto a partir de observaciones de Euclid.",
        "tag": "WIDE FIELD",
    },
]

topics = [
    ("Materia oscura" if es else "Dark matter", "dark-matter.md",
     "La masa invisible que curva la luz." if es else "Invisible mass revealed through its gravitational effects."),
    ("Energía oscura" if es else "Dark energy", "dark-energy.md",
     "La expansión acelerada del universo." if es else "The accelerated expansion of the Universe."),
    ("Lentes gravitacionales" if es else "Gravitational lensing", "gravitational-lensing.md",
     "La gravedad como telescopio cósmico." if es else "Gravity acting as a cosmic telescope."),
    ("Espectroscopia" if es else "Spectroscopy", "spectroscopy.md",
     "Luz, composición y distancias cósmicas." if es else "Light, composition and cosmic distances."),
]

# ---------- Observatory ----------
if page == pages[0]:
    hero_title = "El universo oscuro,<br>cartografiado." if es else "The dark Universe,<br>mapped."
    hero_text = (
        "Un espacio para explorar las observaciones de Euclid, comprender la estructura cósmica "
        "y experimentar con datos astronómicos reproducibles."
        if es else
        "Explore Euclid observations, investigate cosmic structure and experiment with reproducible astronomical data."
    )
    st.markdown(
        f"""
        <div class="hero"><div class="hero-content">
          <div class="hero-tag">ESA · EUCLID SPACE TELESCOPE</div>
          <div class="eyebrow" style="margin-top:1.2rem">COSMIC CARTOGRAPHY / CARTOGRAFÍA CÓSMICA</div>
          <h1>{hero_title}</h1>
          <p>{hero_text}</p>
        </div></div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    c1, c2, c3, c4 = st.columns(4)
    metrics = [
        ("~1,900 deg²", "Área cubierta · DR1-Foundation" if es else "Area covered · DR1-Foundation"),
        (">900 M", "Galaxias" if es else "Galaxies"),
        ("~15,000", "Candidatos a lentes fuertes" if es else "Strong-lensing candidates"),
        (">160 M", "Espectros" if es else "Spectra"),
    ]
    for col, (value, label) in zip((c1, c2, c3, c4), metrics):
        with col:
            st.markdown(
                f'<div class="metric"><div class="metric-value">{value}</div>'
                f'<div class="metric-label">{label}</div></div>',
                unsafe_allow_html=True,
            )
    st.write("")
    heading(
        "01 / OBSERVATIONS",
        "Una nueva mirada al cosmos" if es else "A new view of the cosmos",
        "Imágenes del archivo oficial de Euclid" if es else "Imagery from the official Euclid archive",
    )
    cols = st.columns(2, gap="large")
    for i, item in enumerate(images[:2]):
        with cols[i]:
            st.image(item["url"], width="stretch")
            st.markdown(f'<div class="mono">{item["tag"]}</div>', unsafe_allow_html=True)
            st.subheader(item["title_es"] if es else item["title"])
            st.caption(item["description_es"] if es else item["description"])
    st.write("")
    heading(
        "02 / RESEARCH",
        "Explora las grandes preguntas" if es else "Explore the big questions",
        "Cuatro líneas científicas para empezar" if es else "Four scientific paths to get started",
    )
    cols = st.columns(4, gap="medium")
    for col, (name, filename, desc) in zip(cols, topics):
        with col:
            st.markdown(
                f'<div class="glass-card"><div class="mono">RESEARCH NOTE</div>'
                f'<h3>{name}</h3><p>{desc}</p></div>',
                unsafe_allow_html=True,
            )
    st.write("")
    st.info(
        "Nota: las cifras corresponden al resumen DR1-Foundation descrito en el proyecto. "
        "Consulta las publicaciones oficiales para contexto, definiciones y actualizaciones."
        if es else
        "Note: figures refer to the DR1-Foundation summary described in this project. "
        "Consult official releases for context, definitions and updates."
    )

# ---------- Gallery ----------
elif page == pages[1]:
    heading(
        "03 / IMAGE ARCHIVE",
        "Galería de Euclid" if es else "Euclid image gallery",
        "Una selección de vistas y fenómenos observados por la misión." if es
        else "A selection of views and phenomena observed by the mission.",
    )
    for start in range(0, len(images), 2):
        cols = st.columns(2, gap="large")
        for col, item in zip(cols, images[start:start + 2]):
            with col:
                st.image(item["url"], width="stretch")
                st.markdown(f'<div class="mono">{item["tag"]}</div>', unsafe_allow_html=True)
                st.subheader(item["title_es"] if es else item["title"])
                st.write(item["description_es"] if es else item["description"])
                st.link_button(
                    "Abrir archivo oficial ↗" if es else "Open official archive ↗",
                    item["source"],
                )
    st.caption(
        "Créditos y licencias: verifica la ficha individual de cada imagen en el archivo oficial."
        if es else
        "Credits and licences: verify each image's individual record in the official archive."
    )

# ---------- Science ----------
elif page == pages[2]:
    heading(
        "04 / SCIENCE",
        "Ciencia del universo oscuro" if es else "Science of the dark Universe",
        "Notas introductorias del proyecto. No sustituyen publicaciones científicas ni documentación de misión."
        if es else "Introductory project notes. They do not replace scientific papers or mission documentation.",
    )
    labels = [x[0] for x in topics]
    selected = st.selectbox("Tema científico" if es else "Research topic", labels)
    filename = next(x[1] for x in topics if x[0] == selected)
    path = DOCS / filename
    if path.exists():
        st.markdown("---")
        st.markdown(path.read_text(encoding="utf-8"))
    else:
        st.warning("No se encontró la nota seleccionada." if es else "The selected note was not found.")

# ---------- Source detection and catalogues ----------
elif page == pages[4]:
    from io import BytesIO
    import tempfile
    import numpy as np
    import matplotlib.pyplot as plt
    from astropy.io import fits
    from src.euclid_tools import (
        load_fits_image, detect_sources, aperture_photometry, read_fits_catalogues, sources_to_table
    )

    heading(
        "06 / SOURCE ANALYSIS",
        "Detección de fuentes y catálogos" if es else "Source detection & catalogues",
        "Detección por umbral, fotometría de apertura y lectura de tablas FITS. "
        "Resultados exploratorios, no calibrados." if es else
        "Threshold-based detection, aperture photometry and FITS table inspection. "
        "Exploratory, uncalibrated results."
    )
    uploaded_image = st.file_uploader(
        "Imagen FITS 2D" if es else "2-D FITS image", type=["fits", "fit", "fts"], key="source_image"
    )
    if uploaded_image is not None:
        with tempfile.NamedTemporaryFile(suffix=".fits") as tmp:
            tmp.write(uploaded_image.getvalue())
            tmp.flush()
            try:
                data, header = load_fits_image(tmp.name)
                c1, c2 = st.columns(2)
                with c1:
                    threshold_sigma = st.number_input(
                        "Umbral (sigma)" if es else "Detection threshold (sigma)",
                        min_value=1.0, max_value=20.0, value=5.0, step=0.5
                    )
                with c2:
                    min_pixels = st.number_input(
                        "Píxeles mínimos" if es else "Minimum connected pixels",
                        min_value=1, max_value=100, value=3, step=1
                    )
                sources = detect_sources(data, threshold_sigma, int(min_pixels))
                st.metric("Fuentes detectadas" if es else "Detected sources", len(sources))
                fig, ax = plt.subplots(figsize=(10, 7))
                finite = data[np.isfinite(data)]
                lo, hi = np.percentile(finite, [1, 99])
                ax.imshow(data, origin="lower", cmap="magma", vmin=lo, vmax=hi)
                if sources:
                    ax.scatter([s["xcentroid"] for s in sources], [s["ycentroid"] for s in sources],
                               s=55, facecolors="none", edgecolors="cyan", linewidths=1)
                    for source in sources:
                        ax.annotate(str(source["source_id"]), (source["xcentroid"], source["ycentroid"]),
                                    color="white", fontsize=7)
                ax.set_title("Detected sources · zero-based pixel coordinates")
                ax.set_xlabel("X pixel"); ax.set_ylabel("Y pixel")
                fig.tight_layout()
                st.pyplot(fig); plt.close(fig)
                if sources:
                    st.dataframe(sources, use_container_width=True)
                    table = sources_to_table(sources)
                    csv_buffer = BytesIO()
                    table.write(csv_buffer, format="csv", overwrite=True)
                    fits_buffer = BytesIO()
                    fits.HDUList([fits.PrimaryHDU(), fits.BinTableHDU(table, name="SOURCES")]).writeto(
                        fits_buffer, overwrite=True
                    )
                    d1, d2 = st.columns(2)
                    d1.download_button("Exportar CSV" if es else "Export CSV",
                        csv_buffer.getvalue(), "euclid_sources.csv", "text/csv")
                    d2.download_button("Exportar FITS" if es else "Export FITS",
                        fits_buffer.getvalue(), "euclid_sources.fits", "application/fits")
                    st.markdown("#### " + ("Fotometría de apertura" if es else "Aperture photometry"))
                    selected_id = st.selectbox(
                        "Fuente" if es else "Source",
                        [int(s["source_id"]) for s in sources]
                    )
                    radius = st.slider("Radio de apertura (px)" if es else "Aperture radius (px)",
                                       1.0, 20.0, 4.0, 0.5)
                    selected = sources[selected_id - 1]
                    phot = aperture_photometry(data, selected["xcentroid"], selected["ycentroid"], radius)
                    st.json(phot)
                else:
                    st.info("No se detectaron fuentes con estos parámetros." if es else
                            "No sources found with these settings.")
            except Exception as exc:
                st.error(f"No se pudo analizar la imagen: {exc}" if es else
                         f"Could not analyse image: {exc}")
    st.divider()
    st.markdown("#### " + ("Explorador de catálogos FITS" if es else "FITS catalogue explorer"))
    uploaded_catalogue = st.file_uploader(
        "Tabla FITS" if es else "FITS table", type=["fits", "fit", "fts"], key="fits_catalogue"
    )
    if uploaded_catalogue is not None:
        with tempfile.NamedTemporaryFile(suffix=".fits") as tmp:
            tmp.write(uploaded_catalogue.getvalue()); tmp.flush()
            try:
                catalogues = read_fits_catalogues(tmp.name)
                if not catalogues:
                    st.warning("No se encontraron extensiones de tabla." if es else
                               "No table extensions were found.")
                for catalogue in catalogues:
                    st.subheader(f"HDU {catalogue['hdu_index']} · {catalogue['name']}")
                    st.caption(f"{catalogue['n_rows']} filas · {len(catalogue['columns'])} columnas"
                               if es else
                               f"{catalogue['n_rows']} rows · {len(catalogue['columns'])} columns")
                    st.dataframe(catalogue["rows"], use_container_width=True)
            except Exception as exc:
                st.error(f"No se pudo leer el catálogo: {exc}" if es else
                         f"Could not read catalogue: {exc}")

# ---------- Laboratory ----------
else:
    heading(
        "05 / DATA LAB",
        "Laboratorio FITS avanzado" if es else "Advanced FITS laboratory",
        "Explora la intensidad, el contraste, la distribución de píxeles y la cabecera FITS. "
        "Herramienta educativa; no sustituye un pipeline científico."
        if es else
        "Explore intensity, contrast, pixel distribution and the FITS header. "
        "Educational tool; not a replacement for a scientific pipeline.",
    )
    uploaded = st.file_uploader(
        "Selecciona un archivo FITS" if es else "Choose a FITS file",
        type=["fits", "fit", "fts"],
    )
    if uploaded is not None:
        import tempfile
        import numpy as np
        import matplotlib.pyplot as plt
        from src.euclid_tools import display_limits, image_summary, load_fits_image, stretch_image

        with tempfile.NamedTemporaryFile(suffix=".fits") as tmp:
            tmp.write(uploaded.getvalue())
            tmp.flush()
            try:
                data, header = load_fits_image(tmp.name)
                stats = image_summary(data)
                st.markdown("#### " + ("Resumen de la imagen" if es else "Image summary"))
                m1, m2, m3, m4 = st.columns(4)
                m1.metric("Píxeles válidos" if es else "Finite pixels", f"{stats['n_pixels']:,}")
                m2.metric("No válidos" if es else "Invalid pixels", f"{stats['n_invalid']:,}")
                m3.metric("Mediana" if es else "Median", f"{stats['median']:.5g}")
                m4.metric("Desv. típica" if es else "Std. deviation", f"{stats['std']:.5g}")

                st.caption(
                    f"Dimensiones: {data.shape[1]} × {data.shape[0]} px · "
                    f"dtype: {data.dtype} · "
                    f"mín: {stats['minimum']:.5g} · máx: {stats['maximum']:.5g}"
                    if es else
                    f"Dimensions: {data.shape[1]} × {data.shape[0]} px · "
                    f"dtype: {data.dtype} · "
                    f"min: {stats['minimum']:.5g} · max: {stats['maximum']:.5g}"
                )

                st.markdown("#### " + ("Controles de visualización" if es else "Display controls"))
                left, right = st.columns([1, 1])
                with left:
                    stretch_label = st.selectbox(
                        "Escala de intensidad" if es else "Intensity stretch",
                        ["Lineal", "Logarítmica", "Asinh"] if es else ["Linear", "Logarithmic", "Asinh"],
                    )
                    stretch_map = {
                        ("Lineal" if es else "Linear"): "linear",
                        ("Logarítmica" if es else "Logarithmic"): "log",
                        "Asinh": "asinh",
                    }
                    stretch = stretch_map[stretch_label]
                    cmap = st.selectbox(
                        "Mapa de color" if es else "Colour map",
                        ["magma", "viridis", "inferno", "gray", "cividis"],
                        index=0,
                    )
                with right:
                    low_pct, high_pct = st.slider(
                        "Percentiles de contraste" if es else "Contrast percentiles",
                        min_value=0, max_value=100, value=(1, 99), step=1,
                    )
                    asinh_a = st.number_input(
                        "Parámetro asinh" if es else "Asinh parameter",
                        min_value=0.001, max_value=1.0, value=0.1, step=0.01,
                        disabled=(stretch != "asinh"),
                    )

                vmin, vmax = display_limits(data, low_pct, high_pct)
                display = stretch_image(data, stretch=stretch, vmin=vmin, vmax=vmax, asinh_a=asinh_a)
                fig, ax = plt.subplots(figsize=(10, 6))
                image_artist = ax.imshow(display, origin="lower", cmap=cmap, vmin=0, vmax=1, interpolation="nearest")
                ax.set_title(uploaded.name)
                ax.set_xlabel("X pixel")
                ax.set_ylabel("Y pixel")
                fig.colorbar(image_artist, ax=ax, label="Normalized intensity")
                fig.tight_layout()
                st.pyplot(fig)
                plt.close(fig)
                st.caption(
                    f"Visualización normalizada · límites de datos: {vmin:.5g} a {vmax:.5g} · "
                    f"escala: {stretch_label}"
                )

                st.markdown("#### " + ("Distribución de píxeles" if es else "Pixel distribution"))
                finite = np.asarray(data, dtype=float)
                finite = finite[np.isfinite(finite)]
                hist_fig, hist_ax = plt.subplots(figsize=(10, 3))
                hist_ax.hist(finite, bins=60, histtype="stepfilled", alpha=0.75)
                hist_ax.set_xlabel("Pixel value")
                hist_ax.set_ylabel("Count")
                hist_ax.set_title("Finite pixel-value histogram")
                hist_ax.grid(alpha=0.2)
                hist_fig.tight_layout()
                st.pyplot(hist_fig)
                plt.close(hist_fig)

                with st.expander("Estadísticas completas / Full statistics"):
                    stat_cols = st.columns(3)
                    for col, key in zip(stat_cols * 5, [
                        "mean", "median", "std", "minimum", "maximum",
                        "p01", "p05", "p25", "p75", "p95", "p99",
                    ]):
                        col.write(f"**{key}**")
                        col.write(f"{stats[key]:.7g}")

                with st.expander("Cabecera FITS / FITS header"):
                    st.code(str(header), language="text")
                    selected_keys = ["OBJECT", "TELESCOP", "INSTRUME", "FILTER", "BUNIT",
                                     "EXPTIME", "DATE-OBS", "CRVAL1", "CRVAL2", "CDELT1", "CDELT2"]
                    metadata = {key: header[key] for key in selected_keys if key in header}
                    if metadata:
                        st.json(metadata)
            except Exception as exc:
                st.error(
                    f"No se pudo analizar el FITS: {exc}" if es
                    else f"Could not analyse the FITS file: {exc}"
                )
    else:
        st.markdown(
            '<div class="glass-card"><div class="mono">FITS · IMAGE EXPLORATION</div>'
            '<h3>Del archivo al análisis</h3>'
            '<p>Sube una imagen FITS bidimensional para explorar estadísticas, '
            'contraste lineal/logarítmico/asinh, histogramas y metadatos de cabecera.</p></div>',
            unsafe_allow_html=True,
        )

st.divider()
st.markdown(
    '<div class="footer">EUCLID LAB · OPEN SCIENCE STARTER PROJECT · '
    'IMAGES EMBEDDED FROM THE OFFICIAL ARCHIVE · VERIFY PER-IMAGE CREDITS</div>',
    unsafe_allow_html=True,
)
