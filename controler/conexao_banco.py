import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
host = os.getenv('POSTGRE_HOST')
port = os.getenv('POSTGRE_PORT')
user = os.getenv('POSTGRE_USER')
password = os.getenv('POSTGRE_PASSWORD')
database = os.getenv('POSTGRE_DBNAME')

class PostgreConnector:
    def __init__(self): 
        self._host = host
        self._port = port
        self._database = database
        self._user = user
        self._password = password
        self.conn = None
        self.cursor = None

    def conectar(self):
        try:
            self.conn = psycopg2.connect(
                host=self._host,
                port=self._port,
                database=self._database,
                user=self._user,
                password=self._password
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

    def __enter__(self):
        self.conectar()
    
    def __exit__(self):
        self.fechar_conexao()