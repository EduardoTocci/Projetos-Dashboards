import json
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "dados", "vendas.json")

# Abrindo e carregando o JSON no mesmo bloco
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Convertendo para DataFrame
df = pd.DataFrame.from_dict(data)

# Formatando a coluna de datas
df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')
