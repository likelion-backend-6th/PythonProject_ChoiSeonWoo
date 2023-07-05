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


# 테스트 데이터 추가
# new_book = Books('테스트 타이틀', '테스트 저자', '테스트 출판사')
# new_book.post()


# 데이터 수정 테스트 진행
books = Books()

# 수정 전
print(" 수정 전 -----------------------")
print(books.get(id=14))
print()

# 수정 후
print(" 수정 후 -----------------------")
books.put(id=14)
print(books.get(id=14))
print("-------------------")
print()

books.put(14, "새타이틀", "새저자", "새출판사")
print(books.get(id=14))
print("-------------------")
print()

books.put(14, new_title="새타이틀2", new_publisher="새출판사2")
print(books.get(id=14))
print("-------------------")
print()

books.put(14, new_author="새저자3", new_publisher="새출판사3")
print(books.get(id=14))
print("-------------------")
print()

books.put(14, new_title="새타이틀4" ,new_author="새저자4")
print(books.get(id=14))
print("-------------------")
print()

books.put(14, new_title="새타이틀5")
print(books.get(id=14))
print("-------------------")
print()

books.put(14, new_author="새저자5")
print(books.get(id=14))
print("-------------------")
print()

books.put(14, new_author="새저자5")
print(books.get(id=14))
print("-------------------")