from controler.conta_dao import ContaDAO
from model.conta import Conta

nu_conta = Conta("Nubank", "Conta Corrente")

conta_dao = ContaDAO()
conta_dao.criar_conta(nu_conta)