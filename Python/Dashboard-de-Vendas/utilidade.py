from dataset import df
import streamlit as st
import pandas as pd
import time


 # formatação de número
def formatNumber(value, prefix = ""):
    for unit in ["" , ""]:
        if value < 1000:
             return f'{prefix} {value:.3f} {unit}'
        value /= 1000
    return f"{prefix} {value:.3f} milhões"

def formatNumber2(value, prefix = ""):
    for unit in ["" , ""]:
        if value < 1000:
             return f'{value} {unit}'
        value /= 1000
    return f"{prefix} {value:.3f} milhões"


# tabela receita por produto
def tabela_rec_produto(df):
    tabela_receita_produto = df.groupby("Produto")[["Preço"]].sum().sort_values("Preço" , ascending=False).reset_index()
    tabela_receita_produto["Preço"] = tabela_receita_produto["Preço"].apply(lambda x:formatNumber(x,"R$"))
    tabela_receita_produto.columns = ["Produto", "Receita"]

    return tabela_receita_produto



def tabela_venda_produto(df):

# tabela venda por produto
    tabela_venda_produto = df.groupby("Produto").size().reset_index()
    tabela_venda_produto.columns = ["Produto" , "Vendas"]
    tabela_venda_produto = tabela_venda_produto.sort_values("Vendas",ascending=False)

    return tabela_venda_produto
# print(tabela_venda_produto)


# Função de converter arquivo csv
@st.cache_data
def convert_csv(df):
    return df.to_csv(index=False).encode("utf-8")

def mensagem_sucesso():
    sucess = st.success("Arquivo baixado com sucesso ✅"),
    time.sleep(3),
    sucess = st.empty()
    
    