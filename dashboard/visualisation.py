from dotenv import load_dotenv
from dash import html, dcc, Input, Output, callback
import os
import plotly.express as px
import pandas as pd

def create_bar_graph(data:pd.DataFrame, x:str, y:str, **kwargs) -> px.bar:
    colour = kwargs.get('colour')
    fig = px.bar(data, x, y, color=colour)
    return fig