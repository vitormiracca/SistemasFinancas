from controler.conta_dao import ContaDAO
from controler.categoria_dao import CategoriaDAO
from model.conta import Conta
from model.tipo_lancamento.categoria import Categoria
from model.tipo_lancamento.tipo_lancamento import TipoLancamento

# nu_conta = Conta("Nubank", "Conta Corrente")

# conta_dao = ContaDAO()
# categoria_dao = CategoriaDAO()
# conta_dao.criar_conta(nu_conta)

# categoria_receita = ['Salário', 'Benefícios', 'Outros', 'Devedores', 'Rendimentos']
# categoria_despesa = ['Supermercado', 'Alimentação', 'Shopping', 'Estudo', 'Assinaturas Digitais', 'Tabacaria', 'Outros', 'Despesas Carro']
# for i in categoria_receita:
#     categoria_dao.criar_categoria(Categoria(TipoLancamento.RECEITA, i))
# for i in categoria_despesa:
#     categoria_dao.criar_categoria(Categoria(TipoLancamento.DESPESA, i))

contaDAO = ContaDAO()
categoriaDAO = CategoriaDAO()

df = categoriaDAO.listar_contas()
print(df)

