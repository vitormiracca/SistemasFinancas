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
            "Transferência": TipoLancamento.TRANSFERENCIA
        }
        return mapeamento[string]

    def tipo_lancamento_para_string(tipo_lancamento):
        mapeamento = {
            TipoLancamento.RECEITA: "Receita",
            TipoLancamento.DESPESA: "Despesa",
            TipoLancamento.TRANSFERENCIA: "Transferência"
        }
        return mapeamento[tipo_lancamento]