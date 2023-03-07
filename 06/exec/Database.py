import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import (
	create_engine,
	MetaData, Table, Column, String, Integer, Float, Boolean
)

class Database:
	def create_database(self):
		# Connect with postgres
		connection = psycopg2.connect(user="msalena", password="12345")
		connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

		# Cursor for executing operations with DB
		cursor = connection.cursor()
		# Create DB
		sql_create_database = cursor.execute('create database ft_db')
		# Close connection
		cursor.close()
		connection.close()


	def create_engine(self):
		engine = create_engine(
			"postgresql+psycopg2://msalena:12345@localhost/ft_db"
		)
		engine.connect()
		print(engine)


	def create_table(self, data):
		# Create metadata with all information about table
		metadata = MetaData()

		ships = Table("ships", metadata,
			Column()
		)


if __name__ == "__main__":
	db = Database()
	db.create_database()
	db.create_engine()
