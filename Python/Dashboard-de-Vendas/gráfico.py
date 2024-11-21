import plotly.express as pl
import pandas as pd
from dataset import df
from utilidade import formatNumber

# ===================== criação e processamento de df ==========================
def df_receita_estado(df):
    receita_venda_estado = df.groupby("Local da compra")[["Preço"]].agg(["count","sum"]).reset_index()
    receita_venda_estado.columns = ["Local da compra", 'Vendas', 'Receita']

    lat_lon = df.drop_duplicates(subset="Local da compra")[["Local da compra", "lat", "lon"]]
    receita_venda_estado = receita_venda_estado.merge(lat_lon, on="Local da compra").sort_values("Receita", ascending=False)
    receita_venda_estado["Preço Formatado"] = receita_venda_estado["Receita"].apply(lambda x:formatNumber(x,"R$"))
    # formatNumber(df.shape[0] ,"R$"))

    return receita_venda_estado

def df_catproduto(df):
    receita_catproduto = df.groupby("Categoria do Produto")[["Preço"]].agg(["sum","count"]).reset_index()
    receita_catproduto.columns = ["Categoria do Produto", "Preço" , "Vendas"]
    receita_catproduto["Categoria do Produto"] = receita_catproduto["Categoria do Produto"].str.capitalize()
    receita_catproduto["Receita"] = receita_catproduto["Preço"].apply(lambda x:formatNumber(x,"R$"))
    receita_catproduto = receita_catproduto.sort_values("Preço", ascending=False)

    return receita_catproduto

def df_venda_rec_mensal(df):
    receita_vendas_mensal = df.set_index('Data da Compra').groupby(pd.Grouper(freq='M')).agg({'Preço': ['sum', 'count']}).reset_index()
    receita_vendas_mensal.columns = ["Data da Compra" , "Preço" , "Vendas"]
    receita_vendas_mensal["Ano"] = receita_vendas_mensal["Data da Compra"].dt.year
    receita_vendas_mensal["Mês"] = receita_vendas_mensal["Data da Compra"].dt.month_name()
    receita_vendas_mensal["Receita"] = receita_vendas_mensal["Preço"].apply(lambda x:formatNumber(x,"R$"))

    return receita_vendas_mensal

def df_rec_venda_vendedor(df):
    # criando uma tabela com vendedor , receita e contagem de vendas
    receita_vendedores = pd.DataFrame(df.groupby("Vendedor")["Preço"].agg(["sum" , "count"])).reset_index()
    receita_vendedores.columns = ["Vendedor" , "Preço" , "Venda"]
    receita_vendedores["Receita"] = receita_vendedores["Preço"].apply(lambda x:formatNumber(x,"R$"))

    return receita_vendedores 
# ============================= Gráficos Aba2 (Receita ) =============================

def criar_grafico_receita_estado(df):
    
    receita_venda_estado = df_receita_estado(df)

    grafico_map_estado = pl.scatter_geo(
    receita_venda_estado,
    lat = "lat",
    lon = "lon",
    scope = "south america",
    size = "Receita",
    template= "seaborn",
    # quando passar o mouse em cima vai aparecer local da compra
    hover_name= "Local da compra",
    hover_data= {"lat":False , "lon":False ,"Preço Formatado":True , "Receita":False},
    title = "Receita por Estado"
)
    grafico_map_estado.update_geos(
    showframe = False,
    showcoastlines = False,
    projection_type="equirectangular",
    bgcolor="rgba(0,0,0,0)"
)
    return grafico_map_estado


def criacao_grafico_mensal(df):

    receita_mensal = df_venda_rec_mensal(df)
    
 # gráfico de receita mensal
    grafico_mensal = pl.line(
    receita_mensal,
    x = "Mês",
    y = "Preço",
    markers = True,
    range_y= (0 , receita_mensal.max()), #define o intervalo do eixo y do gráfico. O intervalo é definido de 0 até o valor máximo da receita mensal no DataFrame receita_mensal. Isso garante que o eixo y comece do zero e vá até o máximo valor de receita mensal.
    color= "Ano",
    line_dash= "Ano",
    title="Receita Mensal",
    hover_data={"Receita":True , "Preço":False}
    
    )

    grafico_mensal.update_layout(yaxis_title="Receita")

    return grafico_mensal


def criacao_grafico_rec_catproduto(df):
# gráfico receita por Categoria Produto
    
    receita_catproduto = df_catproduto(df)

    grafico_receita_catproduto = pl.bar(
    receita_catproduto,
    x = "Preço",
    y = "Categoria do Produto",
    orientation="h",
    text="Receita",
    title="Receita por Categoria Produtos",
    hover_data={"Preço":False}
    )
    grafico_receita_catproduto.update_layout(
        yaxis = dict(
            categoryorder = "total ascending"
        )
    )
    grafico_receita_catproduto.update_layout(xaxis_title="Receita")
    grafico_receita_catproduto.update_traces(marker_color="#2B5F82")

    return grafico_receita_catproduto


#====================================== Gráficos aba3 (Venda) ===============================================================

def criacao_venda_catproduto(df):

    # reutilizando o df criado na outra função
    receita_catproduto = df_catproduto(df)

    grafico_venda_catproduto = pl.bar(
    receita_catproduto,
    x = "Vendas",
    y = "Categoria do Produto",
    orientation="h",
    text_auto=True,
    title="Vendas por Categoria Produtos"
    )
    grafico_venda_catproduto.update_layout(
    yaxis = dict(
        categoryorder = "total ascending"
    )
    )
    grafico_venda_catproduto.update_traces(marker_color="#2B5F82")

    return grafico_venda_catproduto


def criacao_venda_estado(df):

    receita_venda_estado = df_receita_estado(df)

    grafico_venda_estado = pl.scatter_geo(

    receita_venda_estado,
    lat = "lat",
    lon = "lon",
    scope = "south america",
    size = "Vendas",
    template= "seaborn",
    # quando passar o mouse em cima vai aparecer local da compra
    hover_name= "Local da compra",
    hover_data= {"lat":False , "lon":False ,"Vendas":True , "Receita":False},
    title = "Vendas por Estado"
    )
    grafico_venda_estado.update_geos(
    showframe = False,
    showcoastlines = False,
    projection_type="equirectangular",
    bgcolor="rgba(0,0,0,0)"
    )

    return grafico_venda_estado

def avaliacao_compra(df):
    avaliação_compra = df.groupby("Avaliação da compra").size().reset_index()
    avaliação_compra.columns = ["Avaliação da compra" , "Avaliações"]

    substituições = {
        5:"Muito Satisfeito",
        4:"Satisfeito",
        3:"Neutro",
        2:"Insatisfeito",
        1:"Muito Insatisfeito"
    }

    cores = ['#4CAF50', '#8BC34A', '#F44336', "#FFC107", "#FF9800"]

    avaliação_compra["Avaliação da compra"] = avaliação_compra["Avaliação da compra"].replace(substituições)

    grafico_avaliação_compra = pl.pie(
        avaliação_compra,
        names="Avaliação da compra",
        values="Avaliações",
        title="Avaliações",
        color_discrete_sequence=cores
        
    )

    return grafico_avaliação_compra


def tipo_pagamento(df):
    venda_tipo_pagamento = df.groupby("Tipo de pagamento").size().reset_index()
    venda_tipo_pagamento.columns = ["Tipos de Pagamento" , "Vendas"]
    venda_tipo_pagamento = venda_tipo_pagamento.sort_values("Vendas" , ascending=False)

    substituições = {
    "cartao_credito":"Cartão de Crédito",
    "cartao_debito":"Cartão de Débito"
    }

    venda_tipo_pagamento["Tipos de Pagamento"] = venda_tipo_pagamento["Tipos de Pagamento"].replace(substituições)
    venda_tipo_pagamento["Tipos de Pagamento"] = venda_tipo_pagamento["Tipos de Pagamento"].str.capitalize()

    grafico_tipo_pagamento = pl.pie(
    venda_tipo_pagamento,
    names="Tipos de Pagamento",
    values="Vendas",
    title="Vendas por Tipo de Pagamento"
    )
    
    return grafico_tipo_pagamento

def grafico_venda_mensal(df):
       
    vendas_mensais = df_venda_rec_mensal(df)

    # gráfico de receita mensal
    grafico_mensal2 = pl.line(
        vendas_mensais,
        x = "Mês",
        y = "Vendas",
        markers = True,
        range_y= (0 , vendas_mensais.max()), #Isso define o intervalo do eixo y do gráfico. O intervalo é definido de 0 até o valor máximo da receita mensal no DataFrame receita_mensal. Isso garante que o eixo y comece do zero e vá até o máximo valor de receita mensal.
        color= "Ano",
        line_dash= "Ano",
        title="Vendas Mensais"
        
    )
    # titulo do eixo x e/ou y
    grafico_mensal2.update_layout(yaxis_title="Receita")
    #grafico_mensal.update_layout(xaxis_title="Mês")

    return grafico_mensal2
# # ======================================= Gráficos Vendedores ================================================

def grafico_rec_vendedor(df):

    rec_vendedores = df_rec_venda_vendedor(df)
    top_receita_vendedores = rec_vendedores.sort_values("Receita",ascending=False).head(5)
    # grafico  receita por vendedor
    grafico_receita_vendedor = pl.bar(
        top_receita_vendedores,
        x= "Preço",
        y= "Vendedor",
        text="Receita",
        orientation="h",
        title="5 Melhores Receitas por Vendedor"
    )
    grafico_receita_vendedor.update_layout(
        yaxis = dict(
            categoryorder = "total ascending"
        )
    )

    grafico_receita_vendedor.update_traces(marker_color="#2B5F82")

    return grafico_receita_vendedor



def grafico_venda_vendedor(df):
     
    venda_vendedor = df_rec_venda_vendedor(df)
    top_vendas_vendedores = venda_vendedor.sort_values("Venda", ascending=False).head(5)

    grafico_venda_vendedor = pl.bar(
    top_vendas_vendedores,
    x = "Venda",
    y= "Vendedor",
    text_auto=True,
    orientation="h",
    title="5 Melhores Vendas por Vendedor"
    # color_discrete_sequence=["#2B5F82"] # TROCAR COR DAS BARRAS
    )
    grafico_venda_vendedor.update_layout(
        yaxis = dict(
            categoryorder = "total ascending"
        )
    )
    grafico_venda_vendedor.update_traces(marker_color="#2B5F82")
    
    return grafico_venda_vendedor
