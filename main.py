from functions import extract_data
import pandas as pd


url = "https://api-football-beta.p.rapidapi.com/teams/statistics"

queries = [
    {"season": "2022", "league": "71", "team": "121"},
    {"season": "2022", "league": "71", "team": "126"},
    {"season": "2022", "league": "71", "team": "128"},
    {"season": "2022", "league": "71", "team": "131"}
]

headers = {
    'x-rapidapi-host': "api-football-beta.p.rapidapi.com",
    'x-rapidapi-key': "#############"
}

# Cria um dicionário vazio para armazenar as informações
data = {}

extract_data(url, queries, headers, 'dados.json')

df = pd.read_json('dados.json')

# Escreve o DataFrame em um arquivo Excel
df.to_excel('dados.xlsx', index=False)
