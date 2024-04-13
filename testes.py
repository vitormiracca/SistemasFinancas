from controler.conta_dao import ContaDAO
from controler.categoria_dao import CategoriaDAO
from controler.lancamento_dao import LancamentoDAO
from model.conta import Conta
from model.lancamento import Lancamento
from model.tipo_lancamento.categoria import Categoria
from model.tipo_lancamento.receita import Receita
from model.tipo_lancamento.tipo_lancamento import TipoLancamento

lancamento_dao = LancamentoDAO()
conta_dao = ContaDAO()
categoria_dao = CategoriaDAO()

# categorias_dict = {
#     TipoLancamento.RECEITA: ['Salário', 'Benefícios', 'Outros', 'Devedores', 'Rendimentos'],
#     TipoLancamento.DESPESA: ['Supermercado', 'Alimentação', 'Shopping', 'Estudo', 'Assinaturas Digitais', 'Tabacaria', 'Outros', 'Despesas Carro']
# }
# for k,v in categorias_dict.items():
#     for i in v:
#         categoria = Categoria(tp_lancamento=k, nome=i)
#         categoria_dao.criar_categoria(categoria=categoria)

# contas_dict = {
#     "Conta Corrente": ["Nubank", "Bradesco"],
#     "Conta de Crédito": [("Bradesco Cartões", 21, 15), ("Nu Crédito", 18, 11)],
#     "Conta Investimentos": ["Ágora"],
#     "Vale": ["Ticket"]
# }
# for k,v in contas_dict.items():
#     for i in v:
#         if isinstance(i, tuple):
#             conta = Conta(conta_nome=i[0], tipo_conta=k, data_vcto=i[1], data_fechamento=i[2])
#         else:
#             conta = Conta(conta_nome=i, tipo_conta=k)
#         conta_dao.criar_conta(conta=conta)

# lancamento_dao.criar_lancamento(Receita(data_lancamento='2023-01-01', valor=1950.99, categoria='Salário', conta='Nubank', descricao='Salário dia 01'))


# print(categoria_dao.listar_categorias())
# categorias = []
# for row in categoria_dao.listar_categorias():
#     categoria = Categoria(tp_lancamento=row[1],
#                         nome=row[2])
#     categorias.append(categoria)

# for i in categorias:
#     print(i.nome)

for i in Conta.listar_contas():
    print(i.conta_id)