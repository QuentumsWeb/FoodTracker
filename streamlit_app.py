import streamlit as st


st.set_page_config(
    page_title="NutriPhoto",
    page_icon="🍽️",
    layout="wide",
)

st.title("🍽️ NutriPhoto")
st.write("Photographier, corriger, comptabiliser.")

st.header("1. Photo du repas")

photo_importee = st.file_uploader(
    "Choisir une photo",
    type=["jpg", "jpeg", "png"],
)

photo_camera = st.camera_input(
    "Ou prendre une photo avec la caméra"
)

photo = photo_camera if photo_camera is not None else photo_importee

if photo is not None:
    st.image(
        photo,
        caption="Photo du repas",
        width="stretch",
    )

    if st.button("Analyser la photo", type="primary"):
        st.success("Photo reçue. L’analyse sera ajoutée à l’étape suivante.")
else:
    st.info("Importe ou prends une photo pour commencer.")
