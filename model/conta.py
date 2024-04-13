from controler.conta_dao import ContaDAO

class Conta:
    def __init__(self, conta_nome:str, tipo_conta:str,  data_vcto = None, data_fechamento = None, conta_id=None):
        self._conta_nome = conta_nome
        self._tipo_conta = tipo_conta
        self._dia_vcto = data_vcto
        self._dia_fechamento = data_fechamento
        self._conta_id = conta_id
        self.lancamentos = []
        
        # self.contas_existentes.append(self)

    # contas_existentes = []
    dao = ContaDAO()

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

    @property
    def dia_vcto(self):
        return self._dia_vcto
    @dia_vcto.setter
    def dia_vcto(self,dia_vcto:str):
        self._dia_vcto = dia_vcto

    @property
    def dia_fechamento(self):
        return self._dia_fechamento
    @dia_fechamento.setter
    def dia_fechamento(self,dia_fechamento:str):
        self._dia_fechamento = dia_fechamento

    @property
    def conta_id(self):
        return self._conta_id
    @conta_id.setter
    def conta_id(self,conta_id:int):
        self._conta_id = conta_id    

#endregion
        
    @classmethod
    def listar_contas(cls):
        contas_list = []
        for row in cls.dao.listar_contas():
            conta = Conta(conta_nome=row[1],
                            tipo_conta=row[2],
                            data_vcto=row[3],
                            data_fechamento=row[4],
                            conta_id=row[0])
            contas_list.append(conta) 
        return contas_list
        # return [c.conta_nome for c in cls.contas_existentes]

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