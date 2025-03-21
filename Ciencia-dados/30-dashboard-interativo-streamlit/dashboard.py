# %% [markdown]
# # Dashboard Interativo com Streamlit

# %%
#%pip install streamlit

# %%
# Importando Bibliotecas
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
# Titulo
st.title("Dashboard Interativo - Segmentação de Clientes")

# %%
# Carregando os dados
@st.cache_data
def carregar_dados():
  return pd.read_csv("../../datasets/clientes_kmeans2.csv")

df = carregar_dados()

# %%
df

# %%
#Sidebar com filtros
st.sidebar.header("Filtros")
categoria = st.sidebar.multiselect(
  "Categoria de Produto Preferida",
  options=df["categoria_produto_preferida"].unique(),
  default=df["categoria_produto_preferida"].unique()
)

valor_min, valor_max = st.sidebar.slider(
  "Faixa de Valor Total de Compras",
  float(df["valor_total_compras"].min()),
  float(df["valor_total_compras"].max()),
  (float(df["valor_total_compras"].min()), float(df["valor_total_compras"].max())),
)

# %%
# Aplicando filtros
df_filtrado = df[
  (df["categoria_produto_preferida"].isin(categoria)) &
  (df["valor_total_compras"].between(valor_min, valor_max))
]

# %%
# Métricas
st.subheader("Resumo de Clientes Filtrados")
st.metric("Total de Clientes", len(df_filtrado))

# %%
# Gráfico de Dispersão
st.subheader("Visualização dos Clusters")
fig, ax = plt.subplots()
sns.scatterplot(
  x="valor_total_compras",
  y="frequencia_compras",
  hue="cluster_kmeans",
  data=df_filtrado,
  palette="viridis",
  ax=ax
)
st.pyplot(fig)

# %%
# Perfil dos cluster
st.subheader("Perfil Médio dos clusters")
perfil = df_filtrado.groupby("cluster_kmeans")[['valor_total_compras', "frequencia_compras", "recencia_ultima_compra"]].mean()
st.dataframe(perfil.style.highlight_max(axis=0))

# %%
# Interpretação
st.markdown("""
  - Cluster 0: [Ex: Clientes de Alto Valor]
  - Cluster 1: [Ex: Clientes Regulares]
  - Cluster 2: [Ex: Clientes Inativos]
""")


