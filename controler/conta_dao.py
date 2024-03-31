import pandas as pd
from controler.conexao_banco import ConexaoBanco

class ContaDAO:
    def __init__(self):
        self.conexao = ConexaoBanco()

    # Implemente métodos para atualizar, excluir e consultar contas
        
    def criar_conta(self, conta):
        self.conexao.conectar()

        try:
            query = "INSERT INTO contas (nome, tipo_conta) VALUES (%s, %s);"
            self.conexao.cursor.execute(query, (conta.conta_nome, conta.tipo_conta))
            # Commit para confirmar a transação no banco de dados
            self.conexao.conn.commit()
            print("Conta criada com sucesso!")
        except Exception as e:
            # Em caso de erro, fazer rollback para desfazer a transação
            self.conexao.conn.rollback()
            print("Erro ao criar conta:", e)
        finally:
            # Fechar a conexão após o uso
            self.conexao.fechar_conexao()

    def atualizar_conta(self, conta):
        self.conexao.conectar()

        try:
            query = "UPDATE conta SET nome = %s, tipo = %s WHERE id_conta = %s;"
            self.conexao.cursor.execute(query, (conta.nome, conta.tipo, conta.id_conta))
            self.conexao.conn.commit()
            print("Conta atualizada com sucesso!")
        except Exception as e:
            self.conexao.conn.rollback()
            print("Erro ao atualizar conta:", e)
        finally:
            self.conexao.fechar_conexao()

    def deletar_conta(self, id_conta):
        self.conexao.conectar()
        try:
            query = "DELETE FROM conta WHERE id_conta = %s;"
            self.conexao.cursor.execute(query, (id_conta,))
            self.conexao.conn.commit()
            print("Conta deletada com sucesso!")
        except Exception as e:
            self.conexao.conn.rollback()
            print("Erro ao deletar conta:", e)
        finally:
            self.conexao.fechar_conexao()

    def listar_contas(self):
        self.conexao.conectar()
        try:
            query = "SELECT * FROM conta;"
            self.conexao.cursor.execute(query)
            rows = self.conexao.cursor.fetchall()
            col_names = [desc[0] for desc in self.conexao.cursor.description]
            df = pd.DataFrame(rows, columns=col_names)
            return df

        except Exception as e:
            print("Erro ao listar contas:", e)
            return None
        
        finally:
            self.conexao.fechar_conexao()