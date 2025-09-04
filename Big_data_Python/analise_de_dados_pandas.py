import pandas as pd

dados = 'C:/Users/alunoti/Downloads/archive/datapix.csv'
try:
    df = pd.read_csv(dados, sep=';')
    
    print("DataFrame carregado com sucesso!")
    print(df.head(10))
    print(df.tail(10))
    
except FileNotFoundError:
    print(f"Erro: O arquivo '{dados}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao carregar o arquivo: {e}")
