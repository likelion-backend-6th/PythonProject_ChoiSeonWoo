from datetime import datetime
from typing import Optional, Union, Tuple

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
            order_by: Optional[Tuple] = None,
    ):
        query = "SELECT * FROM books "
        extra_query = []

        if id or title or author or publisher or is_available:
            if id:
                extra_query.append(f"id = '{id}'")
            if title:
                extra_query.append(f"title LIKE '%{title}%'")
            if author:
                extra_query.append(f"author = '{author}'")
            if publisher:
                extra_query = f"publisher LIKE '%{publisher}%'"
            if is_available:
                extra_query = f"is_available = '{is_available}'"

        extra_query = "WHERE " + ", ".join(extra_query) if extra_query else ""

        if order_by:
            extra_query += "WHERE " f" ORDER BY {order_by[0]} {order_by[1]}"

        query += extra_query

        limit_query = f" LIMIT {size};" if size else ";"
        query += limit_query

        books = DatabaseManager(self.table, query).fetch_all()

        return books

    def post(self):
        query = f"""
        INSERT INTO books (title, author, publisher)
        VALUES ('{self.title}', '{self.author}', '{self.publisher}');
        """
        DatabaseManager(self.table, query).execute_query()

    def put(
            self,
            id: int,
            new_title: Optional[str] = None,
            new_author: Optional[str] = None,
            new_publisher: Optional[str] = None,
    ):
        query = "UPDATE books SET "
        end_query = f" WHERE id = '{id}';"

        if new_title or new_author or new_publisher:
            extra_query = []
            if new_title:
                extra_query.append(f"title = '{new_title}'")
            if new_author:
                extra_query.append(f"author = '{new_author}'")
            if new_publisher:
                extra_query.append(f"publisher = '{new_publisher}'")
            query += ', '.join(extra_query) + end_query
        else:
            change_isavailable = "is_available = NOT is_available"
            query += change_isavailable + end_query

        DatabaseManager(self.table, query).execute_query()

    def handle_complex_query(
            self,
            query: str,
            handle_type: str
    ):
        if handle_type == "get":
            result = DatabaseManager(self.table, query).fetch_all()
        elif handle_type == "post" or "put":
            result = DatabaseManager(self.table, query).execute_query()
        print(f"'{handle_type}' Request was processed Successfully")
        return result


class Loans:

    def __init__(
            self,
            user_id: Optional[int] = None,
            book_id: Optional[int] = None,
            loan_date: Optional[datetime] = None,
            return_date: Optional[datetime] = None,
    ):
        self.table = "loans"
        self.user_id = user_id
        self.book_id = book_id
        self.loan_date = loan_date
        self.return_date = return_date

    def get(
            self,
            size: Optional[int] = None,
            id: Optional[int] = None,
            user_id: Optional[int] = None,
            book_id: Optional[int] = None,
            date: Optional[datetime] = None,
            today: Optional[datetime] = None,
    ):
        query = "SELECT * FROM loans "
        end_query = " ORDER BY id DESC"
        extra_query = []

        if id or user_id or book_id or date or today:
            if id:
                extra_query.append(f"id = '{id}'")
            if user_id:
                extra_query.append(f"user_id = '{user_id}'")
            if book_id:
                extra_query.append(f"book_id = '{book_id}'")
            if date:
                extra_query = f"WHERE loan_date < '{date}'"
            if today:
                extra_query = f"WHERE return_date < '{today}'"

        extra_query = "WHERE " + ", ".join(extra_query) if extra_query else ""
        query += extra_query + end_query

        limit_query = f" LIMIT {size}" if size else ";"
        query += limit_query

        loans = DatabaseManager(self.table, query).fetch_all()

        return loans if not id else loans[0]

    def post(self):
        return_date = f"'{self.return_date}'" if self.return_date else "NULL"
        query = f"""
        INSERT INTO loans (user_id, book_id, loan_date, return_date)
        VALUES ('{self.user_id}', '{self.book_id}', '{self.loan_date}', {return_date});
        """
        DatabaseManager(self.table, query).execute_query()
        Books().put(id=self.book_id)

    def put(
            self,
            id: int,
            user_id: Optional[int] = None,
            book_id: Optional[int] = None,
            loan_date: Optional[datetime] = None,
            return_date: Optional[datetime] = None,
            return_update: Optional[bool] = False,
    ):
        return_date_ = f"'{return_date}'" if return_date else "NULL"
        query = "UPDATE loans SET "
        end_query = f" WHERE id = '{id}';"
        extra_query = []

        if user_id:
            extra_query.append(f"user_id = '{user_id}'")
        if book_id:
            extra_query.append(f"book_id = '{book_id}'")
        if loan_date:
            extra_query.append(f"loan_date = '{loan_date}'")
        if return_update:
            extra_query.append(f"return_date = {return_date_}")

        query += ', '.join(extra_query) + end_query
        DatabaseManager(self.table, query).execute_query()

    def handle_complex_query(
            self,
            query: str,
            handle_type: str
    ):
        if handle_type == "get":
            result = DatabaseManager(self.table, query).fetch_all()
        elif handle_type == "post" or "put":
            result = DatabaseManager(self.table, query).execute_query()
        print(f"'{handle_type}' Request was processed Successfully")
        return result
