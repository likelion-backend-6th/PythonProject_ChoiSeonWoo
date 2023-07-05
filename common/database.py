from typing import List, Optional, Union

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
            print("Connection closed")


class DatabaseManager:
    def __init__(self, db: PostgreSQL, table_: str, query: Optional[Union[str, List[str]]]):
        self.db = db
        self.table = table_
        self.query = query

    def execute_query(self):
        try:
            if type(self.query) == List:
                for q in self.query:
                    self.db.cursor.execute(q)
                    self.db.connection.commit()
            elif type(self.query) == str:
                self.db.cursor.execute(self.query)
                self.db.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"ExecutionQueryError about {self.table}'{e} occured")

    def fetch_all(self):
        try:
            self.db.cursor.execute(self.query)
            result = self.db.cursor.fetchall()
            print("All Data fetched Successfully")
            return result
        except Error as e:
            print(f"FetchQueryError about {self.table} '{e} occured")

    def fetch_many(self, size: int):
        try:
            self.db.cursor.execute(self.query)
            result = self.db.cursor.fetchmany(size)
            print("Multiple Data fetched Successfully")
            return result
        except Error as e:
            print(f"FetchQueryError about {self.table} '{e} occured")

    def fetch_one(self):
        try:
            self.db.cursor.execute(self.query)
            result = self.db.cursor.fetchone()
            print("Single Data fetched Successfully")
            return result
        except Error as e:
            print(f"FetchQueryError about {self.table} '{e} occured")


postgres = PostgreSQL()


# postgres = PostgreSQL()
# CREATE_TABLES = zip(TABLES, CREATE_QUERY_LISTS)
# for table, create_query in CREATE_TABLES:
#     DatabaseManager(postgres, table, create_query).execute_query()
# postgres.close()
#
