# page2.py
import streamlit as st
#import plotly.express as px
import pandas as pd



def app():
    st.title("Descubre la Seguridad de tu Hogar con Nuestra Herramienta de Visualización Sísmica")
    st.write("En un mundo donde la seguridad es primordial, conocer la actividad sísmica de tu región puede marcar la diferencia. Nuestra innovadora herramienta de visualización de sismos te permite explorar de manera interactiva los departamentos y sus datos de magnitud de sismos, brindándote información crucial para tomar decisiones informadas.")

    #st.components.v1.iframe("URL_DEL_CUADRO_DE_ARCGIS_DASHBOARD", width=1700, height=1500)

    st.title("Visualiza datos a nivel de tu Departamento:")
    st.components.v1.iframe("https://gismatech4.maps.arcgis.com/apps/dashboards/2c4bf6ca48824b60b1ebcfd10bfdd881", width=1500, height=900)
    
