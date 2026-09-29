
-- ============================================
-- CONSULTAS SQL
-- ============================================

-- Conferência dos dados da camada Raw
SELECT *
FROM raw_vendas
LIMIT 10;

-- PRIMEIRA PERGUNTA: Qual filial teve a maior receita?

SELECT
    "Branch",
    SUM("Total"::NUMERIC) AS receita_total
FROM raw_vendas
GROUP BY "Branch"
ORDER BY receita_total DESC;

-- SEGUNDA PERGUNTA: Qual filial teve o maior número de vendas?
SELECT
    "Branch",
    COUNT("Invoice ID") AS quantidade_vendas
FROM raw_vendas
GROUP BY "Branch"
ORDER BY quantidade_vendas DESC;

-- TERCEIRA PERGUNTA: Qual linha de produto teve a maior receita?
SELECT
    "Product line",
    SUM("Total"::NUMERIC) AS receita_total
FROM raw_vendas
GROUP BY "Product line"
ORDER BY receita_total DESC;

-- QUARTA PERGUNTA: Qual linha de produto teve o maior média de avaliações?
SELECT
    "Product line",
    AVG("Rating"::NUMERIC) AS media_avaliacoes
FROM raw_vendas
GROUP BY "Product line"
ORDER BY media_avaliacoes DESC;

-- QUINTA PERGUNTA: Qual forma de pagamento mais utilizada?
SELECT
    "Payment",
    COUNT(*) AS quantidade_pagamentos
FROM raw_vendas
GROUP BY "Payment"
ORDER BY quantidade_pagamentos DESC;

-- SEXTA PERGUNTA: Qual foi o valor médio das vendas?
SELECT
    AVG("Total"::NUMERIC) AS valor_medio_vendas
FROM raw_vendas;

-- SÉTIMA PERGUNTA: Qual foi a maior venda?
SELECT
    MAX("Total"::NUMERIC) AS maior_venda
FROM raw_vendas;

-- OITAVA PERGUNTA: Qual foi o dia da semana que teve mais vendas?
SELECT
    TRIM(TO_CHAR(TO_DATE("Date", 'MM/DD/YYYY'), 'Day')) AS dia_semana,
    COUNT(*) AS quantidade_vendas
FROM raw_vendas
GROUP BY dia_semana
ORDER BY quantidade_vendas DESC;

