from datetime import date
from model.conta import Conta
from model.tipo_lancamento.categoria import Categoria
from model.tipo_lancamento.tipo_lancamento import TipoLancamento

class Lancamento:
    def __init__(self, data_lancamento:date, tp_lancamento:TipoLancamento, valor:float, conta:Conta, categoria:Categoria, descricao:str =''):
        self._data_lancamento = data_lancamento
        self._tp_lancamento = tp_lancamento
        self._valor = valor
        self._conta = conta
        self._data_liquidacao = data_lancamento
        self._descricao = descricao
        self.categoria = categoria
        self._conta.adicionar_lancamento(lancamento=self)

    #region Getter e Setter

    @property
    def data_lancamento(self):
        return self._data_lancamento
    @data_lancamento.setter
    def data_lancamento(self, data_lancamento):
        self._data_lancamento = data_lancamento

    @property
    def tp_lancamento(self):
        return self._tp_lancamento
    @tp_lancamento.setter
    def tp_lancamento(self, tp_lancamento):
        self._tp_lancamento = tp_lancamento

    @property
    def valor(self):
        return self._valor
    @valor.setter
    def valor(self, valor:float):
        self._valor = valor

    @property
    def conta(self):
        return self._conta
    @conta.setter
    def conta(self, conta:Conta):
        self._conta = conta

    @property
    def conta_id(self):
        return self._conta.conta_id

    @property
    def categoria_id(self):
        return self.categoria.categoria_id

    @property
    def data_liquidacao(self):
        return self._data_lancamento
    @data_liquidacao.setter
    def data_liquidacao(self, data_liquidacao):
        self._data_liquidacao = data_liquidacao

    @property
    def descricao(self):
        return self._descricao
    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao

    #endregion
    
    def __str__(self) -> str:
        return f"""
- Data: {self.data_lancamento}
- {self.tp_lancamento.upper()} ==> {self.valor}
        """
 
