from datetime import datetime
from time import sleep
from typing import List, Union

from books.models import Books, Loans
from books.validation import FETCH_TYPE_MESSAGE, SEARCH_TYPE_MESSAGE, type_validation, search_validation, \
    loan_book_ids_validation, return_book_ids_validation


def change_isavailable(books_list: List) -> List:
    result = []
    for book in books_list:
        if book[4] == True:
            book = book[:4] + ('대여가능',) + book[5:]
        else:
            book = book[:4] + ('대여중',) + book[5:]
        result.append(book)
    return result


def restore_isavailable(books_list: List) -> List:
    result = []
    for book in books_list:
        if book[4] == '대여가능':
            book = book[:4] + (True,) + book[5:]
        else:
            book = book[:4] + (False,) + book[5:]
        result.append(book)
    return result


def fetch_books_list() -> Union[List, str]:
    while True:
        fetch_type = type_validation(FETCH_TYPE_MESSAGE)
        if fetch_type:
            break

    if fetch_type == 1:
        books_list: List = Books().get()
        return change_isavailable(books_list)
    elif fetch_type == 2:
        books_list: List = Books().get(is_available=True)
        return change_isavailable(books_list) if books_list else "현재 모든 도서가 대출중입니다."


def search_book_list(book_list: List) -> List:
    while True:
        search_type = type_validation(SEARCH_TYPE_MESSAGE)
        if search_type:
            break

    book_list = search_validation(search_type, book_list)

    return change_isavailable(book_list)


def loan_books(user_id: int) -> List:

    book_id_list = loan_book_ids_validation()

    if not book_id_list:
        return []

    for book_id in book_id_list:
        target_book = Books().put(id=book_id)
        new_loan = Loans(user_id, book_id).post()

    return Books().get(user_id=user_id, is_available=False, order_by_info=('l.loan_date', "DESC"))


def return_books(user_id: int) -> List:

    book_id_list = return_book_ids_validation(user_id)

    if not book_id_list:
        return []

    for book_id in book_id_list:
        target_book = Books().put(id=book_id)
        update_return = Loans().put(return_date=datetime.now(), return_update=True, return_book_id=book_id)

    return [Books().get(id=book_id)[0] for book_id in book_id_list]