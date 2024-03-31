from enum import Enum, auto

class TipoLancamento(Enum):
    RECEITA=auto()
    DESPESA=auto()
    TRANSFERENCIA=auto()
    # APORTE=auto()
    # RESGATE=auto()