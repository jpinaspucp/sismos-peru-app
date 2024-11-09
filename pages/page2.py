# page2.py
import streamlit as st
#import plotly.express as px
import pandas as pd



def app():
    st.title("Page dos")
    st.write("Aquí puedes integrar un cuadro de ArcGIS Dashboard.")
    #st.components.v1.iframe("URL_DEL_CUADRO_DE_ARCGIS_DASHBOARD", width=1700, height=1500)
    st.components.v1.iframe("https://gismatech4.maps.arcgis.com/apps/dashboards/2c4bf6ca48824b60b1ebcfd10bfdd881", width=1300, height=1000)
    
