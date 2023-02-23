from dash import Input, Output, callback
from dotenv import load_dotenv
from dash import html, dcc, Input, Output, callback
from SQLConnection import connection
import visualisation as vis
import os

load_dotenv()

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
name = os.getenv("DB_NAME")

sql = connection(user, password, host, 5432, name)

@callback(
	Output(
		"artist_info",'children'
	),
	[
		Input(
			'filters', 'value'
		),
		Input(
			'view_select', 'value'
		),
	]
)
def update_artist_info(name, view):
	name = name.lower()
	view = view.lower()
	if name is None or view != 'artist':
		return []
	artist_info = sql.get_list(
	f"""
		SELECT * 
		FROM artist
		WHERE artist_name = '{name}'
	"""
	)[0]
	artist_works = sql.get_list(
	f"""
		SELECT COUNT(title) from artwork
		WHERE artist_id = {artist_info[0]}
	"""
	)[0][0]
	return [
		html.H1(artist_info[1]),
		html.H2("Nationality: " + artist_info[2]),
		html.H2("Gender: " + artist_info[3]),
		html.H2("Started: " + str(artist_info[4])),
		html.H2("Ended: " + str(artist_info[5]) if artist_info[5] != 0 else 'Ended: ----'),
		html.H2("Pieces: " + str(artist_works))
	]

@callback(
	Output(
		"filters",'options'
	),
	Output(
		"demos",'options'
	),
	[
		Input(
			'view_select', 'value'
		)
	]
)
def update_filters_dropdown(value:list):
	if value is None:
		return [], []
	if "artist" in value:
		names = [
			artist[0] for artist in sql.get_list(
				"""
					SELECT artist_name from artist
				"""
			)
		]
		cols = ['department', 'year']
		return names, cols
	elif "artwork" in value:
		cols = ['nationality', 'gender', 'year', 'department']
		return ['All'], cols

@callback(
	Output(
		"demo_figure",'figure'
	),
	[
		Input(
			'view_select', 'value'
		),
		Input(
			'filters', 'value'
		),
		Input(
			'demos', 'value'
		),
	]
)
def update_demo_fig(type, name, filter):
	if filter == 'year':
		filter = "year_completed"
	if "artist" in type:
		artist_id = sql.get_list(
			f"""
				SELECT * FROM artist where artist_name = '{name}'
			"""
		)[0][0]
		artworks = sql.get_df(
			f"""
				SELECT {filter}, COUNT({filter}) 
				FROM artwork 
				WHERE artist_id = {artist_id}
				GROUP BY {filter}
			"""
		)
		return vis.create_bar_graph(artworks, filter, 'count')
	elif "artwork" in type:
		if filter == 'year_completed' or filter == 'department':
			df = sql.get_df(f"SELECT {filter}, COUNT({filter}) FROM artwork GROUP BY {filter}")
			return vis.create_bar_graph(df, filter, 'count')
		df = sql.get_df(f"SELECT {filter}, COUNT({filter}) FROM artist GROUP BY {filter}")
		return vis.create_bar_graph(df, filter, 'count')

@callback(
	Output(
		"number_of_artists",'children'
	),
	Output(
		"number_of_artworks",'children'
	),
	[
		Input(
			'view_select', 'value'
		)
	]
)
def get_artwork_artist_totals(value):
	artworks = sql.get_list("""
		SELECT COUNT(title) FROM artwork
	""")[0][0]
	artists = sql.get_list("""
		SELECT COUNT(artist_id) FROM artist
	""")[0][0]
	return artists, artworks