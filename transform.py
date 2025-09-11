import pandas as pd
from extract import Extract

class Transform:
    def __init__(self):
        self.extract = Extract()
        self.dados = self.extract.extraindo_dados()
        self.df = pd.DataFrame(self.dados["prices"], columns=['timestamp', 'precos'])

    def limpar_dados(self):
        """Remove duplicatas, valores nulos e faz o tratamento de dados"""
        self.df = self.df.drop_duplicates(subset='timestamp')
        self.df = self.df.dropna()

    def transformar_colunas(self):
        """Converte a coluna de timestamp e calcula a variação percentual"""
        self.df['datas'] = pd.to_datetime(self.df['timestamp'], unit='ms')
        self.df = self.df[self.df['precos'] > 605000]
        self.df = self.df[['datas', 'precos']]

    def calcular_variacoes(self):
        """Calcula a variação percentual e extrai as informações de data"""
        self.df['var_percentual'] = self.df['precos'].pct_change() * 100
        self.df['ano'] = self.df['datas'].dt.year
        self.df['mes'] = self.df['datas'].dt.month
        self.df['dia'] = self.df['datas'].dt.day

    def formatar_dados(self):
        """Remove a coluna de datas e arredonda os valores"""
        self.df = self.df.drop(columns=['datas'])
        self.df = self.df.round(2)

    def transformar(self):
        """Método principal que executa todas as transformações"""
        self.limpar_dados()
        self.transformar_colunas()
        self.calcular_variacoes()
        self.formatar_dados()
        return self.df


if __name__ == "__main__":
    transform = Transform()
    df_transformado = transform.transformar()
    print(df_transformado)
