from dash import html, dcc, Input, Output, callback
from app import app

layout = html.Div(
  children=[
    html.Div(
			children=[
				html.H1('MoMA Data Bank', id='title'),
				html.Div(
					children=[
						html.Div(
							children=[
								html.Div(
									html.H2("Total Number of Artists")
								),
								html.Div(
									html.H2(id='number_of_artists')
								)
							],
							className='totals'
						),
						html.Div(
							children=[
								html.Div(
									html.H2("Total Number of Artworks")
								),
								html.Div(
									html.H2(id='number_of_artworks')
								)
							],
							className='totals'
						),
					],
					id='totals'
				),
			],
      id='header'
		),
		html.Div(
			children=[
				html.Div(
					children=[
						html.Div(
							dcc.Dropdown(
								options=["artist","artwork"],
								id="view_select",
								className="dropdown"
							)
						),
						html.Div(
							dcc.Dropdown(
								id="filters",
								className="dropdown"
							)
						),
						html.Div(
							dcc.Dropdown(
								id="demos",
								className="dropdown"
							)
						),
					],
          id="dropdowns"
				),
				html.Div(
					html.Div(id="artist_info")
				),
				html.Div(
					dcc.Graph(id="demo_figure")
				),
			]
		)
	],
  id='page'
)

app.layout = layout