
from model.lancamento import Lancamento


class Conta:
    def __init__(self, banco:str, saldo:float=0):
        self._banco = banco
        self._saldo = saldo
        self.lancamentos = []
#region Getter e Setters
    @property
    def banco(self):
        return self._banco.title()
    @banco.setter
    def banco(self,banco:str):
        self._banco = banco

    @property
    def saldo(self):
        return self._saldo.title()
    @saldo.setter
    def saldo(self,saldo:float):
        self._saldo = saldo
#endregion

    def adicionar_lancamentos(self, lancamentos:list[Lancamento]):
        for l in lancamentos:
            self.lancamentos.append(l)

    def gera_extrato(self):
        print('#####################')
        print(f'EXTRATO: {self.banco}')
        print('#####################\n')
        for l in self.lancamentos:
            print(l)

