import json
import pandas as pd

file = open("./dados/vendas.json")
data = json.load(file)

# chamando o pandas para tabular o json
df = pd.DataFrame.from_dict(data)

 # formatando de string para data
df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')


file.close()