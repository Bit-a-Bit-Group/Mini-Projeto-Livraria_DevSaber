-- Tabela Clientes
CREATE OR REPLACE TABLE t1engenhariadados.turma3_grupo8.Clientes (
ID_Cliente INT64,
Nome_Cliente STRING,
Email_Cliente STRING,
Estado_Cliente STRING
);

-- Tabela Produtos
CREATE OR REPLACE TABLE t1engenhariadados.turma3_grupo8.Produtos (
ID_Produto INT64,
Nome_Produto STRING,
Categoria_Produto STRING,
Preco_Produto NUMERIC
);

-- Tabela Vendas
CREATE OR REPLACE TABLE t1engenhariadados.turma3_grupo8.Vendas (
ID_Venda INT64,
ID_Cliente INT64,
ID_Produto INT64,
Data_Venda DATE,
Quantidade INT64
);