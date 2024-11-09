# page1.py
import streamlit as st
import pandas as pd
import plotly.express as px


def app():
    #st.title("Página 1 - Gráfico de Dispersión")
    #df = px.data.iris()
    #fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species')
    # Leer el archivo CSV en un DataFrame
    df = pd.read_csv('./data/Catalogo1960_2023_actualizado.csv')
    # Convertir la columna de fecha a datetime si es necesario
    df['FECHA_UTC'] = pd.to_datetime(df['FECHA_UTC'], format='%Y/%m/%d')

    # Título principal
    st.title("Análisis de Sismos y Temblores en Perú (1960-2023)")
    
    # Descripción del dataset
    st.write("""
        Este conjunto de datos contiene información sobre los sismos y temblores registrados en Perú entre 1960 y 2023.
        Los registros incluyen diversas características clave, tales como:
        - **Fecha y hora**: El momento exacto del evento sísmico.
        - **Latitud y longitud**: La ubicación geográfica donde ocurrió el sismo.
        - **Profundidad**: La profundidad a la que se originó el sismo (en kilómetros).
        - **Magnitud**: La magnitud del evento sísmico.
    
        Con esta información, es posible analizar la frecuencia y distribución geográfica de los temblores a lo largo del tiempo, así como la relación entre la magnitud y la profundidad de los eventos sísmicos. Esta base de datos proporciona una visión detallada de la actividad sísmica en Perú, un país ubicado en una de las zonas sísmicas más activas del mundo.
    """)
    
    st.write(""" Adicional a ello, contamos con filtros por fecha y hora, para tener una visualización más amplia y concentrada de acuerdo a lo que necesitemos:""")
    
    # Filtro por fecha
    start_date = st.date_input('Fecha de inicio', df['FECHA_UTC'].min())
    end_date = st.date_input('Fecha de fin', df['FECHA_UTC'].max())
    
    # Filtrar el DataFrame según las fechas seleccionadas
    df_filtered = df[(df['FECHA_UTC'] >= pd.to_datetime(start_date)) & (df['FECHA_UTC'] <= pd.to_datetime(end_date))]
    
    # Filtro por hora (si tienes una columna de hora)
    # Asumimos que 'FECHA_UTC' también contiene información de la hora
    df_filtered['HORA'] = pd.to_datetime(df['HORA_UTC'], format='%H:%M:%S').dt.time
    df_filtered['HORA'] = df_filtered['HORA'].apply(lambda x: x.hour)
    
    # Convertir la columna 'HORA' a tipo int de Python
    df_filtered['HORA'] = df_filtered['HORA'].apply(lambda x: int(x))
    
    # Usar el slider con los valores convertidos a int
    selected_hour_range = st.slider(
        'Filtrar por hora',
        min_value=int(df_filtered['HORA'].min()),  # Asegurarse de que sea un entero de Python
        max_value=int(df_filtered['HORA'].max()),  # Asegurarse de que sea un entero de Python
        value=(int(df_filtered['HORA'].min()), int(df_filtered['HORA'].max()))  # Asegurarse de que sea un entero de Python
    )
    
    # Filtrar el DataFrame según el rango de horas
    df_filtered = df_filtered[
        (df_filtered['HORA'] >= selected_hour_range[0]) & (df_filtered['HORA'] <= selected_hour_range[1])]
    
    # Mostrar los datos filtrados
    st.dataframe(df_filtered)

    # Cargar el archivo CSV

    
    
    #st.plotly_chart(fig) ""
    
    # page1.py
    #import streamlit as st
    #
    #def app():
    #   st.title("Página 1 - Gráfico de Barras")
    #df = px.data.tips()
    #fig = px.bar(df, x='day', y='total_bill', color='sex', barmode='group')
    #st.plotly_chart(fig)