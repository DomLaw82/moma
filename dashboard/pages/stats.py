from dash import html, dcc, Input, Output, callback
from app import app
from pages import search, stats

layout = html.Div(
  children=[
		html.Div(
			children=[
				dcc.Link(
					children=[
						html.Button(
							children="Search"
						)
					
					]
				),
				dcc.Link(
					children=[
						html.Button(
							children="Stats"
						)
					]
				)
			]
		),
    html.Div(
			children=[
				html.Div(
					dcc.Dropdown(
						options=["Gender", "Age", "Nationality"],
						multi=True,
						id="artist_demos"
					)
				),
				html.Div(
					dcc.Graph(id="demo_figure")
				)
			]
		)
	]
)