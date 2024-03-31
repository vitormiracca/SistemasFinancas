import os
import streamlit as st
from model.conta import Conta
from model.tipo_lancamento.categoria import Categoria
from model.tipo_lancamento.despesa import Despesa
from model.tipo_lancamento.receita import Receita
from model.tipo_lancamento.tipo_lancamento import TipoLancamento

st.set_page_config(
    page_title="Home",
    page_icon="💸",
)

st.write("# MyCashFlow 💸")

st.sidebar.success("Registre seus Lançamentos.")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)