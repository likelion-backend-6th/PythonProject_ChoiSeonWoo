from datetime import datetime
from typing import Optional, Tuple, List

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
            title_info: Optional[Tuple] = None,
            author_info: Optional[Tuple] = None,
            publisher_info: Optional[str] = None,
            is_available: Optional[bool] = None,
            order_by_info: Tuple = ("b.id", "ASC"),
            user_id: Optional[int] = None,
            recent_loan_only: bool = True,
    ) -> List:

        if recent_loan_only:
            join_table = f"(SELECT user_id, book_id, loan_date, return_date FROM loans l1 " \
                           "WHERE loan_date = (SELECT MAX(l2.loan_date) FROM loans l2 WHERE l1.book_id = l2.book_id))"
        else:
            join_table = "loans"

        query = f"SELECT b.*, l.loan_date, l.return_date FROM books b LEFT JOIN {join_table} l on b.id = l.book_id "
        extra_query = []

        if id or title_info or author_info or publisher_info or is_available is not None or user_id:
            if id:
                extra_query.append(f"b.id = {id}")
            if title_info:
                extra_query.append(f"b.title {title_info[1]} ILIKE '%{title_info[0]}%'")
            if author_info:
                extra_query.append(f"b.author {author_info[1]} ILIKE '%{author_info[0]}%'")
            if publisher_info:
                extra_query.append(f"b.publisher {publisher_info[1]} ILIKE '%{publisher_info[0]}%'")
            if is_available is not None:
                extra_query.append(f"b.is_available = '{is_available}'")
            if user_id:
                extra_query.append(f"l.user_id = {user_id}")

        extra_query = "WHERE " + " AND ".join(extra_query) if extra_query else ""
        if order_by_info:
            extra_query += f" ORDER BY {order_by_info[0]} {order_by_info[1]} NULLS LAST, b.id"
        else:
            extra_query = f" ORDER BY {order_by_info[0]} {order_by_info[1]}"

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
            loan_date: datetime = datetime.now(),
            return_date: Optional[datetime] = None
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
            loan_date_info: Optional[Tuple] = None,
            return_date_info: Optional[Tuple] = None,
            order_by_info: Tuple = ('id', 'DESC')
    ):
        query = "SELECT * FROM loans "
        extra_query = []

        if id or user_id or book_id or loan_date_info or return_date_info:
            if id:
                extra_query.append(f"id = '{id}'")
            if user_id:
                extra_query.append(f"user_id = '{user_id}'")
            if book_id:
                extra_query.append(f"book_id = '{book_id}'")
            if loan_date_info:
                extra_query.append(f"loan_date {loan_date_info[1]} '{loan_date_info[0]}'")
            if type(return_date_info) == Tuple:
                if return_date_info[1] and return_date_info[0] == "NULL":
                    extra_query.append(f"return_date is {return_date_info[0]}")
                elif type(return_date_info[0]) == datetime :
                    extra_query.append(f"return_date {return_date_info[1]} '{return_date_info[0]}'")

        extra_query = "WHERE " + " AND ".join(extra_query) if extra_query else ""

        if order_by_info:
            extra_query += f" ORDER BY {order_by_info[0]} {order_by_info[1]}"

        query += extra_query

        limit_query = f" LIMIT {size};" if size else ";"
        query += limit_query

        loans = DatabaseManager(self.table, query).fetch_all()

        return loans

    def post(self):
        query = f"""
                    INSERT INTO loans (user_id, book_id, loan_date, return_date)
                    VALUES ('{self.user_id}', '{self.book_id}', '{self.loan_date}'
                 """
        return_date_ = f", '{self.return_date}');" if self.return_date else ", NULL);"

        query += return_date_

        DatabaseManager(self.table, query).execute_query()

    def put(
            self,
            id: Optional[int] = None,
            user_id: Optional[int] = None,
            book_id: Optional[int] = None,
            loan_date: Optional[datetime] = None,
            return_date: Optional[datetime] = None,
            return_update: Optional[bool] = False,
            return_book_id: Optional[int] = None
    ):
        return_date_ = f"'{return_date}'" if return_date else "NULL"
        query = "UPDATE loans SET "
        extra_query = []

        if id:
            end_query = f" WHERE id = '{id}';"
        elif return_book_id:
            end_query = f" WHERE id = (SELECT id FROM loans WHERE book_id = {return_book_id} ORDER BY loan_date desc LIMIT 1);"

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
