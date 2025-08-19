import pandas as pd
import plotly.express as px
import plotly.io as pio
import numpy as np

def criar_grafico_barras(df, coluna_x,coluna_y,titulo = ""):
    fig = px.bar(
        data_frame= df,
        x= coluna_x,
        y= coluna_y,
        title= titulo,
        text= coluna_y
    )

    fig.show()

def criar_grafico_linhas(df, coluna_x,coluna_y,titulo = ""):
    fig = px.line(
        data_frame= df,
        x= coluna_x,
        y= coluna_y,
        title= titulo,
        text= coluna_y
    )

    fig.update_traces(textposition= "bottom right")

    fig.show()
