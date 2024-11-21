import streamlit as st
import pandas as pd
from dataset import df
from utilidade import convert_csv,mensagem_sucesso

st.title("Dataset de Vendas")

#criação de filtros
with st.expander("Colunas"):
    colunas = st.multiselect(
        "Selecione as colunas",
        list(df.columns),
        list(df.columns)
    )

st.sidebar.title("Filtros")
with st.sidebar.expander("Categoria do Produto"):
    cat_produto = st.multiselect(
        "Selecione a Categoria",
        df["Categoria do Produto"].unique(),
        df["Categoria do Produto"].unique()

    )

with st.sidebar.expander("Produtos"):
    produto = st.multiselect(
     "Selecione os Produtos",
     df["Produto"].unique(),
     df["Produto"].unique()
     
    )

with st.sidebar.expander("Preço do Produto"):
    preco = st.slider(
        "Selecione o Preço",
        0,5000,
        (0,5000)
    )

with st.sidebar.expander("Data da Compra"):
    data_inicio = st.date_input(
        "Data de Início",
        df["Data da Compra"].min()
    )
    data_fim = st.date_input(
        "Data de Fim",
        df["Data da Compra"].max()
    )

with st.sidebar.expander("Vendedor"):
    vendedor = st.multiselect(
        "Selecione o Vendedor",
        df["Vendedor"].unique(),
        df["Vendedor"].unique()

    )

with st.sidebar.expander("Estado"):
    estado = st.multiselect(
        "Selecione o Vendedor",
        df["Local da compra"].unique(),
        df["Local da compra"].unique()

    )

filtro_dados = df[
    (df["Categoria do Produto"].isin(cat_produto)) &
    (df["Preço"].between(preco[0], preco[1])) &
    (df["Data da Compra"].between(pd.to_datetime(data_inicio), pd.to_datetime(data_fim))) &
    (df["Vendedor"].isin(vendedor)) &
    (df["Produto"].isin(produto)) &
    (df["Local da compra"].isin(estado))
]

filtro_dados = filtro_dados[colunas]

# fim dos filtros

st.dataframe(filtro_dados)

st.markdown(f"A tabela possui :blue[{filtro_dados.shape[0]}] linhas e :blue[{filtro_dados.shape[1]}] colunas")

st.markdown("Escreva o nome do arquivo")

coluna1,coluna2 = st.columns(2)
with coluna1:
    nome_arquivo = st.text_input(
        "",
        label_visibility="collapsed"
    )
    nome_arquivo += ".csv"
with coluna2:
    st.download_button(
        label="Baixar arquivo",
        data=convert_csv(filtro_dados),
        file_name=nome_arquivo,
        mime="text/csv",
        on_click=mensagem_sucesso
    )