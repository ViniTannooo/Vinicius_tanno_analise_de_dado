import sqlite3
import pandas as pd

# Banco de Dados SQLite
alunos_db = "cadastro_estudantes.db"

# Conexão com o banco
conn = sqlite3.connect(alunos_db)

# Consulta da tabela de alunos
query_alunos = "select * from tb_alunos"
df_alunos = pd.read_sql(query_alunos, conn)

# Consulta da tabela de endereços
query_enderecos = "select * from tb_enderecos"
df_enderecos = pd.read_sql(query_enderecos, conn)

# merge entre tb_alunos e tb_enderecos
df = pd.merge(df_alunos, df_enderecos, left_on="endereco_id", right_on="id", how="inner")
