from dotenv import load_dotenv
from SQLConnection import connection
import os

load_dotenv()

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
name = os.getenv("DB_NAME")

sql = connection(user, password, host, 5432, name)

print(sql.get_list("""
		SELECT * FROM artwork
	""")
)