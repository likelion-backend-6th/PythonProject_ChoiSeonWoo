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


# 전체 책 데이터 조회
print("전체 책 데이터 조회")
books = Books()
all_books = books.get()
print(f"all_books: {all_books}")
assert len(all_books) == 12, "조회한 전체 책 데이터 수가 일치하지 않습니다."

print()

# id 오름차순 기준 5개의 책 데이터 조회
print("id 오름차순 기준 5개의 책 데이터 조회")
multiple_books = books.get(5)
print(f"multiple_books: {multiple_books}")
assert [book[0] for book in multiple_books] == [1, 2, 3, 4, 5], "조회한 5개의 책 데이터가 잘못되었습니다."

print()

# 3번 id의 책 데이터 조회
print("3번 id의 책 데이터 조회")
id_filtered_book = books.get(id=3)
print(f"3번 id의 책: {id_filtered_book}")
assert id_filtered_book[0] == 3, "id로 조회한 책 데이터가 잘못되었습니다."

print()

# 제목에 '파이썬'이 들어가는 책 데이터 조회
print("제목에 '파이썬'이 들어가는 책 데이터 조회")
title_filtered_books = books.get(title="파이썬")
print(f"제목에 '파이썬'이 들어가는 책: {title_filtered_books}")
assert {'파이썬' in book[1] for book in title_filtered_books} == {True}, "제목으로 조회한 책 데이터가 잘못되었습니다."

print()

# '홍길동'님이 집필한 책 데이터 조회
print("'홍길동'님이 집필한 책 데이터 조회")
author_filtered_books = books.get(author="홍길동")
print(f"홍길동 저자의 책: {author_filtered_books}")
assert {'홍길동' in book[2] for book in author_filtered_books} == {True}, "저자로 조회한 책 데이터가 잘못되었습니다."

print()

# 출판사명에 "한빛'이 들어가는 책 데이터 조횣
print("출판사명에 '한빛'이 들어가는 책 데이터 조회")
publisher_filtered_books = books.get(publisher="한빛")
print(f"한빛 출판사의 책: {publisher_filtered_books}")
assert {'한빛' in book[3] for book in publisher_filtered_books} == {True}, " 출판사명으로 조회한 책 데이터가 잘못되었습니다."

print()

# 대여 가능한 책 데이터 조회
print("대여 가능한 책 데이터 조회")
available_books = books.get(is_available=True)
print(f"대여 가능한 책: {available_books}")
assert {book[4] == True for book in available_books} == {True}, "대여 가능으로 조회한 책 데이터가 잘못되었습니다."
