import sqlalchemy
import psycopg2
import pandas as pd


class connection():
	"""
		Class for connecting to the database
	"""
	def __init__(self, username, password, host, port, name) -> None:
		self.engine = sqlalchemy.create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{name}")
		self.conn = self.engine.connect()
		

	def get_df(self, query:str, **kwargs) -> pd.DataFrame:
		"""
			Query the database

		Keyword Args:
				index_col (str): column of the table to use as the dataframe index

		Args:
				query (str): query string

		Returns:
				pd.DataFrame: containing queried data
		"""
		try:
			index_col = kwargs.get('index_col')
			query = sqlalchemy.text(query)
			df = pd.read_sql(query, self.conn, index_col=index_col)
			print(f"{query} executed")
			return df
		except Exception as e:
			print(e)

	def get_list(self, query:str) -> list[tuple]:
		"""
		Execute a query on the db

		Args:
				query (str): query string

		Returns:
				list[tuple]: list of tuples, each tuple representing a row of the result set
		"""
		query = sqlalchemy.text(query)
		try:
			res = self.conn.execute(query)
			res = res.fetchall()
			print(f"'{query}' executed")
			return res
		except Exception as e:
			print(e)