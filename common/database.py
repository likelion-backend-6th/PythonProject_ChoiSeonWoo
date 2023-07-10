from typing import List, Optional, Union

import psycopg2
from psycopg2 import Error
import sys

from common import settings


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
            print(f"Database is connected") if settings.DEBUG else None
            return connection
        except Error as e:
            print(f"Database Error '{e}' occured") if settings.DEBUG else None
            sys.exit(1)

    def close(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Connection closed") if settings.DEBUG else None


class DatabaseManager:
    def __init__(self, table_: str, query: Optional[Union[str, List[str]]]):
        self.db = PostgreSQL()
        self.table = table_
        self.query = query
        print(f"\n쿼리문: {self.query}\n") if settings.DEBUG else None

    def execute_query(self):
        try:
            if type(self.query) == List:
                for q in self.query:
                    self.db.cursor.execute(q)
                    self.db.connection.commit()
            elif type(self.query) == str:
                self.db.cursor.execute(self.query)
                self.db.connection.commit()
            print("\nQuery executed successfully\n") if settings.DEBUG else None
        except Error as e:
            print(f"\nExecutionQueryError about {self.table}'{e} occured\n") if settings.DEBUG else None
        else:
            self.db.close()

    def fetch_all(self):
        try:
            self.db.cursor.execute(self.query)
            result = self.db.cursor.fetchall()
            print("\nAll Data fetched Successfully\n") if settings.DEBUG else None
            return result
        except Error as e:
            print(f"\nFetchQueryError about {self.table} '{e} occured\n") if settings.DEBUG else None
        finally:
            self.db.close()

    def fetch_many(self, size: int):
        try:
            self.db.cursor.execute(self.query)
            result = self.db.cursor.fetchmany(size)
            print("\nMultiple Data fetched Successfully\n")
            return result
        except Error as e:
            print(f"\nFetchQueryError about {self.table} '{e} occured\n") if settings.DEBUG else None
        finally:
            self.db.close()

    def fetch_one(self):
        try:
            self.db.cursor.execute(self.query)
            result = self.db.cursor.fetchone()
            print("\nSingle Data fetched Successfully\n") if settings.DEBUG else None
            return result
        except Error as e:
            print(f"\nFetchQueryError about {self.table} '{e} occured\n") if settings.DEBUG else None
        finally:
            self.db.close()
