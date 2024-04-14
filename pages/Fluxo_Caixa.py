# carregando as bibliotecas
import streamlit as st

from controler.lancamento_dao import LancamentoDAO
from model import lancamento
from model.conta import Conta
from model.lancamento import Lancamento
from model.tipo_lancamento.categoria import Categoria
from model.tipo_lancamento.despesa import Despesa
from model.tipo_lancamento.receita import Receita
from model.tipo_lancamento.tipo_lancamento import TipoLancamento

#region Preparando ambiente para teste
lancamento_dao = LancamentoDAO()

contas = Conta.listar_contas()
tipos_lancamentos_str = TipoLancamento.listar_tipos_str()

#endregion

st.set_page_config(page_title="Fluxo_Caixa", page_icon="📈")
st.title('Inserir Lançamento')
st.sidebar.success("Registre seus Lançamentos.")

### Formulário ###
input_tipo_lancamento = st.radio("Tipo de Lançamento", tipos_lancamentos_str, horizontal=True, )

col1, col2 = st.columns([1, 1])
with col1:
    input_data_lancamento = st.date_input(label='Data do Lançamento', format="DD/MM/YYYY")
    input_conta = st.selectbox(label='Conta Usada',
                                options=contas, 
                                format_func= lambda conta: conta.conta_nome)
with col2:
    input_valor_lancamento = st.number_input(label='Valor do Lançamento', step=0.01)
    st.date_input(label="Data do Débito", format="DD/MM/YYYY", disabled=True, value=input_data_lancamento)

categorias = Categoria.listar_categorias_por_tipo(input_tipo_lancamento)
input_categoria_lancamento = st.selectbox(label="Categoria Lançamento", options=categorias, format_func= lambda cat: cat.nome)
input_descricao = st.text_input(label='Insira a descrição do Lançamento')

button_submit = st.button(label="Enviar")

if button_submit:
    lancamento = Lancamento(
        data_lancamento=input_data_lancamento,
        tp_lancamento=input_tipo_lancamento,
        valor=input_valor_lancamento,
        conta=input_conta,
        descricao=input_descricao,
        categoria=input_categoria_lancamento
        )
    lancamento_dao.criar_lancamento(lancamento)

df_lancamentos = lancamento_dao.listar_lancamentos()
st.dataframe(df_lancamentos.sort_values(by='data_lancamento', ascending=False))