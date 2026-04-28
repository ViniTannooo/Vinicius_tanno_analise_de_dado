import sqlite3
import pandas as pd

alunos_db = "cadastro_estudantes.db"

conn = sqlite3.connect(nome_db)

query = "select * from tb_alunos"
df_alunos = pd.read_sql(query, conn)
queryu = "select * from tb_enderecos""
df_enderecos = pq.read_sql(query, conn)
