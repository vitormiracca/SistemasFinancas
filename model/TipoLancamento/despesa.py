from datetime import date
from model.TipoLancamento.categoria import Categoria
from model.TipoLancamento.tp_lancamento import TipoLancamento
from model.conta import Conta
from model.lancamento import Lancamento

class Despesa(Lancamento):
    def __init__(self, valor:float, data_lancamento:date, data_liquidacao:date, conta:Conta, categoria:str, descricao:str = ''):
        super().__init__(valor, data_lancamento, data_liquidacao, conta, TipoLancamento.DESPESA, descricao)
        self.categoria = categoria

    _categorias = {}

    @classmethod
    def listar_categorias(self):
        self._categorias = Categoria.listar_categorias(self.tp_lancamento)

    #region Getter e Setters
    @property
    def categoria(self):
        return self._categoria.title()
    @categoria.setter
    def categoria(self,categoria:str):
        self._categoria = categoria
    #endregion

    def __str__(self) -> str:
        return f"""
- Data: {self.data_lancamento}
- {self.tp_lancamento.name} ==> {self.valor}
- Categoria: {self.categoria}
- Descrição: {self.descricao}
        """