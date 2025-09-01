# Relatório – Análise de Dados Livraria DevSaber

## 1. Contexto da Livraria DevSaber

A Livraria DevSaber é uma livraria criada para apoiar leitores e interessados em tecnologia, programação e inovação.

Ainda que fictícia, tem uma missão realista: oferecer os melhores livros técnicos e de educação continuada aos profissionais, ajudando-os a evoluírem em suas carreiras.

Com o aumento da base de clientes e das vendas, o dono percebeu a necessidade de gerar insights estratégicos e decidiu substituir planilhas por um pipeline de dados no Google BigQuery.

## 2. Por que planilhas não são ideais

- Escalabilidade limitada
- Baixa performance
- Colaboração difícil
- Falta de automação
- Análises limitadas
- Risco de corromper o arquivo

## 3. Perguntas de negócio

- Quais são os livros mais vendidos?
- Qual o faturamento por mês?
- Quem são os clientes mais fiéis?
- Quais categorias de produtos geram mais receita?
- Que estratégia de divulgação, baseada no fluxo de vendas, posso seguir para expandir meu negócio?

## 4. Consultas SQL e Resultados

### Livros mais vendidos

**Query:**

```sql
SELECT nome_produto, SUM(quantidade) AS total_vendas
FROM `my-project-90354-470710.livraria_devsaber.vendas`
GROUP BY nome_produto
ORDER BY total_vendas DESC
LIMIT 10;

```

**Resultado:**

| nome_produto | total_vendas |
| --- | --- |
| … | … |
| **Insight final:** |  |
| O livro com mais vendas indica os produtos a focar em promoções e estoque. |  |

### Faturamento por mês

**Query:**

```sql
SELECT FORMAT_DATE('%Y-%m', data_venda) AS mes,
       SUM(preco_produto * quantidade) AS faturamento
FROM `my-project-90354-470710.livraria_devsaber.vendas`
GROUP BY mes
ORDER BY mes;

```

**Resultado:**

| mes | faturamento |
| --- | --- |
| … | … |
| **Insight final:** |  |
| Meses com maior faturamento ajudam a planejar campanhas sazonais ou promoções estratégicas. |  |

### Clientes mais fiéis

**Query:**

```sql
SELECT nome_cliente,
       SUM(quantidade) AS total_compras
FROM `my-project-90354-470710.livraria_devsaber.vendas`
GROUP BY nome_cliente
ORDER BY total_compras DESC
LIMIT 10;

```

**Resultado:**

| nome_cliente | total_compras |
| --- | --- |
| … | … |
| **Insight final:** |  |
| Clientes mais fiéis podem receber ofertas exclusivas ou programas de fidelidade. |  |

### Categorias de produtos mais lucrativas

**Query:**

```sql
SELECT categoria_produto,
       SUM(preco_produto * quantidade) AS faturamento_total
FROM `my-project-90354-470710.livraria_devsaber.vendas`
GROUP BY categoria_produto
ORDER BY faturamento_total DESC;

```

**Resultado:**

| categoria_produto | faturamento_total |
| --- | --- |
| … | … |
| **Insight final:** |  |
| Categorias mais lucrativas devem receber prioridade no estoque e no marketing. |  |

### Meses com maior volume de vendas (para estratégia de divulgação)

**Query:**

```sql
SELECT EXTRACT(MONTH FROM data_venda) AS mes,
       SUM(quantidade) AS total_vendas
FROM `my-project-90354-470710.livraria_devsaber.vendas`
GROUP BY mes
ORDER BY total_vendas DESC;

```

**Resultado:**

| mes | total_vendas |
| --- | --- |
| … | … |
| **Insight final:** |  |
| Meses com maior volume de vendas são ideais para campanhas de divulgação e promoções especiais. |  |

## 5. Observações gerais

- Livros mais vendidos → foco em promoções e estoque.
- Meses com maior faturamento → planejar campanhas sazonais.
- Categorias mais lucrativas → priorizar marketing e estoque.
- Clientes mais fiéis → considerar programas de fidelidade ou ofertas especiais.

