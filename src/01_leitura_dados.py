import pandas as pd

df = pd.read_csv("data/raw/SuperMarket Analysis.csv")
print (df.head())
df.info()