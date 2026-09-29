# importação do Pandas e leitura inicial do arquivo CSV.

import pandas as pd
df = pd.read_csv('data/processed/vendas_tratadas.csv')
df['data_venda'] = pd.to_datetime(df['data_venda'])

print(df.head())
print(df.info())

# Exploração dos dados: Estatísticas descritivas.
print(df.describe())

# Responde a primeira pergunta: Qual filial apresentou o maior faturamento?
faturamento_filial = df.groupby('filial')['valor_total'].sum()
print(faturamento_filial)

# Responde a segunda pergunta: Qual filial apresentou o maior quantidade de vendas?
quantidade_vendas_filial = df.groupby('filial')['id_venda'].count()
print(quantidade_vendas_filial)

# Responde a terceira pergunta: Qual linha de produto apresentou o maior faturamento?
faturamento_linha_produto = df.groupby('linha_produto')['valor_total'].sum()
print(faturamento_linha_produto)

# Responde a quarta pergunta: Qual linha de produto recebeu a melhor avaliação média?
avaliacao_media_linha_produto = df.groupby('linha_produto')['avaliacao'].mean()
print(avaliacao_media_linha_produto)

# Responde a quinta pergunta: Qual foi a forma de pagamento mais utilizada?
forma_pagamento_mais_utilizada = df['forma_pagamento'].mode()[0]
print(forma_pagamento_mais_utilizada)

# Responde a sexta pergunta: Qual foi o valor médio das vendas?
valor_medio_vendas = df['valor_total'].mean()
print(valor_medio_vendas)

# Responde a sétima pergunta: Qual foi a maior venda registrada?
maior_venda = df['valor_total'].max()
print(maior_venda)

# Responde a oitava pergunta: Em qual dia da semana ocorreu a maior quantidade de vendas?
df['dia_semana'] = df['data_venda'].dt.day_name()
quantidade_vendas_dia_semana = df.groupby('dia_semana')['id_venda'].count()
dia_maior_vendas = quantidade_vendas_dia_semana.idxmax()
print(dia_maior_vendas)

# GRAFICOS

import matplotlib.pyplot as plt

# Grafico 1: Faturamento por filial
faturamento_filial.sort_values().plot(kind='bar')

plt.title('Faturamento por Filial')
plt.xlabel('Filial')
plt.ylabel('Faturamento')
plt.tight_layout()

plt.savefig('resultados/faturamento_por_filial.png')
plt.close()

# Grafico 2: Filial realizou a maior quantidade de vendas
quantidade_vendas_filial.sort_values().plot(kind='bar')

plt.title('Quantidade de Vendas por Filial')
plt.xlabel('Filial')
plt.ylabel('Quantidade de Vendas')
plt.tight_layout()

plt.savefig('resultados/quantidade_vendas_por_filial.png')
plt.close()

# Grafico 3: Linha de produto apresentou o maior faturamento
faturamento_linha_produto.sort_values().plot(kind='bar')

plt.title('Faturamento por Linha de Produto')
plt.xlabel('Linha de Produto')
plt.ylabel('Faturamento')
plt.tight_layout()

plt.savefig('resultados/faturamento_por_linha_produto.png')
plt.close()

# Grafico 4: Linha de produto recebeu a melhor avaliação média
avaliacao_media_linha_produto.sort_values().plot(kind='bar')

plt.title('Avaliação Média por Linha de Produto')
plt.xlabel('Linha de Produto')
plt.ylabel('Avaliação Média')
plt.tight_layout()

plt.savefig('resultados/avaliacao_media_por_linha_produto.png')
plt.close()

# Grafico 5: A forma de pagamento mais utilizada
forma_pagamento = df['forma_pagamento'].value_counts()
forma_pagamento.plot(kind='bar')

plt.title('Forma de Pagamento Mais Utilizada')
plt.xlabel('Forma de Pagamento')
plt.ylabel('Quantidade de Vendas')
plt.tight_layout()

plt.savefig('resultados/forma_pagamento_mais_utilizada.png')
plt.close()

# Gráfico 6: Distribuição dos valores das vendas
valor_medio = df['valor_total'].mean()

plt.hist(df['valor_total'], bins=20)
plt.axvline(valor_medio, linestyle='--', linewidth=2)

plt.title('Distribuição dos Valores das Vendas')
plt.xlabel('Valor da Venda')
plt.ylabel('Quantidade de Vendas')

plt.tight_layout()

plt.savefig('resultados/distribuicao_valores_vendas.png')
plt.close()

# Gráfico 7: Maior venda
maior_venda = df['valor_total'].max()

plt.hist(df['valor_total'], bins=20)
plt.axvline(maior_venda, linestyle='--', linewidth=2)

plt.title('Maior Venda')
plt.xlabel('Valor da Venda')
plt.ylabel('Quantidade de Vendas')

plt.tight_layout()

plt.savefig('resultados/maior_venda.png')
plt.close()

# Gráfico 8: Quantidade de vendas por dia da semana
vendas_dia_semana = df['data_venda'].dt.day_name().value_counts()
vendas_dia_semana.plot(kind='bar')

plt.title('Quantidade de Vendas por Dia da Semana')
plt.xlabel('Dia da Semana')
plt.ylabel('Quantidade de Vendas')

plt.tight_layout()

plt.savefig('resultados/vendas_por_dia_semana.png')
plt.close()












