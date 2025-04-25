import streamlit as st
import pandas as pd
import plotly.express as px


car_data = pd.read_csv('vehicles_us.csv')

st.header('Panel de Control de Anuncios de Venta de Coches')

hist_button = st.button('Construir Histograma de Kilometraje')
if hist_button:
    st.write('Generando un histograma de la columna "odometer"...')
    fig_hist = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig_hist, use_container_width=True)

scatter_button = st.button('Construir Gráfico de Dispersión de Precio vs. Año')
if scatter_button:
    st.write('Generando un gráfico de dispersión entre "year" y "price"...')
    fig_scatter = px.scatter(car_data, x='model_year', y='price')
    st.plotly_chart(fig_scatter, use_container_width=True)