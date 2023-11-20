from model.TipoLancamento.categoria import Categoria
from model.TipoLancamento.tp_lancamento import TipoLancamento
from model.conta import Conta
from model.TipoLancamento.receita import Receita
from model.TipoLancamento.despesa import Despesa

# Adiciona categorias
categoria_receita = ['Salário', 'Benefícios', 'Outros', 'Devedores', 'Rendimentos']
categoria_despesa = ['Supermercado', 'Alimentação', 'Shopping', 'Estudo', 'Assinaturas Digitais', 'Tabacaria', 'Outros']

for i in categoria_receita:
    Categoria(TipoLancamento.RECEITA, i)
for i in categoria_despesa:
    Categoria(TipoLancamento.DESPESA, i)

# Lista as categorias para cada tipo de lançamento
enum_tipo_lancamento = Categoria.enum_tp_lancamento()
for tipo in enum_tipo_lancamento:
    print(f"Categorias para {tipo.name}: {Categoria.listar_categorias(tipo)}")
    print()


# Criar contas 
conta_nu = Conta('Nubank', 2500)
conta_bra = Conta('Bradesco', 15.50)
conta_ticket = Conta('Ticket', 10.60)

# Criar lançamentos
receita1 = Receita(2850.50, '2023-11-01', '2023-11-01', conta_nu, 'Salário')
receita2 = Receita(1500, '2023-11-15', '2023-11-15', conta_nu, 'Salário')
receita3 = Receita(650.45, '2023-11-01', '2023-11-01', conta_ticket, 'Benefícios')

despesa1 = Despesa(170, '2023-11-10', '2023-11-10', conta_nu, 'Shopping')
despesa2 = Despesa(47.99, '2023-11-10', '2023-11-10', conta_ticket, 'Alimentação')
despesa3 = Despesa(17, '2023-11-10', '2023-11-10', conta_ticket, 'Supermercado')
despesa4 = Despesa(32.20, '2023-11-10', '2023-11-10', conta_nu, 'Tabacaria')
despesa5 = Despesa(41, '2023-11-10', '2023-11-10', conta_nu, 'Estudo')


# Realizar os lançamentos nas contas
conta_nu.adicionar_lancamentos([receita1, receita2, despesa5, despesa4, despesa1])
conta_ticket.adicionar_lancamentos([receita3, despesa2, despesa3])

conta_nu.gera_extrato()
print()
print()
conta_ticket.gera_extrato()