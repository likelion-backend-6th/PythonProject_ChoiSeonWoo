from datetime import datetime
from time import sleep
from typing import List, Union, Optional

from tabulate import tabulate

from books.models import Books, Loans
from books.validation import FETCH_TYPE_MESSAGE, SEARCH_TYPE_MESSAGE, type_validation, search_validation, \
    loan_book_ids_validation, return_book_ids_validation
from common.validation import bool_validation, SEARCH_LOANABLE_MESSAGE
from users.models import Users


def change_book_list(book_list: List, func_type: int) -> List:
    func_type_info = {1: "도서 정보", 2: " 대출일자 포함", 3: "전체"}

    result = []
    if not book_list:
            book_list = [[" - "] * 6]

    for book in book_list:
        if type(book[4]) == bool:
            if book[4]:
                book = list(book[:4]) + ["대여가능", " - ", " - "]
            elif not book[4]:
                loan_date = book[5].strftime("%Y년 %m월 %d일") if book[5] else ' - '
                return_date = book[6].strftime("%Y년 %m월 %d일") if book[6] else ' - '
                book = list(book[:4]) + ["대여중", loan_date, return_date]

        if func_type == 1:
            book = book[:4]
        elif func_type == 2:
            book = book[:6]
        elif func_type == 3:
            book = book

        result.append(book)

    return result if result else book_list


def change_loan_list(loan_list: List) -> List:
    result = []
    if not loan_list:
        loan_list = [[" - "] * 5]

    for loan in loan_list:
        if type(loan[3] == datetime):
            loan_date = loan[3].strftime("%Y년 %m월 %d일 %H시 %M분")
            return_date = loan[4].strftime("%Y년 %m월 %d일") if loan[4] else ''
            loan = list(loan[:3]) + [loan_date, return_date]

            result.append(loan)

    return result if result else loan_list


def render_table(data, table_name):
    headers = []
    if table_name =="users":
        headers = ["No.", "ID", "사용자명", "성함"]
    elif table_name =="books":
        headers = ["NO.", "ID", "제목", "저자", "출판사", "대출가능여부", "대출일"]
        headers = headers[:len(data[0])+1]
    elif table_name == "loans":
        headers = ["NO.", "ID", "사용자 ID", "도서 ID", "대출일", "반납일"]

    table = tabulate(data, headers=headers, tablefmt="fancy_grid",
                     showindex=True, numalign='center', stralign='left', maxcolwidths=30)
    table_lines = table.split("\n")
    table_lines_modified = ["   " + line for line in table_lines]
    table = "\n".join(table_lines_modified)

    return table


def fetch_book_list() -> List | int:
    print("\n   =========           도서 조회를 진행합니다.          =========")
    fetch_type = type_validation(FETCH_TYPE_MESSAGE)

    if fetch_type == -1:
        return -1

    elif fetch_type == 1:
        book_list: List = Books().get()

    elif fetch_type == 2:
        book_list: List = Books().get(is_available=True)

    if not book_list:
        print("\n   현재 모든 도서가 대출중입니다.\n")

    func_type = 2 if fetch_type == 1 else 1
    print("\n   [조회 결과]")
    print(render_table(change_book_list(book_list, func_type), "books"))

    return [book_list, func_type] if book_list else -1


def search_book_list(book_list: Optional[List] = None) -> List | int:
    print("\n   =========           도서 검색를 진행합니다.          =========\n")

    if book_list:
        book_list, func_type = book_list, 2
        render_table_title = "\n   [대상 도서]"
        print(render_table_title)
        print(render_table(change_book_list(book_list, func_type), "books"))
    else:
        book_check = bool_validation(SEARCH_LOANABLE_MESSAGE)
        if book_check:
            book_list = Books().get(is_available=True)
            print("\n   현재 대출 가능한 도서 목록입니다.")
            print(render_table(change_book_list(book_list, 1), 'books'))
        elif book_check is None:
            return -1

    search_type = type_validation(SEARCH_TYPE_MESSAGE)
    if search_type == -1:
        return -1

    book_list = search_validation(search_type, book_list)

    print("\n   [검색 결과]")
    print(render_table(change_book_list(book_list, func_type), "books"))

    return book_list if book_list != -1 else -1


def loan_books(user_id: int) -> List | int:
    print("\n   =========           도서 대여를 진행합니다.          =========\n")

    book_check = bool_validation(SEARCH_LOANABLE_MESSAGE)
    if book_check:
        print("\n   현재 대출 가능한 도서 목록입니다.")
        print(render_table(change_book_list(Books().get(is_available=True), 1), 'books'))
    elif book_check is None:
        return -1

    book_id_list = loan_book_ids_validation()

    if book_id_list == -1:
        return -1

    elif not book_id_list:
        return []

    else:
        for book_id in book_id_list:
            target_book = Books().put(id=book_id)
            new_loan = Loans(user_id, book_id).post()

    current_loan_books = Books().get(user_id=user_id, is_available=False, order_by_info=('l.loan_date', "DESC"))

    print("\n   대출이 정상적으로 완료되었습니다.")

    print("\n   현재 대출 중인 도서의 목록입니다.")
    print(render_table(change_book_list(current_loan_books, 2), 'books'))

    return current_loan_books


def return_books(user_id: int) -> List | int:
    print("\n   =========           도서 반납을 진행합니다.          =========\n")

    retunable_book_list = Books().get(user_id=user_id, is_available=False, order_by_info=('l.loan_date', "DESC"))
    username = Users().get(id=user_id)[0][1]

    if not retunable_book_list:
        print(f"   {username} 님의 반납 가능한 도서가 존재하지 않습니다.\n")
        return -1

    print(f"\n   {username} 님의 반납 가능한 도서 목록입니다.")
    print(render_table(change_book_list(retunable_book_list, 2), 'books'))

    book_id_list = return_book_ids_validation(user_id, retunable_book_list)

    if book_id_list == -1:
        return -1

    else:
        for book_id in book_id_list:
            target_book = Books().put(id=book_id)
            update_return = Loans().put(return_date=datetime.now(), return_update=True, return_book_id=book_id)

    current_loan_books = Books().get(user_id=user_id, is_available=False, order_by_info=('l.loan_date', "DESC"))

    print("\n   반납이 정상적으로 완료되었습니다.")

    print("\n   현재 대출 중인 도서의 목록입니다.")
    print(render_table(change_book_list(current_loan_books, 2), 'books'))

    return current_loan_books