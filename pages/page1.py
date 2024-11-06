# page1.py
""" import streamlit as st
import plotly.express as px
import pandas as pd

def app():
    st.title("Página 1 - Gráfico de Dispersión")
    df = px.data.iris()
    fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species')
    st.plotly_chart(fig) """
    
    # page1.py
import streamlit as st

def app():
    st.title("Page UNO")
    st.write("Aquí puedes integrar un cuadro de ArcGIS Dashboard.")
    #st.components.v1.iframe("URL_DEL_CUADRO_DE_ARCGIS_DASHBOARD", width=700, height=500)
    st.components.v1.iframe("https://oefa.maps.arcgis.com/apps/dashboards/7430e90bd060492b9a550c01f95d9843", width=700, height=500)
    
