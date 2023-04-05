import json
import pandas as pd
import requests
import json


url = "https://api-football-beta.p.rapidapi.com/teams/statistics"

queries = [
    {"season": "2022", "league": "71", "team": "121"},
    {"season": "2022", "league": "71", "team": "126"},
    {"season": "2022", "league": "71", "team": "128"},
    {"season": "2022", "league": "71", "team": "131"}
]

headers = {
    'x-rapidapi-host': "api-football-beta.p.rapidapi.com",
    'x-rapidapi-key': "###########"
}

# Cria um dicionário vazio para armazenar as informações
data = {}

# Itera sobre as queries e faz o request para cada uma
for query in queries:
    response = requests.request("GET", url, params=query, headers=headers)

    # Adiciona as informações ao dicionário
    key = f"{query['league']}-{query['team']}"
    data[key] = response.json()

# Salva o dicionário em um arquivo JSON
with open('dados.json', 'w') as f:
    json.dump(data, f)


