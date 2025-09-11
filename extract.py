import requests
import pandas as pd

class Extract:
    def __init__(self, url=None):
        self.url = url or "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=brl&days=7"

    def extraindo_dados(self):
        """
        Função que extrai dados de preços de Bitcoin da API CoinGecko.
        Retorna os dados em formato JSON, com informações de preço ao longo de 7 dias.
        """
        try:
            
            response = requests.get(self.url)
              
            response.raise_for_status()  
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"Erro na requisição HTTP: {http_err}")
        except Exception as err:
            raise Exception(f"Erro desconhecido: {err}")
        
        try:

            data = response.json()
        except ValueError:
            raise Exception("Erro ao converter a resposta para JSON")
        

        return data


if __name__ == "__main__":
    extract = Extract()
    try:
        dados = extract.extraindo_dados()
        print(dados) 
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
