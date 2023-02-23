from dash import html, dcc, Input, Output, callback
from app import app
from pages import search, stats

layout = html.Div(
  children=[
    html.Div(
			children=[
				html.Div(
					dcc.Dropdown(
						options=["Gender","Nationality"],
						multi=True,
						id="artist_demos"
					)
				),
				html.Div(
					dcc.Graph(id="demo_figure")
				)
			]
		),
	]
)