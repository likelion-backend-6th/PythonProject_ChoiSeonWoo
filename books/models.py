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


# 현재 책 데이터 조회
print("전체 책 데이터 조회")
books = Books()
now_all_books = books.get()
print(f"현재 책 데이터: {now_all_books}")
now_all_books_count = len(now_all_books)

# books 데이터 추가
new_book = Books('파이썬 CCC', '최모씨', '시공사')
new_book.post()

# 새로 책 데이터 조회
new_all_books = new_book.get()
print(f"새로 조회한 책 데이터: {new_all_books}")
new_all_books_count = len(new_all_books)

print(f"이전 책 데이터의 수는 {now_all_books_count}개였으며, 현재 책 데이터 수는 {new_all_books_count}개 입니다. ")

# 책 권수가 정상적으로 증가하였는지 확인
assert new_all_books_count == now_all_books_count + 1, "요청한 책 데이터가 정상적으로 생성되지 않았습니다."
