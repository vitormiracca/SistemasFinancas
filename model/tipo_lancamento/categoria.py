from model.tipo_lancamento.tipo_lancamento import TipoLancamento
from controler.categoria_dao import CategoriaDAO

class Categoria:
    def __init__(self, tp_lancamento:TipoLancamento, nome: str, categoria_id:int = None):
        self._tp_lancamento = tp_lancamento
        self._nome = nome
        self._categoria_id = categoria_id
    #     self._categorias[tp_lancamento].add(nome)

    # _categorias = {
    #     TipoLancamento.RECEITA : set(),
    #     TipoLancamento.DESPESA : set(),
    #     TipoLancamento.TRANSFERENCIA : set(),
    # }
    dao = CategoriaDAO()

    @property
    def nome(self):
        return self._nome.title()
    @nome.setter
    def nome (self, nome:str):
        self._nome = nome

    @property
    def tp_lancamento(self):
        return self._tp_lancamento
    
    @property
    def tipo_lancamento(self):
        return TipoLancamento.tipo_lancamento_para_string(self._tp_lancamento)

    @property
    def categoria_id(self):
        return self._categoria_id
    @categoria_id.setter
    def categoria_id(self, categoria_id):
        self._categoria_id = categoria_id
    
    @classmethod
    def listar_categorias(cls):
        rows = cls.dao.listar_categorias()
        categorias_list = []
        for row in rows:
            categoria = Categoria(tp_lancamento=row[1],
                                nome=row[2],
                                categoria_id=row[0])
            categorias_list.append(categoria)
        return categorias_list
        # if (tipo_lancamento):
        #     return cls._categorias[tipo_lancamento]
        # else:
        #     return set.union(*cls._categorias.values())

    @classmethod
    def listar_categorias_por_tipo(cls, tipo_lancamento=None):
        lista = [i for i in cls.listar_categorias() if i.tp_lancamento == tipo_lancamento]
        return lista

    @classmethod
    def enum_tp_lancamento(cls):
        return TipoLancamento