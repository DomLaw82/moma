from dash import html, dcc, Input, Output, callback
from app import app
from pages import search, stats

layout = html.Div(
  children=[
    html.Div(
			children=[
				html.H1('MoMA Data Bank'),
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

# page_references = {
# 	"/home": layout,
# 	"/search": search.layout,
# 	"/stats": stats.layout
# }

# @callback(
# 	Output(
# 			component_id='page_content',
# 			component_property='children',
# 			),
# 	[Input(
# 			component_id='url',
# 			component_property='pathname',
# 			)]
# )
# def display_page(pathname: str) -> html.Div:
# 	if pathname in list(page_references.keys()):
# 		print(pathname)
# 		return page_references[pathname]
# 	else:
# 			return '404'