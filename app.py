import streamlit as st
from pages import page1, page2

st.set_page_config(page_title="Mi Aplicación Appp Streamlit", layout="wide")

# Crear un menú de navegación
menu = ["Vista datos", "Utilidad"]
choice = st.sidebar.selectbox("Selecciona una página", menu)

if choice == "Vista datos":
    page1.app()
elif choice == "Utilidad":
    page2.app()
