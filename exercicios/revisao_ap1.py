#-----------------------------------------------------------
# PYTHON BÁSICO
#-----------------------------------------------------------

# Listas e dicionários

# Lista []
# Dicionário {}

# Como pegar elementos de listas e dicionários
# Lista[0]
# Dicionário["Key"]

#-----------------------------------------------------------
# OBTER DADOS
#-----------------------------------------------------------

import pandas as pd

df = pd.read_csv("nome.csv")
df = pd.read_excel("nome.xlsx")

#-----------------------------------------------------------
# ORGANIZAR DADOS
#-----------------------------------------------------------

# Filtrar dados

filtro = (df[df["idade"] >= 10]) & (df["nome"].str.contains("a"))     # Retorna todas as linhas com idade >= 10 e que o nome que contenha a letra "a"

df_idade = df.loc[filtro, ["nome", "idade", "endereço"]]      # Me retorna um df com as três colunas indicadas e com as linhas após o filtro

filtro = df["nome"].str.contains("Pedro", case=False)     #Filtro que seleciona apenas os Pedros e não considera letra maiúscula/minúscula

#-----------------------------------------------------------

# Rankear dados

df["Roic"].rank(ascending=False)
df.sort_values(["Roic"], ascending=False)

#-----------------------------------------------------------

# Criar nova coluna

df["nova_col"] = 0

#-----------------------------------------------------------

# Calcular - min, max, media

df["nova_col"].min()

#-----------------------------------------------------------

# Agrupar dados

df.groupby("estado")["renda"].min()

#-----------------------------------------------------------
# APIs
#-----------------------------------------------------------

# Consumir APIs

import requests

URL = "https://..."

Response = requests.get(URL)

Response.status_code    # se retornou 200 é sucesso

dados = Response.json()

pd.DataFrame(dados)


