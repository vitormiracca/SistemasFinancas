class Conta:
    def __init__(self, conta_nome:str, tipo_conta:str):      #saldo:float=0
        self._conta_nome = conta_nome
        self._tipo_conta = tipo_conta
        self.lancamentos = []

#region Getter e Setters
    @property
    def conta_nome(self):
        return self._conta_nome.title()
    @conta_nome.setter
    def conta_nome(self,conta_nome:str):
        self._conta_nome = conta_nome

    @property
    def tipo_conta(self):
        return self._tipo_conta.title()
    @tipo_conta.setter
    def tipo_conta(self,tipo_conta:str):
        self._tipo_conta = tipo_conta
#endregion

    def adicionar_lancamento(self, lancamento):
        self.lancamentos.append(lancamento)

    def adicionar_lancamentos_lista(self, lancamentos:list):
        for l in lancamentos:
            self.lancamentos.append(l)

    def gera_extrato(self):
        print('#####################')
        print(f'EXTRATO: {self.conta_nome}')
        print('#####################\n')
        for l in self.lancamentos:
            print(l)


    def gera_balanco(self):
        balanco_final = sum(lancamento.valor for lancamento in self.lancamentos)
        print('##################')
        print(f'BALANÇO: {self.conta_nome}')
        print(balanco_final)
        print('##################')