import os
from dotenv import load_dotenv
import pandas as pd
from controler.conexao_banco import PostgreConnector

class ContaDAO:
    def __init__(self):
        self.conexao = PostgreConnector()

    # Implemente métodos para atualizar, excluir e consultar contas
        
    def criar_conta(self, conta):
        self.conexao.conectar()

        try:
            query = "INSERT INTO contas (nome, tipo_conta, dia_vcto, dia_fechamento) VALUES (%s, %s, %s, %s);"
            self.conexao.cursor.execute(query, (conta.conta_nome, conta.tipo_conta, conta.dia_vcto, conta.dia_fechamento))
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
            query = "UPDATE contas SET nome = %s, tipo_conta = %s, dia_vcto = %s, dia_fechamento = %s  WHERE id_conta = %s;"
            self.conexao.cursor.execute(query, (conta.nome, conta.tipo_conta, conta.dia_vcto, conta.dia_fechamento, conta.id_conta))
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
            query = "DELETE FROM contas WHERE id_conta = %s;"
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
            query = "SELECT * FROM contas;"
            self.conexao.cursor.execute(query)
            rows = self.conexao.cursor.fetchall()
            return rows

        except Exception as e:
            print("Erro ao listar contas:", e)
            return None
        
        finally:
            self.conexao.fechar_conexao()