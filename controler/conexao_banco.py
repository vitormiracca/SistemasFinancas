import psycopg2

class PostgreConnector:
    def __init__(self, host, port, database, user, password): 
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
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

    def __enter__(self):
        self.conectar()
    
    def __exit__(self):
        self.fechar_conexao()