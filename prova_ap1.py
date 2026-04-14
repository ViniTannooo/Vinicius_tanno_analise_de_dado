# O dataset NCR Ride Bookings contém registros de corridas urbanas realizadas em regiões da National Capital Region (NCR), que abrange Delhi, Gurgaon, Noida, Ghaziabad, Faridabad e áreas próximas.
# Utilize os arquivos : ncr_ride_bookings.csv para resolver as questoes.
# Principais informaçoes no dataset:
# Date → Data da corrida
# Time → Horário da corrida
# Booking ID → Identificador da corrida
# Booking Status → Status da corrida
# Customer ID → Identificador do cliente
# Vehicle Type → Tipo de veículo
# Pickup Location → Local de embarque
# Drop Location → Local de desembarque
# Booking Value → Valor da corrida
# Ride Distance → Distância percorrida
# Driver Ratings → Avaliação do motorista
# Customer Rating → Avaliação do cliente
# Payment Method → Método de pagamento
# Questões:

import pandas as pd
import requests

df_book = pd.read_csv("/Users/viniciustanno/Desktop/Faculdade/Vinicius_tanno_analise_de_dado/Vinicius_tanno_analise_de_dado/ncr_ride_bookings.csv")

# (0,5) 1 - Quantas corridas estão com Status da Corrida como Completada ("Completed") no dataset? 
df_book_completed = float(df_book[df_book["Booking Status"] == "Completed"]["Booking Status"].count())
print(f"{int(df_book_completed)} corridas estão com Status de Completada")

# (0,5) 2 - Qual a proporção em relação ao total de corridas?
df_book_completed_proportion = df_book_completed/float(df_book["Booking ID"].count())
print(f"{df_book_completed_proportion*100}% das corridas foram completadas")
# (0,5) 3 - Calcule a média da Distância ("Ride Distance") percorrida por cada Tipo de veículo.
df_book_mean_vehicle = df_book.groupby("Vehicle Type")["Ride Distance"].mean()
print(f"A média de distância percorrida por tipo de veículo foi:\n{df_book_mean_vehicle}")

# (0,5) 4 - Qual o Metodo de Pagamento ("Payment Method") mais utilizado pelas bicicletas ("Bike") ?
df_bike_payment = df_book[df_book["Vehicle Type"] == "Bike"].groupby("Payment Method")["Booking ID"].count()
print(f"{df_bike_payment.idxmax()} foi o método de pagamento mais utilizado pelas bicicletas")

# (0,5) 5 - Qual o valor total arrecadado ("Booking Value") apenas das corridas Completed?
df_value_completed = float(df_book[df_book["Booking Status"] == "Completed"]["Booking Value"].sum())
print(f"O valor total arrecadado das corridas completadas é de ${df_value_completed}")

# (0,5) 6 - E qual o ticket médio ("Booking Value")dessas corridas Completed?
df_value_completed_mean = float(df_book[df_book["Booking Status"] == "Completed"]["Booking Value"].mean())
print(f"O ticket médio das corridas completadas é de ${df_value_completed_mean}")

# (1,5) 7 - O IPEA disponibiliza uma API pública com diversas séries econômicas. 
# Para encontrar a série de interesse, é necessário primeiro acessar o endpoint de metadados.
# Acesse o endpoint de metadados: "http://www.ipeadata.gov.br/api/odata4/Metadados";
# Transforme em um DataFrame;
# Filtre para encontrar as séries da Fipe relacionadas a venda de imoveis (“vendas - Brasil”).
# Dica: 
# Utilize a coluna FNTSIGLA para encontrar a serie da Fipe;
# Utilize a coluna SERNOME para encontrar as vendas de imoveis no Brasil;

URL_IPEA = "http://www.ipeadata.gov.br/api/odata4/Metadados"

response_IPEA = requests.get(URL_IPEA)

response_IPEA.status_code

df_IPEA = pd.DataFrame(response_IPEA.json())


# (1,5) 8 -  Descubra qual é o código da série correspondente (coluna: SERCODIGO).
# CODIGO_ENCONTRADO=''
# Usando o código encontrado, acesse a API de valores: f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{CODIGO_ENCONTRADO}')"
# Construa um DataFrame através da chave 'value' do retorno da api
# Selecione apenas as colunas datas (VALDATA) e os valores (VALVALOR).
# Exiba a Data e o Valor que teve o valor maximo de vendas.



# (1,5) 9 - Descubra quanto rendeu a VALE no ano de 2025
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# params = {"ticker": "VALE3", "data_ini": "2001-01-01", "data_fim": "2026-12-31"}
# response = requests.get(
#     f"{base_url}/preco/corrigido",
#     headers={"Authorization": f"Bearer {token}"},
#     params=params,
# )

URL_FIN = "https://laboratoriodefinancas.com/api/v2"

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc3MTE2Nzk2LCJpYXQiOjE3NzQ1MjQ3OTYsImp0aSI6IjFmZTg2MzE3NzU3MTRmNDY4Y2UyZWFmMTdkZmUxYWQ4IiwidXNlcl9pZCI6IjExMiJ9.MwFBcwADjVPl8mqIn06OT7cvU-Aao12HiWiQQkwCjYc"

params = {"ticker": "VALE3", "data_ini": "2025-01-01", "data_fim": "2025-12-31"}

response = requests.get(
    f"{URL_FIN}/preco/corrigido",
    headers={"Authorization": f"Bearer {token}"},
    params=params,
    )

response.status_code

df_preco_VALE_2025 = pd.DataFrame(response.json())
df_preco_VALE_2025["data"] = pd.to_datetime(df_preco_VALE_2025["data"])
df_preco_VALE_2025 = df_preco_VALE_2025.sort_values(by="data", ascending=True)
df_rendimento_VALE_2025 = ((float(df_preco_VALE_2025.iloc[-1]["fechamento"])/float(df_preco_VALE_2025.iloc[0]["abertura"]))-1)*100

print(f"No ano de 2025, a Vale rendeu {df_rendimento_VALE_2025}%")

# (1,5) 10 - Você tem acesso à API do Laboratório de Finanças, que fornece dados do Planilhão em formato JSON. 
# Selecione a empresa do setor de "tecnologia" que apresenta o maior ROE (Return on Equity) na data base 2024-04-01.
# Exiba APENAS AS COLUNAS "ticker", "setor" e o "roe"
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# response = requests.get(
#     f"{base_url}/bolsa/planilhao",
#     headers={"Authorization": f"Bearer {token}"},
#     params={"data_base": "2026-04-01"},
# )

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "SEU_JWT"
response = requests.get(
    f"{base_url}/bolsa/planilhao",
    headers={"Authorization": f"Bearer {token}"},
    params={"data_base": "2026-04-01"},
    )

response.status_code

df = pd.DataFrame(response.json())
df_tech = df[df["setor"] == "tecnologia"]
df_tech = df_tech.sort_values(by="roe", ascending=False)
df_tech_1roe = df_tech.iloc[0]["ticker"]
print(f"A empresa de tecnologia com o maior ROE foi a {df_tech_1roe}")

# (1,5) 11 - Faça a Magic Formula através dos indicadores Return on Capital (roc) e Earning Yield (ey) no dia 2024-04-01.
# Monte uma carteira de investimento com 10 ações baseado na estratégia Magic Formula.
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# response = requests.get(
#     f"{base_url}/bolsa/planilhao",
#     headers={"Authorization": f"Bearer {token}"},
#     params={"data_base": "2026-04-01"},
# )

df["rank_roc"] = df["roc"].rank(ascending=False)
df["rank_ey"] = df["earning_yield"].rank(ascending=False)

df["magic_formula"] = df["rank_roc"] + df["rank_ey"]
df.sort_values(by="magic_formula", ascending=True)

df_top10 = df.iloc[0:10]
df_top10_ticker = df.iloc[0:10]["ticker"]

print(f"Aplicando a Magic Formula, as melhores empresas para se investir são: {df_top10_ticker}")

# (1,5) 12 - Quantos setores ("setor") tem essa carteira formada por 10 ações?

df_top10_setores = df_top10.groupby("setor").count()
df_top10_quant_setores = int(df_top10_setores["ticker"].count())
print(f"Existem {df_top10_quant_setores} setores nessa carteira")
