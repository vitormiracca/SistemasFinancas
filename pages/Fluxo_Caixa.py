# carregando as bibliotecas
import streamlit as st

from model.conta import Conta
from model.tipo_lancamento.categoria import Categoria
from model.tipo_lancamento.despesa import Despesa
from model.tipo_lancamento.receita import Receita
from model.tipo_lancamento.tipo_lancamento import TipoLancamento

#region Preparando ambiente para teste

# Adiciona categorias
categoria_receita = ['Salário', 'Benefícios', 'Outros', 'Devedores', 'Rendimentos']
categoria_despesa = ['Supermercado', 'Alimentação', 'Shopping', 'Estudo', 'Assinaturas Digitais', 'Tabacaria', 'Outros', 'Despesas Carro']
for i in categoria_receita:
    Categoria(TipoLancamento.RECEITA, i)
for i in categoria_despesa:
    Categoria(TipoLancamento.DESPESA, i)
Categoria(TipoLancamento.TRANSFERENCIA, "Transferência")

nu_conta = Conta("Nubank", "Conta Corrente")
nu_credito = Conta("Nubank Crédito", "Crédito")
bradesco_credito = Conta("Bradesco Cartões", "Crédito")
ticket_vale = Conta("Ticket", "Vale Refeição")

Receita('2024-02-01', 1959.10, "Salário", nu_conta, "Salário dia 01")
Receita('2024-02-01', 750, "Benefícios", ticket_vale, "VR dia 01")
Despesa('2024-02-01', 55.5, "Alimentação", ticket_vale, "Mc Donalds")
Despesa('2024-02-01', 198.90, "Estudo", bradesco_credito, "Workshop Databricks")
Despesa('2024-02-01', 49, "Tabacaria", nu_conta, "")
Despesa('2024-02-01', 250, "Despesas Carro", bradesco_credito, "Gasolina")
Despesa('2024-02-01', 750, "Supermercado", ticket_vale, "NT")
Receita('2024-02-15', 1580, "Salário", nu_conta, "Salário dia 15")

#endregion

st.set_page_config(page_title="Fluxo_Caixa", page_icon="📈")
st.title('Inserir Lançamento')
st.sidebar.success("Registre seus Lançamentos.")

contas = Conta.listar_contas()
tipos_lancamentos_str = TipoLancamento.listar_tipos_str()

### Formulário ###
input_tipo_lancamento = st.radio("Tipo de Lançamento", tipos_lancamentos_str, horizontal=True, )

col1, col2 = st.columns([1, 1])
with col1:
    input_data_lancamento = st.date_input(label='Data do Lançamento', format="DD/MM/YYYY")
    input_conta = st.selectbox(label='Conta Usada',
                                options=contas)
with col2:
    input_valor_lancamento = st.number_input(label='Valor do Lançamento', step=0.01)
    st.date_input(label="Data do Débito", format="DD/MM/YYYY", disabled=True, value=input_data_lancamento)

input_categoria_lancamento = st.selectbox(label="Categoria Lançamento", options=Categoria.listar_categorias(TipoLancamento.string_para_tipo_lancamento(input_tipo_lancamento)))
input_descricao = st.text_input(label='Insira a descrição do Lançamento')

button_submit = st.button(label="Enviar")