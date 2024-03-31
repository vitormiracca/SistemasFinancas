from model.tipo_lancamento.tipo_lancamento import TipoLancamento

class Categoria:
    def __init__(self, tp_lancamento:TipoLancamento, nome: str):
        self._tp_lancamento = tp_lancamento
        self._nome = nome
        self._categorias[tp_lancamento].add(nome)

    _categorias = {
        TipoLancamento.RECEITA : set(),
        TipoLancamento.DESPESA : set(),
    }

    @property
    def nome(self):
        return self._nome.title()
    @nome.setter
    def nome (self, nome:str):
        self._nome = nome

    @property
    def tp_lancamento(self):
        return self._tp_lancamento
    
    @classmethod
    def listar_categorias(cls, tipo_lancamento=None):
        if (tipo_lancamento):
            return cls._categorias[tipo_lancamento]
        else:
            return set.union(*cls._categorias.values())

    @classmethod
    def enum_tp_lancamento(cls):
        return TipoLancamento