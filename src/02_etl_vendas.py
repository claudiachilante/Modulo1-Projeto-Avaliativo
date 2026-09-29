# Importação do Pandas e primeira leitura dos dados ( estrutura / original).

from tkinter import S

import pandas as pd
df = pd.read_csv("data/raw/SuperMarket Analysis.csv")
print (df.head())
df.info()

# Conversão do Date de texto para data.

df["Date"] = pd.to_datetime(df["Date"])
df.info()

# Conversão do Time de texto para hora.

df["Time"] = pd.to_datetime(df["Time"], format='%I:%M:%S %p').dt.time
df.info()

# Verificação de valores nulos e duplicados.
print (df.isnull().sum())
print (df.duplicated().sum())

# Criação de uma nova coluna com o valor da compra (Unit price * Quantity + Tax 5%).
df["Valor_da_Compra"] = df["Unit price"] * df["Quantity"] + df["Tax 5%"]
print(df[["Valor_da_Compra", "Sales"]].head())

# Conferencia do valor da compra com o valor de vendas.
print (df[["Valor_da_Compra", "Sales"]].head())
print((df["Valor_da_Compra"] - df["Sales"]). abs().max())

# Mostra o nome das colunas do dataframe.
print (df.columns)

# Renomeando colunas.
df = df.rename(columns={
    "Invoice ID": "id_venda",
    "Branch": "filial",
    "City": "cidade",
    "Customer type": "tipo_cliente",
    "Gender": "genero",
    "Product line": "linha_produto",
    "Unit price": "preco_unitario",
    "Quantity": "quantidade",
    "Tax 5%": "imposto",
    "Sales": "valor_total",
    "Date": "data_venda",
    "Time": "hora_venda",
    "Payment": "forma_pagamento",
    "cogs": "custo_mercadoria",
    "gross margin percentage": "margem_percentual",
    "gross income": "receita_bruta",
    "Rating": "avaliacao"
})
print(df.columns)

# Salvando o arquivo tratado
df.to_csv("data/processed/vendas_tratadas.csv", index=False)

# Verificando a tipagem das colunas numericas
print(df.dtypes)

# Verificando se existem vendas zeradas ou negativas
print("Vendas zeradas ou negativas:")
print(df[(df["valor_total"] <= 0)])
 
# Verificando preços negativos ou zerados
print("Preços zerados ou negativos:")
print(df[(df["preco_unitario"] <= 0)])

# Verificando impostos negativos ou zerados
print("Impostos zerados ou negativos:")
print(df[(df["imposto"] <= 0)])

# Verificando Valor Total negativo ou zerado
print("Valor Total zerado ou negativo:")
print(df[(df["valor_total"] <= 0)])

# Verificando custos negativos ou zerados
print("Custos zerados ou negativos:")
print(df[(df["custo_mercadoria"] <= 0)])

# Verificando Avaliação, valores entre 0 à 10.
print("Avaliações fora do intervalo [0, 10]:")
print(df[(df["avaliacao"] < 0) | (df["avaliacao"] > 10)])