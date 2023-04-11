import requests
import json


def extract_data(url, queries, headers, file_name):
    # Cria um dicionário vazio para armazenar as informações
    data = {}

    # Itera sobre as queries e faz o request para cada uma
    for query in queries:
        response = requests.get(url, params=query, headers=headers)

        # Adiciona as informações ao dicionário
        key = f"{query['league']}-{query['team']}"
        data[key] = response.json()

    # Salva o dicionário em um arquivo JSON
    with open(file_name, 'w') as f:
        json.dump(data, f)
