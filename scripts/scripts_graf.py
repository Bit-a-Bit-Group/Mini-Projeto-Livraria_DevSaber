
#1-

from google.colab import auth
from google.cloud import bigquery
import pandas as pd
import folium
from folium.plugins import HeatMap
import numpy as np
from IPython.display import display, HTML

auth.authenticate_user()

query_sp = """
SELECT *
FROM `t1engenhariadados.turma3_grupo8.Clientes` 
WHERE Estado_Cliente = 'SP'
"""
client = bigquery.Client()
df_sp = client.query(query_sp).to_dataframe()

print(f"Clientes de SP encontrados: {len(df_sp)}")

mapa = folium.Map(location=[-23.5505, -46.6333], zoom_start=7)
np.random.seed(42)
latitudes = np.random.uniform(-25.0, -20.0, len(df_sp))
longitudes = np.random.uniform(-53.0, -44.0, len(df_sp))

HeatMap(list(zip(latitudes, longitudes)), radius=20, blur=15).add_to(mapa)

folium.Marker(
    location=[-23.5505, -46.6333],
    popup=f"São Paulo: {len(df_sp)} clientes",
    icon=folium.Icon(color='red', icon='star')
).add_to(mapa)

display(HTML(mapa._repr_html_()))


#2 - Análise de Preços

from google.colab import auth
from google.cloud import bigquery
import matplotlib.pyplot as plt
import pandas as pd

auth.authenticate_user()
client = bigquery.Client()

query = """
SELECT Preco_Produto 
FROM `t1engenhariadados.turma3_grupo8.Produtos`
"""

df = client.query(query).to_dataframe()

caros = df[df['Preco_Produto'] > 100]
baratos = df[df['Preco_Produto'] < 50]
menor_valor = df['Preco_Produto'].min()
maior_valor = df['Preco_Produto'].max()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

## Boxplot comparativo
ax1.boxplot([baratos['Preco_Produto'], caros['Preco_Produto']], 
           labels=['< R$ 50', '> R$ 100'])
ax1.set_title('Comparação de Faixas de Preço')
ax1.set_ylabel('Preço (R$)')
ax1.grid(True, alpha=0.1)

## Histograma comparativo
ax2.hist(baratos['Preco_Produto'], alpha=0.7, label='< R$ 50', bins=15)
ax2.hist(caros['Preco_Produto'], alpha=0.7, label='> R$ 100', bins=15)
ax2.set_title('Distribuição de Preços')
ax2.set_xlabel('Preço (R$)')
ax2.set_ylabel('Frequência')
ax2.legend()
ax2.grid(True, alpha=0.1)

info_text = f"Menor valor: R$ {menor_valor:.2f}\nMaior valor: R$ {maior_valor:.2f}"
plt.figtext(0.5, 0.01, info_text, ha='center', fontsize=12, 
            bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.8))

plt.tight_layout()
plt.subplots_adjust(bottom=0.15)
plt.savefig('analise_precos.png', dpi=300, bbox_inches='tight')
plt.show()

total = len(df)
print(f"Estatísticas:")
print(f"Total de produtos: {total}")
print(f"Produtos < R$ 50: {len(baratos)} ({len(baratos)/total*100:.1f}%)")
print(f"Produtos > R$ 100: {len(caros)} ({len(caros)/total*100:.1f}%)")
print(f"Preço médio: R$ {df['Preco_Produto'].mean():.2f}")



#3 - Linha Temporal Vendas

from google.colab import auth
from google.cloud import bigquery
import matplotlib.pyplot as plt
import pandas as pd

auth.authenticate_user()
client = bigquery.Client()

query = """
SELECT 
    Data_Venda,
    COUNT(*) as Total_Vendas,
    SUM(Valor_Total) as Valor_Total
FROM `t1engenhariadados.turma3_grupo8.Vendas`
WHERE Data_Venda BETWEEN '2024-02-20' AND '2024-05-10'
GROUP BY Data_Venda
ORDER BY Data_Venda ASC
"""
dados = client.query(query).to_dataframe()
dados['Data_Venda'] = pd.to_datetime(dados['Data_Venda'])

plt.figure(figsize=(12, 6))
plt.plot(dados['Data_Venda'], dados['Total_Vendas'], marker='o', linewidth=2)
plt.title('Vendas por Dia - Período: 20/02 a 10/05/2024')
plt.ylabel('Quantidade de Vendas')
plt.xlabel('Data')
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('vendas_temporal.png', dpi=300, bbox_inches='tight')
plt.show()

print(f"Total de vendas: {dados['Total_Vendas'].sum()}")
print(f"Valor total: R$ {dados['Valor_Total'].sum():.2f}")


#4 - Ficção Científica

python
from google.colab import auth
from google.cloud import bigquery
import pandas as pd
import matplotlib.pyplot as plt

auth.authenticate_user()
client = bigquery.Client()

query = """
SELECT *
FROM `t1engenhariadados.turma3_grupo8.Vendas` as v
JOIN `t1engenhariadados.turma3_grupo8.Produtos` as p
ON v.ID_Produto = p.ID_Produto
WHERE p.Categoria_Produto = 'Ficção Científica'
ORDER BY v.Data_Venda ASC
"""

print(" EXECUTANDO QUERY COMPLETA COM JOIN...")
ficcao_df = client.query(query).to_dataframe()

print(f"{len(ficcao_df)} vendas de Ficção Científica encontradas!")

ficcao_df['Data_Venda'] = pd.to_datetime(ficcao_df['Data_Venda'])
ficcao_df['Mes'] = ficcao_df['Data_Venda'].dt.month_name()

vendas_por_mes = ficcao_df['Mes'].value_counts()

plt.figure(figsize=(10, 8))
vendas_por_mes.plot(kind='pie', autopct='%1.1f%%', colors=plt.cm.Set3.colors)
plt.title('Distribuição de Vendas por Mês - Ficção Científica', fontweight='bold')
plt.ylabel('')
plt.tight_layout()
plt.savefig('ficcao_cientifica_mes.png', dpi=300, bbox_inches='tight')
plt.show()

print(" TOP 3 PRODUTOS:")
top_3 = ficcao_df['Nome_Produto'].value_counts().head(3)
for i, (produto, qtd) in enumerate(top_3.items(), 1):
    valor = ficcao_df[ficcao_df['Nome_Produto'] == produto]['Valor_Total'].sum()
    print(f"{i}. {produto}: {qtd} vendas, R$ {valor:.2f}")

print(f"\n Total de vendas: {len(ficcao_df)}")
print(f" Valor total: R$ {ficcao_df['Valor_Total'].sum():.2f}")





#5 - Valor por Venda

from google.colab import auth
from google.cloud import bigquery
import matplotlib.pyplot as plt
import pandas as pd

auth.authenticate_user()
client = bigquery.Client()
query = """
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
LIMIT 10
"""
print("CALCULANDO VALOR TOTAL POR VENDA...")
vendas_df = client.query(query).to_dataframe()
print("DADOS CARREGADOS!")
print(vendas_df)
plt.figure(figsize=(12, 6))
plt.bar(vendas_df['ID_Venda'].astype(str), vendas_df['Valor_Total_Venda'], 
        color='lightblue', edgecolor='black', alpha=0.7)
plt.title('💰 Valor Total por Venda (Top 10)', fontweight='bold', pad=20)
plt.xlabel('ID da Venda')
plt.ylabel('Valor Total (R$)')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)

for i, valor in enumerate(vendas_df['Valor_Total_Venda']):
    plt.text(i, valor + 0.1, f'R$ {valor:.2f}', ha='center', va='bottom', fontweight='bold')
plt.tight_layout()
plt.savefig('valor_por_venda.png', dpi=300, bbox_inches='tight')
plt.show()





#6 - Top Produtos

from google.colab import auth
from google.cloud import bigquery
import matplotlib.pyplot as plt
import pandas as pd

auth.authenticate_user()
client = bigquery.Client()

query = """
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
LIMIT 10
"""

print(" BUSCANDO TOP 10 PRODUTOS MAIS VENDIDOS...")
top_produtos_df = client.query(query).to_dataframe()

print(" DADOS CARREGADOS!")
print(top_produtos_df)

plt.figure(figsize=(12, 8))
bars = plt.barh(top_produtos_df['Nome_Produto'], top_produtos_df['Quantidade_Total_Vendida'],
                color='skyblue', edgecolor='black', alpha=0.7)

plt.title(' TOP 10 Produtos Mais Vendidos\n(por Quantidade Total)', fontweight='bold', pad=20)
plt.xlabel('Quantidade Total Vendida')
plt.ylabel('Produto')
plt.grid(axis='x', alpha=0.3)

for bar, valor in zip(bars, top_produtos_df['Quantidade_Total_Vendida']):
    plt.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
             f'{valor:.0f}', ha='left', va='center', fontweight='bold')

plt.tight_layout()
plt.savefig('top_produtos_vendidos.png', dpi=300, bbox_inches='tight')
plt.show()


print("\n ESTATÍSTICAS:")
print("=" * 40)
print(f"Produto mais vendido: {top_produtos_df.iloc[0]['Nome_Produto']}")
print(f"Quantidade: {top_produtos_df.iloc[0]['Quantidade_Total_Vendida']} unidades")
print(f"Total geral top 10: {top_produtos_df['Quantidade_Total_Vendida'].sum()} unidades")