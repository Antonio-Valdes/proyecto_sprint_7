import pandas as pd
import streamlit as st
import plotly as pt

df = pd.read_csv("vehicles_us.csv")

# Creando aplicación
st.header("Aplicación proyecto Sprint 7")
st.dataframe(df)