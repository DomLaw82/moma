from dash import html, dcc, Input, Output, callback
from app import app
from pages import search, stats

app.layout = html.Div(
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
					html.H2("Total Number of Artwork")
				),
				html.Div(
					html.H2(id='number_of_artists')
				)
			]
		),
    html.Div(
			id="page_content"
		),
	],
  id='page'
)

page_references = {
	"/": app.layout,
	"/search": search.layout,
	"/stats": stats.layout
}

@callback(
	Output(
			component_id='page_content',
			component_property='children',
			),
	[Input(
			component_id='url',
			component_property='pathname',
			)]
)
def display_page(pathname: str) -> html.Div:
	if pathname in list(page_references.keys()):
		print(pathname)
		return page_references[pathname]
	else:
			return '404'