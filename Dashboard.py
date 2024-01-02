import streamlit as st
import pandas as pd 
import plotly.express as px
import requests

st.title("DASHBOARD DE VENDAS :shopping_trolley:")

url = 'https://labdados.com/produtos'
response = requests.get(url)
dados = pd.DataFrame.from_dict(response.json())
receita_total = dados['Preço'].sum()
qtd_vendas = dados.shape[0]

st.metric('Receita',receita_total)
st.metric('Quantidade de vendas',qtd_vendas)

st.dataframe(dados)