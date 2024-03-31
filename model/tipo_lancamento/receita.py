from datetime import date
from model.tipo_lancamento.categoria import Categoria
from model.tipo_lancamento.tipo_lancamento import TipoLancamento
from model.conta import Conta
from model.lancamento import Lancamento


class Receita(Lancamento):
    def __init__(self, data_lancamento:date, valor:float, categoria:Categoria, conta:Conta, descricao:str=''):
        super().__init__(data_lancamento, TipoLancamento.RECEITA, valor, conta, descricao)
        self._categoria = categoria

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