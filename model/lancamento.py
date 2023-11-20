from datetime import date
from model.conta import Conta

class Lancamento:
    def __init__(self, valor:float, data_lancamento:date, data_liquidacao:date, conta:Conta, descricao:str = '', tp_lancamento:str=''):
        self._valor = valor
        self._data_lancamento = data_lancamento
        self._data_liquidacao = data_liquidacao
        self._conta = conta
        self._descricao = descricao
        self._tp_lancamento = tp_lancamento

    #region Getter e Setter
    @property
    def valor(self):
        return self._valor
    @valor.setter
    def valor(self, valor:float):
        self._valor = valor

    @property
    def data_lancamento(self):
        return self._data_lancamento
    @data_lancamento.setter
    def data_lancamento(self, data_lancamento):
        self._data_lancamento = data_lancamento

    @property
    def data_liquidacao(self):
        return self._data_lancamento
    @data_liquidacao.setter
    def data_liquidacao(self, data_liquidacao):
        self._data_liquidacao = data_liquidacao

    @property
    def conta(self):
        return self._conta
    @conta.setter
    def conta(self, conta):
        self._conta = conta

    @property
    def descricao(self):
        return self._descricao
    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao

    @property
    def tp_lancamento(self):
        return self._tp_lancamento
    @tp_lancamento.setter
    def tp_lancamento(self, tp_lancamento):
        self._tp_lancamento = tp_lancamento
    #endregion
    
 
