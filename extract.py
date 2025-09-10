import requests
import pandas as pd
from datetime import datetime


def extract():
    '''
    Funcão que extrai dados da API
    '''
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=brl&days=7"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Erro na API: {response.status_code}")
    data = response.json()
    return data

data = extract()





df = pd.DataFrame(data["prices"], columns=['timestamp', 'precos'])
df = df.drop_duplicates(subset='timestamp')
df['datas'] = pd.to_datetime(df['timestamp'], unit='ms')
df = df[['datas', 'precos']]


df = df.round(2)
print(df)
