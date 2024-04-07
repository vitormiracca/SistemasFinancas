import os
from dotenv import load_dotenv
import pandas as pd
from controler.conexao_banco import PostgreConnector

load_dotenv()
host = os.getenv('POSTGRE_HOST')
port = os.getenv('POSTGRE_PORT')
user = os.getenv('POSTGRE_USER')
password = os.getenv('POSTGRE_PASSWORD')
databse = os.getenv('POSTGRE_DBNAME')

class CategoriaDAO:
    def __init__(self):
        self.conexao = PostgreConnector(host=host, port=port, database=databse, user=user, password=password)

    def criar_categoria(self, categoria):
        self.conexao.conectar()

        try:
            query = "INSERT INTO categorias (tipo_lancamento, nome) VALUES (%s, %s);"
            self.conexao.cursor.execute(query, (categoria.tipo_lancamento, categoria.nome))
            # Commit para confirmar a transação no banco de dados
            self.conexao.conn.commit()
            print("Categoria criada com sucesso!")
        except Exception as e:
            # Em caso de erro, fazer rollback para desfazer a transação
            self.conexao.conn.rollback()
            print("Erro ao criar categoria:", e)
        finally:
            # Fechar a conexão após o uso
            self.conexao.fechar_conexao()

    def atualizar_conta(self, categoria):
        self.conexao.conectar()

        try:
            query = "UPDATE categorias SET nome = %s, tipo_lancamento = %s WHERE id = %s;"
            self.conexao.cursor.execute(query, (categoria.nome, categoria.tipo_lancamento, categoria.id_categoria))
            self.conexao.conn.commit()
            print("Categoria atualizada com sucesso!")
        except Exception as e:
            self.conexao.conn.rollback()
            print("Erro ao atualizar Categoria:", e)
        finally:
            self.conexao.fechar_conexao()

    def deletar_conta(self, id_categoria):
        self.conexao.conectar()
        try:
            query = "DELETE FROM categorias WHERE id_categoria = %s;"
            self.conexao.cursor.execute(query, (id_categoria,))
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
            query = "SELECT * FROM categorias;"
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