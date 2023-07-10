from datetime import datetime
from time import sleep
from typing import List, Union, Optional

from books.models import Books, Loans
from books.validation import FETCH_TYPE_MESSAGE, SEARCH_TYPE_MESSAGE, type_validation, search_validation, \
    loan_book_ids_validation, return_book_ids_validation


def change_isavailable(books_list: List) -> List:
    result = []
    for book in books_list:
        if type(book[4] == bool):
            if book[4]:
                book = book[:4] + ('대여가능',) + ('', '')
            elif not book[4]:
                loan_date = book[5].strftime("%Y년 %m월 %d일") if book[5] else ''
                return_date = book[6].strftime("%Y년 %m월 %d일") if book[6] else ''
                book = book[:4] + ('대여중',) + (loan_date, return_date)

            result.append(book)

    return result if result else books_list


def fetch_books_list() -> List | str | bool:
    print("\n   =========           도서 조회를 진행합니다.          =========\n")
    fetch_type = type_validation(FETCH_TYPE_MESSAGE)

    if fetch_type == 1:
        books_list: List = Books().get()
        return change_isavailable(books_list)

    elif fetch_type == 2:
        books_list: List = Books().get(is_available=True)

        return change_isavailable(books_list) if books_list else "현재 모든 도서가 대출중입니다."
    elif fetch_type == -1:
        return -1


def search_book_list(book_list: Optional[List] = None) -> List | bool:
    print("\n   =========           도서 검색를 진행합니다.          =========\n")
    book_list = book_list if book_list else fetch_books_list()

    if book_list == -1:
        return -1

    print("\n   지정하신 도서를 대상으로 검색을 진행합니다.")

    search_type = type_validation(SEARCH_TYPE_MESSAGE)
    if search_type == -1:
        return -1

    book_list = search_validation(search_type, book_list)

    return change_isavailable(book_list) if book_list != -1 else False


def loan_books(user_id: int) -> List | bool:
    print("\n   =========           도서 대여를 진행합니다.          =========\n")
    book_id_list = loan_book_ids_validation()

    if book_id_list == -1:
        return False

    elif not book_id_list:
        return []

    else:
        for book_id in book_id_list:
            target_book = Books().put(id=book_id)
            new_loan = Loans(user_id, book_id).post()

    return change_isavailable(Books().get(user_id=user_id, is_available=False, order_by_info=('l.loan_date', "DESC")))


def return_books(user_id: int) -> List | bool:
    print("\n   =========           도서 반납을 진행합니다.          =========\n")
    book_id_list = return_book_ids_validation(user_id)

    if book_id_list == -1:
        return False

    elif not book_id_list:
        return []

    else:
        for book_id in book_id_list:
            target_book = Books().put(id=book_id)
            update_return = Loans().put(return_date=datetime.now(), return_update=True, return_book_id=book_id)

    return change_isavailable(Books().get(user_id=user_id, is_available=False, order_by_info=('l.loan_date', "DESC")))
