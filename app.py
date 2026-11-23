from __future__ import annotations

import streamlit as st

st.set_page_config(page_title="euclid-lab | Exploring the dark Universe",
                   page_icon="🌌", layout="wide")

st.title("🌌 euclid-lab")
st.subheader("Exploring the dark Universe with ESA's Euclid mission")
st.caption("A bilingual starter project · Proyecto inicial bilingüe")

LANG = st.sidebar.selectbox("Language / Idioma", ["English", "Español"])
es = LANG == "Español"

intro = (
    "Explora imágenes oficiales, conceptos científicos y primeros experimentos reproducibles."
    if es else
    "Explore official imagery, scientific concepts and reproducible starter experiments."
)
st.write(intro)

st.info(
    "DR1-Foundation · 12 November 2026 · ~1,900 deg² · >900 million galaxies · "
    "~15,000 strong-lensing candidates"
)

images = [
    {
        "title": "Messier 81 galaxy group",
        "title_es": "Grupo de galaxias Messier 81",
        "url": "https://euclid.caltech.edu/download/AvmImage/86/binary/larger",
        "source": "https://euclid.caltech.edu/images",
        "description": "Euclid's view of the core of the Messier 81 galaxy group.",
        "description_es": "Vista de Euclid de la región central del grupo de galaxias Messier 81.",
    },
    {
        "title": "Ring galaxy NGC 1291",
        "title_es": "Galaxia anular NGC 1291",
        "url": "https://euclid.caltech.edu/download/AvmImage/85/binary/larger",
        "source": "https://euclid.caltech.edu/images",
        "description": "A ring galaxy with an inner bar and outer ring structure.",
        "description_es": "Una galaxia anular con barra interior y anillo exterior.",
    },
    {
        "title": "Strong gravitational-lens candidates",
        "title_es": "Candidatos a lentes gravitacionales fuertes",
        "url": "https://euclid.caltech.edu/download/AvmImage/90/binary/larger",
        "source": "https://euclid.caltech.edu/images",
        "description": "Examples of strong-lensing candidates identified in Euclid observations.",
        "description_es": "Ejemplos de candidatos a lente gravitacional fuerte identificados en observaciones de Euclid.",
    },
    {
        "title": "Northern sky mosaic",
        "title_es": "Mosaico del cielo del hemisferio norte",
        "url": "https://euclid.caltech.edu/download/AvmImage/87/binary/larger",
        "source": "https://euclid.caltech.edu/images",
        "description": "A large mosaic assembled from Euclid observations.",
        "description_es": "Un gran mosaico compuesto a partir de observaciones de Euclid.",
    },
]

st.header("Image gallery / Galería")
cols = st.columns(2)
for i, item in enumerate(images):
    with cols[i % 2]:
        st.image(item["url"], use_container_width=True)
        st.markdown(f"**{item['title_es'] if es else item['title']}**")
        st.write(item["description_es"] if es else item["description"])
        st.link_button("Abrir ficha oficial / Open archive" if es else "Open official archive",
                       item["source"])

st.divider()
st.header("Science themes / Temas científicos")
topics = [
    ("Materia oscura" if es else "Dark matter", "docs/dark-matter.md"),
    ("Energía oscura" if es else "Dark energy", "docs/dark-energy.md"),
    ("Lentes gravitacionales" if es else "Gravitational lensing", "docs/gravitational-lensing.md"),
    ("Espectroscopia" if es else "Spectroscopy", "docs/spectroscopy.md"),
]
for label, path in topics:
    st.markdown(f"- **{label}** — `{path}`")

st.caption(
    "Credits: ESA/Euclid/Euclid Consortium/NASA; image processing by J.-C. Cuillandre and E. Bertin "
    "(verify the exact credit and licence on each image record)."
)
st.caption("Images are embedded from the official archive; this app does not rehost them.")
