
# Importações:
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config('Análise Logistica', layout='wide')

# Carregar os dados
df = pd.read_excel("base_logistica_completa.xlsx",sheet_name="Entregas")
# Ler os dados                   
# Tirando dados duplicados   
unique_categoria = df['Categoria'].unique()
unique_tipo_Veiculo = df['Veiculo'].unique()
todos = df

filtro_categoria, filtro_veiculo = st.columns(2)

with filtro_categoria:
    categoria = st.selectbox("Selecione a categoria dos produtos", unique_categoria)
with filtro_veiculo:
    veiculo = st.selectbox("Selecione o veículo",unique_tipo_Veiculo)


# Filtrando categorias

filtro_produto_categoria = df[(df['Categoria'] == categoria) &  (df['Veiculo'] == veiculo)]

# Criando as métricas
# Total entregas
total_entregas = len(filtro_produto_categoria)
# Soma dos fretes
total_fretes = filtro_produto_categoria['Valor_Frete'].sum()

col1, col2 = st.columns(2)

col1.metric("Total de entregas", total_entregas)
col2.metric("Total de fretes ", round(total_fretes,2))

# Gráfico de entregas por estado


quantidade_entregas = filtro_produto_categoria.groupby('Estado_Entrega')['Produto'].count().reset_index()

st.bar_chart(data=quantidade_entregas,x='Estado_Entrega',y='Produto')

filtro_produto_categoria

        

#produto = st.selectbox("Selecione a categoria dos produtos", categoria)
    # Filtro por categoria de produto
#filtro_categoria = df[df['Categoria'] == produto]


    #categoria = df('Entregas')['Categoria'].unique()
    #categoria
#dataframe['Disciplina'].unique():
    #estado = st.selectbox("Selecione os estado", ['SP','MG','ES'])
    
    #peso_min = dataframe['Peso_Kg'].min()

    #peso_max = dataframe['Peso_Kg'].max()
    #filtrado = dataframe[(dataframe['Peso_Kg'] > peso_min) & (dataframe['Peso_Kg'] < peso_max)]


    # Filtro dos dados
    #colfiltro1, colfiltro2 = st.columns(2)

    #with colfiltro1:
        #minimo = st.number_input(label="Minimo", min_value=0, max_value=int(peso_max))
    #with colfiltro2:
        #maximo = st.number_input(label="Máximo", min_value=0, max_value=int(peso_max))