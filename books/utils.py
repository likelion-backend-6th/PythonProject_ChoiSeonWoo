from datetime import datetime
from time import sleep
from typing import List, Union

from books.models import Books, Loans
from books.validation import fetch_type_validation, search_type_validation, \
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


def fetch_books_list() -> List:
    message = "\n   희망하시는 조회 대상 도서 정보의 번호를 입력해주세요.\n" \
              "   [  1. 모든 도서  2. 현재 대출 가능한 도서  ]\n" \
              "   -->  번호 입력  :  "

    fetch_type = int(input(message))
    fetch_type = fetch_type_validation(fetch_type)

    if not fetch_type:
        fetch_books_list()

    if fetch_type == 1:
        books_list: List = Books().get()
        return change_isavailable(books_list)
    elif fetch_type == 2:
        books_list: List = Books().get(is_available=True)
        return change_isavailable(books_list) if books_list else "현재 모든 도서가 대출중입니다."


def search_book_list(book_lists) -> Union[List, str]:
    message1 = "\n   검색을 희망하는 항목에 대한 번호를 입력해주세요.\n" \
               "   [  1. ID  2. 제목  ]\n" \
               "   -->  번호 입력  :  "

    search_type_list = {1: "ID", 2: "제목"}

    search_type = int(input(message1))
    search_type = search_type_validation(search_type)

    if not search_type:
        search_book_list(book_lists)

    message2 = f"\n   도서의 {search_type_list[search_type]} 을/를 입력해주세요.\n" \
               f"   -->  {search_type_list[search_type]} 입력  :  "

    target = input(message2)

    if search_type == 1:
        result: List = list(filter(lambda x: x[0] == int(target), book_lists))
    elif search_type == 2:
        result: List = list(filter(lambda x: target in x[1], book_lists))

    result = result if result else f"해당 {search_type_list[search_type]} (으)로 검색한 도서는 존재하지 않습니다."

    return result


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