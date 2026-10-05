# Leitura dos dados / mostrando informações gerais e estatísticas descritivas.
import pandas as pd

df = pd.read_csv("data/raw/SuperMarket Analysis.csv")
print (df.head())
df.info()
print(df.describe())