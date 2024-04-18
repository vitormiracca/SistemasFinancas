import pandas as pd
from controler.conexao_banco import PostgreConnector

class AnalyticsDAO:
    def __init__(self):
        self.conexao = PostgreConnector()

    def df_lancamentos(self):
        self.conexao.conectar()
        try:
            query = """
                SELECT 
                    l.data_lancamento,
                    l.tipo_lancamento,
                    l.valor,
                    co.nome                 as conta, 
                    co.tipo_conta,
                    ca.nome                 as categoria,
                    co.dia_vcto,
                    co.dia_fechamento,
                    ca.nome,
                    l.descricao,
                    l.data_liquidacao
                FROM lancamentos l
                JOIN contas co
                    ON l.conta_id = co.id
                JOIN categorias ca
                    ON l.categoria_id = ca.id
                ORDER BY data_lancamento DESC;
            """
            self.conexao.cursor.execute(query)
            rows = self.conexao.cursor.fetchall()
            col_names = [desc[0] for desc in self.conexao.cursor.description]
            df = pd.DataFrame(rows, columns=col_names)
            return df

        except Exception as e:
            print("Erro ao listar lancamentos:", e)
            return None
        
        finally:
            self.conexao.fechar_conexao