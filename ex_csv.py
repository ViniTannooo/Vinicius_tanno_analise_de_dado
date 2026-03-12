
# LISTA DE EXERCÍCIOS – ANÁLISE DE DADOS COM PANDAS Dataset: Ranking
# Mundial de Universidades (notas.csv)


# ============================================================
# EXPLORAÇÃO INICIAL (EDA BÁSICA)
# ============================================================


import pandas as pd
df = pd.read_csv("/Users/viniciustanno/Desktop/Faculdade/Vinicius_tanno_analise_de_dado/Vinicius_tanno_analise_de_dado/notas.csv")

#----------------------------------------------
# Exercício 1 – Conhecendo o Dataset 

# 1. Quantas linhas e colunas existem?
df.shape

# 2. Quais são os tipos de dados? 
df.dtypes

# 3. Existe coluna com valores ausentes?
df.isnull().sum()

# 4. Qual é o período de anos disponível? 
df.loc[:,"year"].unique()

# 5. Quantos países diferentes existem?
df.loc[:,"country"].sum()

#----------------------------------------------
# Exercício 2 – Estatísticas Gerais 

# 1. Média do score 
df["score"].mean()

# 2. Maior score 
df["score"].max()

# 3.Menor score 
df["score"].min()

# 4. Média do score por ano 
df.groupby("year")["score"].mean()

# 5. Desvio padrão do score
df["score"].std()


# ============================================================
# FILTROS E SELEÇÕES
# ============================================================


#----------------------------------------------
# Exercício 3 – Top Universidades 

# 1. Mostre as 10 melhores universidades do mundo (menor world_rank) 
top_10 = df.nsmallest(10, "world_rank")
top_10["institution"]

# 2. Mostre as 5 melhores universidades do Brasil (se existirem) 
brazil = df[df["country"] == "Brazil"]
brazil_5 = brazil.nsmallest(5, "world_rank")
brazil_5["institution"]

# 3. Mostre universidades com score maior que 90 
top_90 = df[df["score"]>90]
top_90["institution"]

# 4. Mostre universidades dos EUA com score maior que 80
top_80 = df[df["score"]>80]
top_80_EUA = top_80[top_80["country"] == "USA"]
top_80_EUA["institution"]

#----------------------------------------------
# Exercício 4 – Seleção Avançada 

# 1. Mostre apenas as colunas: institution,
# country e score 
df[["institution", "country", "score"]]

# 2. Mostre universidades entre rank 50 e 100 
top_50_100 = df[(df["score"]>=50) & (df["score"]<=100)]
top_50_100 = df[df["score"].between(50, 100)]
top_50_100["institution"]

# 3. Mostre universidades cujo país é “United Kingdom”
uk = df[df["country"] == "United Kingdom"]
uk["institution"]


# ============================================================ PARTE 3 –
# MISSING VALUES
# ============================================================


#----------------------------------------------
# Exercício 5 – Valores Ausentes 

# 1. Quantos valores nulos existem na coluna broad_impact? 
null_broad_impact = df["broad_impact"].isnull().sum()
null_broad_impact

# 2. Qual percentual do dataset é nulo? 
null_percentage = 100*(null_broad_impact/df.shape[0])
print(f"O percentual do dataset que é nulo é {null_percentage:.2f}%")

# 3. Remova linhas com broad_impact nulo 
df_without_null = df.dropna(subset=["broad_impact"])
df_without_null

# 4. Preencha valores nulos com a média 
df_X = df.fillna(df["broad_impact"].mean())
df_X

# 5. Compare a média antes e depois do preenchimento
df_mean = df["broad_impact"].mean()
df_mean_X = df_X["broad_impact"].mean()
print(f"A média antes era {df_mean:.2f}, depois do preenchimento ficou {df_mean_X:.2f}")


# ============================================================ PARTE 4 –
# GROUPBY (ANÁLISE POR PAÍS E ANO)
# ============================================================


# Exercício 6 – Análise por País 

# 1. Média do score por país
df_countries = df.groupby("country")["score"].mean()
df_countries
 
# 2. País com maior média de score 
df_countries.idxmax()

# 3. Quantidade de universidades por país 
institution_country = df.groupby("country")["institution"].count()

# 4. Top 10 países com mais universidades
institution_country.sort_values(ascending=False).head(10)


# Exercício 7 – Análise por Ano 

# 1. Média do score por ano 
year_mean = df.groupby("year")["score"].mean()
year_mean

# 2. Qual ano teve maior média? 
year_mean.idxmax()

# 3. Faça um gráfico da evolução do score médio ao longo do tempo
year_mean.plot(kind="line", marker="o", figsize=(10,5),color="darkblue")