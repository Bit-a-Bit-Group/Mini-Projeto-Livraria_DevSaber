-- CONSULTAS
SELECT *
FROM `t1engenhariadados.turma3_grupo8.Clientes` 
WHERE Estado_Cliente = 'SP' 
ORDER BY Nome_Cliente ASC

--clientes de sao paulo 
-- tabela de produtos

SELECT * FROM `t1engenhariadados.turma3_grupo8.Produtos` 

--exibindo todos  os produtos da tabela
SELECT *
FROM `t1engenhariadados.turma3_grupo8.Produtos`
WHERE Preco_Produto > 100
ORDER BY Preco_Produto desc


SELECT *
FROM `t1engenhariadados.turma3_grupo8.Produtos`
WHERE Preco_Produto < 50
ORDER BY Preco_Produto desc


--TABELA DE VENDAS,DATA DA PRIMEIRA COMPRA E ULTIMA COMPRA REGISTRADA
SELECT *
FROM `t1engenhariadados.turma3_grupo8.Vendas`
WHERE Data_Venda BETWEEN '2024-02-20' AND '2024-05-10'
ORDER BY Data_Venda asc


--usando join para produto de ficcao cientifica e tabela de vendas
SELECT *
FROM `t1engenhariadados.turma3_grupo8.Vendas` AS v
JOIN `t1engenhariadados.turma3_grupo8.Produtos` AS p
ON v.ID_Produto = p.ID_Produto
WHERE Categoria_Produto = 'Ficção Científica'

--Pergunta 4: Qual é o valor total de cada venda?
SELECT
    V.ID_Venda,
    SUM(V.Quantidade * P.Preco_Produto) AS Valor_Total_Venda
FROM `t1engenhariadados.turma3_grupo8.Vendas` AS V
JOIN `t1engenhariadados.turma3_grupo8.Produtos` AS P
    ON V.ID_Produto = P.ID_Produto
GROUP BY
    V.ID_Venda
ORDER BY
    V.ID_Venda
LIMIT 10;

--Pergunta 5: Qual é o produto mais vendido?
SELECT
    P.Nome_Produto,
    SUM(V.Quantidade) AS Quantidade_Total_Vendida
FROM `t1engenhariadados.turma3_grupo8.Vendas` AS V
JOIN `t1engenhariadados.turma3_grupo8.Produtos` AS P
    ON V.ID_Produto = P.ID_Produto
GROUP BY
    P.Nome_Produto
ORDER BY
    Quantidade_Total_Vendida DESC
LIMIT 10;

--VIEW
CREATE OR REPLACE VIEW `t1engenhariadados.turma3_grupo8.v_relatorio_vendas_detalhado` AS
SELECT
    V.ID_Venda,
    V.Data_Venda,
    C.Nome_Cliente,
    C.Estado_Cliente,
    P.Nome_Produto,
    P.Categoria_Produto,
    V.Quantidade,
    P.Preco_Produto,
    (V.Quantidade * P.Preco_Produto) AS Valor_Total
FROM `t1engenhariadados.turma3_grupo8.Vendas` AS V
JOIN `t1engenhariadados.turma3_grupo8.Clientes` AS C ON V.ID_Cliente = C.ID_Cliente
JOIN `t1engenhariadados.turma3_grupo8.Produtos` AS P ON V.ID_Produto = P.ID_Produto;
