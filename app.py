import pandas as pd
import streamlit as st

# carregar dados
df = pd.read_csv('Municipal-Diagnostico.csv', sep=';')

# título
st.title("Análise de Resíduos Sólidos")

# filtro (AQUI está a melhoria 👇)
estado = st.selectbox("Escolha um estado", df["UF Declarante"].dropna().unique())

# filtrar dados
df_estado = df[df["UF Declarante"] == estado]

# mostrar dados
st.write("Dados filtrados:")
st.write(df_estado.head())

# gráfico
st.write("Coleta seletiva:")
st.bar_chart(df_estado["Possui Coleta Seletiva Implantada"].value_counts())