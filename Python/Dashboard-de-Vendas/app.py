import streamlit as st
import plotly.express as pl
# importa o dataset de outro arquivo para esse 
from dataset import df
from utilidade import formatNumber,tabela_rec_produto,tabela_venda_produto,formatNumber2
from gráfico import criar_grafico_receita_estado,criacao_grafico_mensal,criacao_grafico_rec_catproduto ,criacao_venda_catproduto,criacao_venda_estado,avaliacao_compra,tipo_pagamento,grafico_venda_mensal,grafico_rec_vendedor,grafico_venda_vendedor



# deixa o site mais largo
st.set_page_config(layout="wide")
st.title("Dashboard de Vendas :shopping_trolley:")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)


# criação de filtros 

st.sidebar.title("Filtro de Vendedores")

filtro_vendedor = st.sidebar.multiselect( 
    "Vendedores",
    df["Vendedor"].unique()

)
filtro_Estado = st.sidebar.multiselect(
    "Estados",
    df["Local da compra"].unique()
)
filtro_cat_produto = st.sidebar.multiselect(
    "Categoria do Produto",
    df["Categoria do Produto"].unique()
)
filtro_produtos = st.sidebar.multiselect(
   "Selecione o Produto",
   df["Produto"].unique()
)


df_filtrado = df.copy()
if filtro_vendedor:
    df_filtrado = df_filtrado[df_filtrado["Vendedor"].isin(filtro_vendedor)]
if filtro_Estado:
    df_filtrado = df_filtrado[df_filtrado["Local da compra"].isin(filtro_Estado)]
if filtro_cat_produto:
    df_filtrado = df_filtrado[df_filtrado["Categoria do Produto"].isin(filtro_cat_produto)]
if filtro_produtos:
   df_filtrado = df_filtrado[df_filtrado["Produto"].isin(filtro_produtos)]


# criação de abas
aba1,aba2,aba3,aba4 = st.tabs(["Tabela" , "Receita" ,"Vendas" ,"Vendedores"])

with aba1:
    st.dataframe(df_filtrado)

with aba2:
    coluna1 , coluna2  = st.columns(2)
    
    with coluna1:

        format_value = formatNumber(df_filtrado["Preço"].sum() , "R$")
        card_html = f"""
        <div style='display: flex; height: 150px; width: 300px;
                    background-color: #f0f2f6; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);'>
            <div style='text-align: center; margin:auto'>
                <p style='margin: 0; font-size: 30px; font-weight: bold; color:#4986A7'>{format_value}</p>
                <p style='margin: 0; color:#0E1117;'>Receita Mensal</p>
            </div>
        </div>

     """
        st.markdown(card_html, unsafe_allow_html=True) 
        
        
    
    
    
    with coluna2:
        
        qnt_vendas = formatNumber2(df_filtrado.shape[0])
    
        card2_html = f"""
        
        <div style='display: flex; height: 150px; width: 300px;
                    background-color: #f0f2f6; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);'>
            <div style='text-align: center; margin:auto'>
                <p style='margin: 0; font-size: 30px; font-weight: bold; color:#4986A7'>{qnt_vendas}</p>
                <p style='margin: 0; color:#0E1117;'>Vendas</p>
            </div>
        </div>
     """
        st.markdown(card2_html, unsafe_allow_html=True)
        


    colunaA , colunaB , colunaC = st.columns(3)

    with colunaA:
     st.plotly_chart(criacao_grafico_rec_catproduto(df_filtrado),use_container_width=True)

    with colunaB:
     st.markdown("<tspan style='font-weight:bold;'><b>Tabela de Receita por Produto</b></tspan>", unsafe_allow_html=True)
     st.dataframe(tabela_rec_produto(df_filtrado),height=352,use_container_width=True)

    with colunaC:
     st.plotly_chart(criar_grafico_receita_estado(df_filtrado), use_container_width=True)
    
    st.plotly_chart(criacao_grafico_mensal(df_filtrado), use_container_width=True)
    



with aba3:
    coluna1,coluna2 = st.columns(2)

    with coluna1:
        st.markdown(card2_html,unsafe_allow_html=True)

    with coluna2:
        st.markdown(card_html,unsafe_allow_html=True)
        
    colunaA , colunaB , colunaC = st.columns(3)

    with colunaA:
        st.plotly_chart(criacao_venda_catproduto(df_filtrado),use_container_width=True)
        
    with colunaB:
        st.markdown("<tspan style='font-weight:bold;'><b>Tabela de Vendas por Produto</b></tspan>", unsafe_allow_html=True)
        st.dataframe(tabela_venda_produto(df_filtrado),use_container_width=True,height=352)

    with colunaC:
        st.plotly_chart(criacao_venda_estado(df_filtrado),use_container_width=True)
    
    colunaD,colunaE = st.columns(2)
    with colunaD:
        st.plotly_chart(tipo_pagamento(df_filtrado),use_container_width=True)

    with colunaE:
        st.plotly_chart(avaliacao_compra(df_filtrado) , use_container_width=True)
    
    st.plotly_chart(grafico_venda_mensal(df_filtrado),use_container_width=True)
     

with aba4:
        coluna1,coluna2 = st.columns(2)

        with coluna1:
            qnt_vendedores = df_filtrado["Vendedor"].nunique()
            card3_html = f"""
        <div style='display: inline-flex; height: 150px; width: 300px;
                    background-color: #f0f2f6; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);'>
            <div style='text-align: center; margin:auto'>
                <p style='margin: 0; font-size: 30px; font-weight: bold; color:#4986A7'>{qnt_vendedores}</p>
                <p style='margin: 0; color:#0E1117;'>Vendedores</p>
            </div>
        </div>
     """
            st.markdown(card3_html,unsafe_allow_html=True)
            st.plotly_chart(grafico_rec_vendedor(df_filtrado) , use_container_width=True)

        with coluna2:
             qnt_vendas = formatNumber2(df_filtrado.shape[0])
             card4_html = f"""
            <div style='display: inline-flex; height: 150px; width: 300px;
                    background-color: #f0f2f6; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);'>
            <div style='text-align: center; margin:auto'>
                <p style='margin: 0; font-size: 30px; font-weight: bold; color:#4986A7'>{qnt_vendas}</p>
                <p style='margin: 0; color:#0E1117;'>Vendas</p>
            </div>
        </div>
        """
             st.markdown(card4_html,unsafe_allow_html=True)
             st.plotly_chart(grafico_venda_vendedor(df_filtrado) , use_container_width=True)