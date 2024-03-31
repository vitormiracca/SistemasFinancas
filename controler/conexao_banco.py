from dotenv import load_dotenv
import os
import psycopg2

class ConexaoBanco:
    def __init__(self):
        load_dotenv()  
        self.host = os.getenv("POSTGRE_HOST")
        self.port = os.getenv("POSTGRE_PORT")
        self.database = os.getenv("POSTGRE_DBNAME")
        self.user = os.getenv("POSTGRE_USER")
        self.password = os.getenv("POSTGRE_PASSWORD")
        self.conn = None
        self.cursor = None

    def conectar(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.cursor = self.conn.cursor()
            print("Conexão ao banco de dados estabelecida com sucesso!")
        except (Exception, psycopg2.Error) as error:
            print("Erro ao conectar ao banco de dados:", error)

    def fechar_conexao(self):
        if self.conn:
            self.cursor.close()
            self.conn.close()
            print("Conexão ao banco de dados fechada.")