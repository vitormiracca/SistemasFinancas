import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from controler.analytics_dao import AnalyticsDAO
from model.conta import Conta
from model.tipo_lancamento.categoria import Categoria
from model.tipo_lancamento.despesa import Despesa
from model.tipo_lancamento.receita import Receita
from model.tipo_lancamento.tipo_lancamento import TipoLancamento

st.set_page_config(
    page_title="Home",
    page_icon="💸",
)
st.title("MyCashFlow 💸")

st.sidebar.success("FILTROS...")

analytics_dao = AnalyticsDAO()
df = analytics_dao.df_lancamentos()
st.dataframe(df)

# Calcular valores para os KPIs
total_receita = df[df['tipo_lancamento'] == 'Receita']['valor'].sum()
total_despesa = df[df['tipo_lancamento'] == 'Despesa']['valor'].sum()
perc_balanco = (total_receita - total_despesa) / total_receita * 100

# Mostrar os KPIs
st.write("## Dashboard de Receitas e Despesas 💸")
st.write("### KPIs")
st.metric(label="Total de Receitas", value=f'R${float(total_receita)}')
st.write(f"Total de Despesa: R${total_despesa:.2f}")
st.write(f"Percentual de Receita Sobrando: {perc_balanco:.2f}%")


# Agrupar e somar despesas e receitas por categoria
despesas_por_categoria = df[df['tipo_lancamento'] == 'Despesa'].groupby('nome')['valor'].sum()
despesas_por_categoria = despesas_por_categoria.abs().reset_index()  # Aplicando o valor absoluto
despesas_por_categoria['valor'] = despesas_por_categoria['valor'].astype(float)

receitas_por_categoria = df[df['tipo_lancamento'] == 'Receita'].groupby('nome')['valor'].sum()
receitas_por_categoria = receitas_por_categoria.abs().reset_index()  # Aplicando o valor absoluto
receitas_por_categoria['valor'] = receitas_por_categoria['valor'].astype(float)

# Plotar o gráfico de barras
col1, col2 = st.columns([1, 1])
with col1:
    st.write("## Despesas por Categoria")
    st.bar_chart(despesas_por_categoria, y='valor', x='nome')
with col2:
    st.write("## Receitas por Categoria")
    st.bar_chart(receitas_por_categoria, y='valor', x='nome')

# Agrupar e somar despesas por contas
despesas_por_conta = df[df['tipo_lancamento'] == 'Despesa'].groupby('conta')['valor'].sum()
despesas_por_conta = despesas_por_conta.abs().reset_index() 
despesas_por_conta['valor'] = despesas_por_conta['valor'].astype(float)

# Plotar o gráfico de pizza
st.write("## Despesas por Conta")
st.plotly_chart(despesas_por_conta.plot.pie(y='valor'))