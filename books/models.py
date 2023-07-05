from typing import Optional

from common.database import DatabaseManager


class Books:

    def __init__(
            self,
            title: Optional[str] = None,
            author: Optional[str] = None,
            publisher: Optional[str] = None,
            is_available: bool = True
    ):
        self.table = "books"
        self.title = title
        self.author = author
        self.publisher = publisher
        self.is_available = is_available

    def get(
            self,
            size: Optional[int] = None,
            id: Optional[int] = None,
            title: Optional[str] = None,
            author: Optional[str] = None,
            publisher: Optional[str] = None,
            is_available: Optional[bool] = None,
    ) -> object:
        if id is not None:
            query = f"SELECT * FROM books WHERE id = '{id}';"
            book = DatabaseManager(self.table, query).fetch_one()
            return book

        elif title is not None:
            query = f"SELECT * FROM books WHERE title LIKE '%{title}%';"
            books = DatabaseManager(self.table, query).fetch_all()
            return books

        elif author is not None:
            query = f"SELECT * FROM books WHERE author = '{author}';"
            books = DatabaseManager(self.table, query).fetch_all()
            return books

        elif publisher is not None:
            query = f"SELECT * FROM books WHERE publisher LIKE '%{publisher}%';"
            books = DatabaseManager(self.table, query).fetch_all()
            return books

        elif is_available is not None:
            query = f"SELECT * FROM books WHERE is_available = '{is_available}';"
            books = DatabaseManager(self.table, query).fetch_all()
            return books

        elif size is not None:
            query = f"SELECT * from books order by id limit {size};"
            books = DatabaseManager(self.table, query).fetch_many(size)
            return books

        else:
            query = f"SELECT * FROM books;"
            books = DatabaseManager(self.table, query).fetch_all()
            return books

    def post(self):
        query = f"""
        INSERT INTO books (title, author, publisher)
        VALUES ('{self.title}', '{self.author}', '{self.publisher}');
        """
        DatabaseManager(self.table, query).execute_query()

