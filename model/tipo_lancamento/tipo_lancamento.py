from enum import Enum, auto

class TipoLancamento(Enum):
    RECEITA=auto()
    DESPESA=auto()
    TRANSFERENCIA=auto()
    # APORTE=auto()
    # RESGATE=auto()

    def string_para_tipo_lancamento(string):
        mapeamento = {
            "Receita": TipoLancamento.RECEITA,
            "Despesa": TipoLancamento.DESPESA,
            "Transferência Entre Contas": TipoLancamento.TRANSFERENCIA
        }
        return mapeamento[string]

    def tipo_lancamento_para_string(tipo_lancamento):
        mapeamento = {
            TipoLancamento.RECEITA: "Receita",
            TipoLancamento.DESPESA: "Despesa",
            TipoLancamento.TRANSFERENCIA: "Transferência Entre Contas"
        }
        return mapeamento[tipo_lancamento]
    
    @classmethod
    def listar_tipos(cls):
        return list(cls)
    
    @classmethod
    def listar_tipos_str(cls):
        tipos = [cls.tipo_lancamento_para_string(i) for i in cls.listar_tipos()]
        return tipos
