import os
import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv
from prettytable import from_db_cursor

load_dotenv(dotenv_path="./secrets/.env")


class PostGreSQL:
    def __init__(self):
        self.host = os.getenv("PSQL_HOST")
        self.db_name = os.getenv("PSQL_DATABASE")
        self.user = os.getenv("PSQL_USER")
        self.password = os.getenv("PSQL_PASS")

    def connect(self):
        # Construct connection string
        try:
            # Connect to an existing database
            connection = psycopg2.connect(user=self.user, password=self.password,
                                          host=self.host, port="5432", database=self.db_name, sslmode='require')
            # Create a cursor to perform database operations
            #cursor = connection.cursor()

            # Print PostgreSQL details
            print("Connected to the database")
            return connection
        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def create_table_score(self, table_name: str):
        conn = self.connect()
        cursor = conn.cursor()
        SQL_QUERY = """CREATE TABLE IF NOT EXISTS {0} (
        id_score SERIAL PRIMARY KEY,
        name VARCHAR(250) UNIQUE,
        score INT) ;""".format(table_name)
        cursor.execute(SQL_QUERY)
        conn.commit()
        cursor.close()
        conn.close()
        print("Table " + table_name + " created")

    def select(self, table: str):
        conn = self.connect()
        cursor = conn.cursor()
        # Fetch all rows from table
        cursor.execute(f"SELECT * FROM {table}")
        rows = cursor.fetchall()
        # Print all rows
        for row in rows:
            print(row)
        cursor.close()
        conn.close()
        return rows

    def insert(self, table: str, data: list):
        conn = self.connect()
        c = conn.cursor()
        if data != "":
            query = f"INSERT INTO {table} (name, score) VALUES (%s, %s);"
            new_data = (data[0], data[1])
            c.execute(query, new_data)
            conn.commit()
            c.close()
            conn.close()
