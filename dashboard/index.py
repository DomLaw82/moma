from dash import html, dcc, Input, Output, callback
from app import app
from pages import search, stats

layout = html.Div(
  children=[
		html.Header(
			children=[
				dcc.Location(
					id='url',
					refresh=False,
				),
			]
		),
		html.Div(
			children=[
				dcc.Link(
					children=[
						html.Button(
							children="Home",
							className='nav_button'
						)
					],
					href="./"
				),
				dcc.Link(
					children=[
						html.Button(
							children="Search",
							className='nav_button'
						)
					],
					href="./search"
				),
				dcc.Link(
					children=[
						html.Button(
							children="Stats",
							className='nav_button'
						)
					],
					href="./stats"
				)
			],
			id='nav_bar'
		),
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
					]
				),
				html.Div(
					children=[
						html.Div(
							html.H2("Total Number of Artworks")
						),
						html.Div(
							html.H2(id='number_of_artworks')
						)
					]
				),
			]
		),
		html.Div(
			children=[
				html.Div(
					children=[
						html.Div(
							dcc.Dropdown(
								options=["Artist","Artwork"],
								multi=True,
								id="view_select"
							)
						),
						html.Div(
							dcc.Dropdown(
								multi=True,
								id="demos"
							)
						),
					],
          id="dropdowns"
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