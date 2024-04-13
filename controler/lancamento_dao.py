import pandas as pd
from controler.conexao_banco import PostgreConnector

class LancamentoDAO:
    def __init__(self):
        self.conexao = PostgreConnector()

    # Implemente métodos para atualizar, excluir e consultar lancamentos
        
    def criar_lancamento(self, lancamento):
        self.conexao.conectar()

        try:
            query = "INSERT INTO lancamentos (data_lancamento, tipo_lancamento, valor, data_liquidacao, descricao, conta_id, categoria_id) VALUES (%s, %s, %s, %s, %s, %s, %s);"
            self.conexao.cursor.execute(query, (lancamento.data_lancamento, lancamento.tp_lancamento, lancamento.valor, lancamento.data_liquidacao,lancamento.descricao, lancamento.conta_id, lancamento.categoria_id))
            # Commit para confirmar a transação no banco de dados
            self.conexao.conn.commit()
            print("lancamento criada com sucesso!")
        except Exception as e:
            # Em caso de erro, fazer rollback para desfazer a transação
            self.conexao.conn.rollback()
            print("Erro ao criar lancamento:", e)
        finally:
            # Fechar a conexão após o uso
            self.conexao.fechar_conexao()

    def atualizar_lancamento(self, lancamento):
        self.conexao.conectar()

        try:
            query = "UPDATE lancamentos SET data_lancamento = %s, tipo_lancamento = %s, valor = %s, data_liquidacao = %s, descricao = %s, conta_id = %s WHERE id = %s;"
            self.conexao.cursor.execute(query, (lancamento.data_lancamento, lancamento.tp_lancamento, lancamento.valor, lancamento.data_liquidacao,lancamento.descricao, lancamento.conta_id, lancamento.id_lancamento))
            self.conexao.conn.commit()
            print("lancamento atualizada com sucesso!")
        except Exception as e:
            self.conexao.conn.rollback()
            print("Erro ao atualizar lancamento:", e)
        finally:
            self.conexao.fechar_conexao()

    def deletar_lancamento(self, id_lancamento):
        self.conexao.conectar()
        try:
            query = "DELETE FROM lancamentos WHERE id = %s;"
            self.conexao.cursor.execute(query, (id_lancamento,))
            self.conexao.conn.commit()
            print("lancamento deletada com sucesso!")
        except Exception as e:
            self.conexao.conn.rollback()
            print("Erro ao deletar lancamento:", e)
        finally:
            self.conexao.fechar_conexao()

    def listar_lancamentos(self):
        self.conexao.conectar()
        try:
            query = "SELECT * FROM lancamentos;"
            self.conexao.cursor.execute(query)
            rows = self.conexao.cursor.fetchall()
            col_names = [desc[0] for desc in self.conexao.cursor.description]
            df = pd.DataFrame(rows, columns=col_names)
            return df

        except Exception as e:
            print("Erro ao listar lancamentos:", e)
            return None
        
        finally:
            self.conexao.fechar_conexao()