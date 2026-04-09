"""
Aula - Exercicios de Pandas DataFrame
Como usar:
1) Leia o enunciado de cada bloco.
2) Complete o codigo onde estiver RESOLUCAO.
3) Rode o arquivo e valide os resultados.

Requisito:
- Instalar pandas: pip install pandas

Regra da aula:
- Pense no DataFrame como uma planilha.
- Resolva um exercicio por vez.
"""
# -------------------------------------------------
# BLOCO 1: criar DataFrame e inspecionar estrutura
# -------------------------------------------------
import pandas as pd
dados_vendas = {
    "mes": ["Jan", "Jan", "Fev", "Fev", "Mar", "Mar"],
    "filial": ["Centro", "Norte", "Centro", "Norte", "Centro", "Norte"],
    "vendas": [12000, 9500, 13500, 10200, 14100, 11000],
    "clientes": [210, 180, 225, 190, 235, 205],
}

# Exercicio 1:
# a) Crie o DataFrame df_vendas usando dados_vendas
df_vendas = pd.DataFrame(dados_vendas)

# b) Mostre as 5 primeiras linhas
df_vendas.head()

# c) Mostre o formato (linhas, colunas)
df_vendas.shape

# d) Mostre os tipos de dados das colunas
df_vendas.dtypes


# -------------------------------------------------
# BLOCO 2: selecionar colunas e linhas
# -------------------------------------------------

# Exercicio 2:

# a) Mostre apenas as colunas "mes" e "vendas"
df_vendas[["mes", "vendas"]]

# b) Mostre somente a primeira linha
df_vendas.iloc[0]

# c) Mostre as linhas de indice 2 ate 4
df_vendas.iloc[2:5]


# -------------------------------------------------
# BLOCO 3: filtros com condicoes de negocio
# -------------------------------------------------

# Exercicio 3:

# a) Filtre vendas acima de 12000
df_vendas[df_vendas['vendas']>12000]

# b) Filtre apenas a filial "Centro"
df_vendas[df_vendas["filial"]=="Centro"]

# c) Filtre vendas acima de 11000 na filial "Norte"
df_vendas[(df_vendas["filial"]=="Norte") & (df_vendas["vendas"]>11000)]


# -------------------------------------------------
# BLOCO 4: novas colunas e metricas
# -------------------------------------------------

# Exercicio 4:

# a) Crie a coluna "ticket_medio" = vendas / clientes
df_vendas["ticket médio"] = df_vendas["vendas"]/df_vendas["clientes"]

# b) Crie a coluna "meta_batida" com True para vendas >= 13000
df_vendas["meta batida"] = df_vendas["vendas"]>=13000

# c) Mostre apenas "filial", "mes", "ticket_medio", "meta_batida"
df_vendas[['filial', 'mes', 'ticket_medio', 'meta_batida']]


# -------------------------------------------------
# BLOCO 5: agregacao com groupby
# -------------------------------------------------

# Exercicio 5:

# a) Calcule total de vendas por filial
vendas_filial = df_vendas.groupby("filial")["vendas"].sum()
vendas_filial

# b) Calcule media de clientes por mes
df_vendas.groupby("mes")["clientes"].mean()

# c) Descubra a filial com maior total de vendas
vendas_filial.idxmax()


# -------------------------------------------------
# BLOCO 6: ordenacao e ranking
# -------------------------------------------------

# Exercicio 6:

# a) Ordene df_vendas por "vendas" em ordem decrescente
df_vendas_decrescente = df_vendas.sort_values(by='vendas', ascending=False)

# b) Pegue os 3 maiores resultados de vendas
df_vendas_decrescente[0:3]

# c) Mostre um ranking com "filial", "mes", "vendas"
df_vendas_decrescente[['filial', 'mes', 'vendas']]


# -------------------------------------------------
# BLOCO 7: desafio final de analise
# -------------------------------------------------

# Exercicio 7 (desafio):

# 1) Gere um resumo por filial com:
#    - total_vendas
#    - media_ticket_medio
#    - total_clientes
resumo_filial = df_vendas.groupby("filial").agg({
    "vendas": "sum",
    "ticket médio": "mean",
    "clientes": "sum"
}).rename(columns={
    "vendas": "total_vendas", 
    "ticket médio": "media_ticket_medio", 
    "clientes": "total_clientes"
})
resumo_filial

# 2) Ordene o resumo por total_vendas (desc)
resumo_filial.sort_values(by="total_vendas", ascending=False)

# 3) Exiba qual filial teve melhor desempenho geral
melhor_filial = resumo_filial.index[0]
melhor_filial


# ===========================================================
# PARTE 1 – Estrutura lista + dicionário
# ===========================================================

dados_list_dict = [{
    "Column A":[1, 2, 3],
    "Column B":[4, 5, 6],
    "Column C":[7, 8, 9]
}]


# -----------------------------------------------------------
# EXERCÍCIO 1 – Explorando a estrutura
# -----------------------------------------------------------

# 1. Qual é o tipo de dados_list_dict?
type(dados_list_dict)

# 2. Qual é o tipo do primeiro elemento?
type(dados_list_dict[0])

# 3. Como acessar a lista da "Column A"?
dados_list_dict[0]["Column A"]

# 4. Como acessar o segundo elemento da "Column C"?
dados_list_dict[0]["Column C"][1]


# -----------------------------------------------------------
# EXERCÍCIO 2 – Convertendo para DataFrame
# -----------------------------------------------------------

# 1. Converta dados_list_dict[0] em um DataFrame chamado df1
import pandas as pd

df_dados = pd.DataFrame(dados_list_dict[0])
df_dados

# 2. Mostre:

#    - shape
df_dados.shape

#    - tipos das colunas
df_dados.dtypes

# 3. Calcule:
#    - soma de cada coluna
df_dados.sum()

#    - média de cada coluna
df_dados.mean()


# -----------------------------------------------------------
# EXERCÍCIO 3 – Criando novas colunas
# -----------------------------------------------------------

# No df1:
# 1. Crie coluna "Total" = soma das colunas
df_dados["Total"] = df_dados.sum(axis=1)
df_dados

# 2. Crie coluna "Media" = média por linha
df_dados["Média"] = df_dados.mean(axis=1)
df_dados

# 3. Filtre linhas onde Total > 10
df_dados[df_dados["Total"]<=10]


# -----------------------------------------------------------
# EXERCÍCIO 4 – Conversões estruturais
# -----------------------------------------------------------

# 1. Converta df1 para:
#    - lista de dicionários [ {linha1}, {linha2}, {linha3} ]
dicionarios = df_dados.to_dict(orient="records")
dicionarios

#    - dicionário de listas { coluna1: [valores], coluna2: [valores] }
lista = df_dados.to_dict(orient="list")
lista

# Dica:
# orient="records":
#   Cada elemento representa uma linha.
#   Estrutura ideal para APIs e JSON.

# orient="list":
#   Cada chave representa uma coluna.
#   Estrutura colunar, útil para reconstruir DataFrame.


# RESOLVA AQUI:


# -----------------------------------------------------------
# EXERCÍCIO 5 – Trabalhando com lista
# -----------------------------------------------------------

# 1. Transforme a coluna "Column A" em uma lista chamada lista_a.
lista_a = df_dados["Column A"].to_list()
lista_a

# 2. Multiplique cada elemento da lista por 10.
lista_a_10 = []
for num in lista_a:
    num = num*10
    lista_a_10.append(num)
lista_a_10

# 3. Crie uma nova coluna chamada "Column A x10" com essa nova lista.
df_dados["Column A x10"] = lista_a_10
df_dados


# ===========================================================
# BASE DE DADOS
# ===========================================================
import pandas as pd
dados = [
    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-01", "valor": 5000},

    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 102, "descricao": "Produto B",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-01", "valor": 3000},

    {"id_pais": 1, "nome_pais": "Argentina", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-02", "valor": 4000},

    {"id_pais": 1, "nome_pais": "Argentina", "id_produto": 102, "descricao": "Produto B",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-02", "valor": 6000},

    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-03", "valor": 7000},
]


# ===========================================================
# PARTE 1 – EXPLORAÇÃO INICIAL
# ===========================================================

# Exercício 1
# 1. Qual o tipo da variável dados?
type(dados)

# 2. Quantos registros existem?
len(dados)

# 3. Quais são as chaves do primeiro dicionário?
list(dados[0].keys())

# 4. Liste todos os países existentes (sem repetição).
paises = []
for dado in dados:
    if dado["nome_pais"] not in paises:
        paises.append(dado["nome_pais"])
paises


# ===========================================================
# PARTE 2 – CONVERSÃO PARA DATAFRAME
# ===========================================================

# Exercício 2
# 1. Converta dados para DataFrame chamado df
df = pd.DataFrame(dados)

# 2. Mostre shape, tipos e primeiras linhas
df.shape
df.dtypes
df.head()

# 3. Converta a coluna periodo para datetime
pd.to_datetime(df["periodo"])
df


# ===========================================================
# PARTE 3 – FILTROS E ORDENAÇÃO
# ===========================================================

# Exercício 3 – Filtros

# 1. Filtre apenas Brasil
df[df["nome_pais"] == "Brasil"]

# 2. Filtre apenas Produto A
df[df["descricao"] == "Produto A"]

# 3. Filtre valor > 4000
df[df["valor"] > 4000]

# 4. Combine Brasil + Produto A
df[(df["nome_pais"] == "Brasil") & (df["descricao"] == "Produto A")]


# Exercício 4 – Ordenação

# 1. Ordene por valor crescente
df.sort_values(by="valor", ascending=True)

# 2. Ordene por valor decrescente
df.sort_values(by="valor", ascending=False)

# 3. Ordene por periodo e depois por valor
df.sort_values(by=["periodo", "valor"], ascending=[True, True])


# ===========================================================
# PARTE 4 – AGREGAÇÕES
# ===========================================================

# Exercício 5 – GroupBy Simples

# 1. Total exportado por país
df.groupby("nome_pais")["valor"].sum()

# 2. Total exportado por produto
df.groupby("id_produto")["valor"].sum()

# 3. Média por país
df.groupby("nome_pais")["valor"].mean()

# 4. Quantidade de operações por país
df.groupby("nome_pais").size()


# Exercício 6 – GroupBy Múltiplo

# Agrupe por nome_pais e descricao
# Calcule soma, média e contagem
df.groupby(["nome_pais", "descricao"])["valor"].agg(["sum", "mean", "count"])

# Explique em comentário o que essa tabela representa


# ===========================================================
# PARTE 5 – PIVOT TABLE
# ===========================================================

# Exercício 7 – Pivot por Produto
# Linhas: periodo
# Colunas: descricao
# Valores: soma de valor
pivot_produto = df.pivot_table(index='periodo', columns='descricao', values='valor', aggfunc='sum')
pivot_produto

# Responda:
# 1. Qual produto vendeu mais?
# 2. Qual mês teve maior valor total?
# 3. Existe mês sem venda?

# RESOLVA AQUI:
df['ano'] = df['periodo'].dt.year
df['mes'] = df['periodo'].dt.month
df['valor_mil'] = df['valor'] / 1000

# Exercício 8 – Pivot por País
# Linhas: periodo
# Colunas: nome_pais
# Valores: soma de valor

# Explique o que podemos interpretar dessa tabela

# RESOLVA AQUI:
pais = df.pivot_table(index="periodo", columns="nome_pais", values="valor", aggfunc="sum")
pais


# ===========================================================
# PARTE 6 – FEATURE ENGINEERING
# ===========================================================

# Exercício 9
# 1. Extraia ano e mês da coluna periodo
# 2. Crie coluna valor_mil (valor / 1000)
# 3. Calcule crescimento percentual por produto mês a mês

# RESOLVA AQUI:
df['periodo'] = pd.to_datetime(df['periodo'])
df['ano'] = df['periodo'].dt.year
df['mes'] = df['periodo'].dt.month
df['valor_mil'] = df['valor'] / 1000

df = df.sort_values(by=['descricao', 'periodo'])
df['crescimento'] = df.groupby('descricao')['valor'].pct_change()
df


# ===========================================================
# PARTE 7 – QUALIDADE DE DADOS
# ===========================================================

# Exercício 10
# 1. Verifique valores nulos
# 2. Verifique valores negativos
# 3. Verifique duplicatas

# RESOLVA AQUI:
df.isnull().sum()
df[df["valor"]<0]
df.duplicated().sum()
