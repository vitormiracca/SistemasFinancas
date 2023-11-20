from datetime import date
from model.conta import Conta
from model.lancamento import Lancamento

class Despesa(Lancamento):
    def __init__(self, valor:float, data_lancamento:date, data_liquidacao:date, conta:Conta, descricao:str, categoria:str):
        super().__init__(valor, data_lancamento, data_liquidacao, conta, descricao, 'Despesa')
        self.categoria = categoria

    #region Getter e Setters
    @property
    def categoria(self):
        return self._categoria.title()
    @categoria.setter
    def categoria(self,categoria:str):
        self._categoria = categoria
    #endregion
