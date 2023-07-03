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
