from typing import List

import psycopg2
from psycopg2 import Error
import sys

from common import settings
from common.tables import TABLES, CREATE_QUERY_LISTS


class PostgreSQL:
    def __init__(self):
        self.connection = self.create_connection()
        self.cursor = self.connection.cursor()

    @staticmethod
    def create_connection():
        try:
            connection = psycopg2.connect(
                host=settings.POSTGRES_HOST,
                port=settings.POSTGRES_PORT,
                dbname=settings.POSTGRES_DBNAME,
                user=settings.POSTGRES_USER,
                password=settings.POSTGRES_PASSWORD
            )
            print(f"Database is connected")
            return connection
        except Error as e:
            print(f"Database Error '{e}' occured")
            sys.exit(1)

    def close(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Connection closed.")


class DatabaseManager:
    def __init__(self, table, query, db: PostgreSQL):
        self.table = table
        self.query = query
        self.db = db

    def execute_query(self):
        try:
            if type(self.query) == List:
                for q in self.query:
                    self.db.cursor.execute(q)
                    self.db.connection.commit()
            else:
                self.db.cursor.execute(self.query)
                self.db.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"ExecutionQueryError about {self.table}'{e} occured")

    def fetch_query(self):
        try:
            self.db.cursor.execute(self.query)
            result = self.db.cursor.fetchall()
            return result
        except Error as e:
            print(f"FetchQueryError about {self.table} '{e} occured")


postgres = PostgreSQL()
CREATE_TABLES = zip(TABLES, CREATE_QUERY_LISTS)
for table, create_query in CREATE_TABLES:
    DatabaseManager(table, create_query, postgres).execute_query()
postgres.close()

