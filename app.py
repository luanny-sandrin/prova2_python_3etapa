import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Prova Python", page_icon="❤", layout="centered")

st.title("Índice de Qualidade de Vida Urbana (IQVU) dos bairros de Belo Horizonte")
st.header("Dados")

df = pd.read_csv("bd_iqvu_1994_2016.csv", sep=";", encoding="latin-1", decimal=",")
df.columns = df.columns.str.replace("\ufeff", "", regex=False) .str.strip()


df_filtrado = df[
    (df["NOMEUP"].isin(["Taquaril", "Santa Ines"])) &
    (df["ï»¿SERIE"] == "SERIE HISTORICA")
].copy()

df_filtrado

st.write("https://dados.pbh.gov.br/")

st.markdown('# :red[PROFESSORA EU FIZ TUDO ERRADO, DESCULPA EU AÍ 😭😭]')
with st.sidebar:
    st.header("Filtrar")