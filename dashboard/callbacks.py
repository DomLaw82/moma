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

# @callback(
# 	Output(
# 		"demo_figure",'figure'
# 	),
# 	[
# 		Input(
# 			'artist_demos', 'value'
# 		)
# 	]
# )
# def update_artist_figure(value:list):
# 	cols = ", ".join(value)
# 	if len(value) == 1 and 'Gender' in value:
# 		df = sql.get_df(f"SELECT gender, count(gender) FROM artist group by gender")
# 		return vis.create_bar_graph(df, "gender", 'count')
# 	elif len(value) == 1 and 'Gender' not in value:
# 		df = sql.get_df(f"SELECT nationality, count(nationality) FROM artist group by nationality")
# 		return vis.create_bar_graph(df, "nationality", 'count')
# 	else:
# 		df = sql.get_df(f"SELECT nationality, gender, count(gender) FROM artist group by nationality, gender")
# 		return vis.create_bar_graph(df, "nationality", 'count', colour='gender')
	

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
		print(cols)
		return names, cols
	# elif "artwork" in value:
	# 	names = [artist[0] for artist in sql.get_list("""
	# 		SELECT artist_name from artist
	# 	""")]
	# 	return names

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
	# elif "artwork" in value:
	# 	names = [artist[0] for artist in sql.get_list("""
	# 		SELECT artist_name from artist
	# 	""")]
	# 	return names