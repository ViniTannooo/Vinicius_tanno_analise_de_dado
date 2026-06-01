import pandas as pd
import requests

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzgwNTcwNzA4LCJpYXQiOjE3Nzc5Nzg3MDgsImp0aSI6IjNmNTBiZWM4OWVkZDQzMWI5NTljZWFkYmFkZTdiNjYyIiwidXNlcl9pZCI6IjExOCJ9.4m2iY0iB32ZKdO6_uZb-H1Cu9zwOXJcenbCHAv-qTFE"
params = {"ticker": "LREN3", "ano_tri": "20254T"}
resp = requests.get(
    f"{base_url}/bolsa/balanco",
    headers={"Authorization": f"Bearer {token}"},
    params=params,
)

resp.status_code
data = resp.json()[0]['balanco']
df = pd.DataFrame(data)

def encontrar_contas_contabeis(df):
    
