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
		"demo_figure",'figure'
	),
	[
		Input(
			'artist_demos', 'value'
		)
	]
)
def update_artist_figure(value:list):
	cols = ", ".join(value)
	if len(value) == 1 and 'Gender' in value:
		df = sql.get_df(f"SELECT gender, count(gender) FROM artist group by gender")
		return vis.create_bar_graph(df, "gender", 'count')
	elif len(value) == 1 and 'Gender' not in value:
		df = sql.get_df(f"SELECT nationality, count(nationality) FROM artist group by nationality")
		return vis.create_bar_graph(df, "nationality", 'count')
	else:
		df = sql.get_df(f"SELECT nationality, gender, count(gender) FROM artist group by nationality, gender")
		return vis.create_bar_graph(df, "nationality", 'count', colour='gender')