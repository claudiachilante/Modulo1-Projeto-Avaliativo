# Leitura dos dados / mostrando os primeiros registros, informações gerais e estatísticas descritivas

import pandas as pd

df = pd.read_csv("data/raw/SuperMarket Analysis.csv")
print (df.head())
df.info()
print(df.describe())