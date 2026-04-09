import pandas as pd

df = pd.read_excel("/Users/viniciustanno/Desktop/Faculdade/Vinicius_tanno_analise_de_dado/Vinicius_tanno_analise_de_dado/salary.xlsx")
df

# 1 - Quantas linhas e quantas colunas tem o dataset?
df.shape

# 2 - Qual a média salarial? Qual é o maior salário? O menor salário?
salary_mean = df["salary"].mean()
df["salary"].max()
df["salary"].min()

# 3 - Crie um df com apenas as colunas job_title, salary, company_location, company_size, remote_ratio?
df[["job_title", "salary", "company_location", "company_size", "remote_ratio"]]

# 4 - Qual é o maior e menor salário de um “Data Scientist”? Onde fica essas empresas?
df[df["job_title"] == "Data Scientist"].max()
df[df["job_title"] == "Data Scientist"].min()

# 5 - Qual a profissão com a maior média salarial? E a menor?
salary_job = df.groupby("job_title")["salary"].mean()
salary_job.idxmax()
salary_job.idxmin()

# 6 - Quais as profissões com a média salarial maior que a média geral?
job_over_mean = salary_job[salary_job > salary_mean]

# 7 - Qual a localização com maior média salarial?
salary_loc = df.groupby("employee_residence")["salary"].mean()
salary_loc.idxmax()

# 8 - Quais as profissões que existem no Brasil (BR)?
df["job_title"][df["company_location"] == "BR"]

# 9 - Qual a média salarial no Brasil?
df["salary"][df["company_location"] == "BR"].mean()

# 10 - Quantas profissões existem no Brasil?
df["job_title"][df["company_location"] == "BR"].count()

# 11 - Qual a profissão que mais ganha no Brasil? (Considerando média salarial)
salary_job_BR = df[df["company_location"] == "BR"].groupby("job_title")["salary"].mean()
salary_job_BR.idxmax()

# 12 - Quantas profissões tem nos US e que trabalham em empresas grandes (L)?
df[(df["company_location"] == "US") & (df["company_size"] == "L")]["job_title"].nunique()

# 13 - Qual é a média salarial das empresas médias (M) na Canada (CA)?
df[(df["company_location"] == "CA") & (df["company_size"] == "M")]["salary"].mean()

# 14 - Qual é o país com mais profissões? E qual é o com menos?
df.groupby("company_location")["job_title"].nunique()

# 15 - Quem ganha mais que trabalha remoto, presencial ou híbrido?
# Na maioria dessas bases: 0 = Presencial, 50 = Híbrido, 100 = 100% Remoto
salary_ratio = df.groupby("remote_ratio")["salary"].mean()
salary_ratio.idxmax()

# 16 - Qual o país com maior numero de profissões trabalhando 100% remoto?
remote_countries = df[df["remote_ratio"] == 100].groupby("company_location")["job_title"].nunique()
remote_countries.idxmax()
