from dotenv import load_dotenv
from dash import html, dcc, Input, Output, callback
import os
import plotly.express as px
import pandas as pd

def create_bar_graph(data:pd.DataFrame, x:str, y:str, **kwargs) -> px.bar:
    colour = kwargs.get('colour')
    title = kwargs.get('title')
    fig = px.bar(data, x, y, color=colour).update_layout(paper_bgcolor="#619B8A", plot_bgcolor='#619B8A', title=f'Pieces by {format_axes_labels(x)}')
    fig.update_xaxes(title_font=dict(color='#f0f8ff'), tickfont=dict(color='#f0f8ff'), title=format_axes_labels(x))
    fig.update_xaxes(gridcolor='#f0f8ff', zerolinecolor='#f0f8ff', zerolinewidth=3)
    fig.update_yaxes(title_font=dict(color='#f0f8ff'), tickfont=dict(color='#f0f8ff'), title=format_axes_labels(y))
    fig.update_yaxes(gridcolor='#f0f8ff', zerolinecolor='#f0f8ff', zerolinewidth=3)
    fig.update_layout(
        title={
            'x':0.5,
            'xanchor': 'center',
        },
        title_font_size=22,
        font_color='#f0f8ff'
	)
    return fig

def format_axes_labels(label: str) -> str:
	if '_' in label:
		label = label.split('_')
		new_label = []
		for word in label:
			word = word[0].upper()+word[1:]
			new_label.append(word)
		return " ".join(new_label)
	elif 'rpm' in label.lower():
		return label.upper()
	else:
		return label[0].upper()+label[1:]
	