from datetime import datetime
from typing import List, Optional, Tuple

from books.models import Books, Loans
from books.validation import FETCH_TYPE, FETCH_TYPE_MESSAGE, SEARCH_TYPE, SEARCH_TYPE_MESSAGE, \
    type_validation, search_validation, loan_book_ids_validation, return_book_ids_validation, \
    name_validation, datetime_validation
from common.core import render_table
from common.validation import SEARCH_LOANABLE_MESSAGE, bool_validation, existed_id_validation
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
            return_date = loan[4].strftime("%Y년 %m월 %d일 %H시 %M분") if loan[4] else ' - '
            loan = list(loan[:3]) + [loan_date, return_date]

            result.append(loan)

    return result if result else loan_list


def fetch_book_list(user: Optional[Tuple] = None) -> List | int:
    print("\n   =========           도서 조회를 진행합니다.          =========")
    fetch_type = type_validation(FETCH_TYPE, FETCH_TYPE_MESSAGE)

    if fetch_type == -1:
        return -1

    elif fetch_type == 1:
        book_list: List = Books().get()

    elif fetch_type == 2:
        book_list: List = Books().get(is_available=True)

        if not book_list:
            print("\n   현재 모든 도서가 대출중입니다.\n")

    elif fetch_type == 3:
        book_list: List = Books().get(user_id=user[0], is_available=False, order_by_info=('loan_date', 'DESC'))

    func_type = 1 if fetch_type == 2 else 2

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
            book_list, func_type = Books().get(is_available=True), 1
            print("\n   현재 대출 가능한 도서 목록입니다.")
            print(render_table(change_book_list(book_list, 1), 'books'))
        elif not book_check:
            book_list, func_type = Books().get(), 2
        elif book_check is None:
            return -1

    search_type = type_validation(SEARCH_TYPE, SEARCH_TYPE_MESSAGE)
    if search_type == -1:
        return -1

    book_list = search_validation(search_type, book_list)
    if book_list == -1:
        return -1

    print("\n   [검색 결과]")
    print(render_table(change_book_list(book_list, func_type), "books"))

    return book_list if book_list != -1 else -1


def loan_books(user: Tuple) -> List | int:
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
            new_loan = Loans(user[0], book_id).post()

    current_loan_books = Books().get(user_id=user[0], is_available=False, order_by_info=('l.loan_date', "DESC"))

    print("\n   대출이 정상적으로 완료되었습니다.")

    print("\n   현재 대출 중인 도서의 목록입니다.")
    print(render_table(change_book_list(current_loan_books, 2), 'books'))

    return current_loan_books


def return_books(user: Tuple) -> List | int:
    print("\n   =========           도서 반납을 진행합니다.          =========\n")

    retunable_book_list = Books().get(user_id=user[0], is_available=False, order_by_info=('l.loan_date', "DESC"))
    username = Users().get(id=user[0])[0][1]

    if not retunable_book_list:
        print(f"   {username} 님의 반납 가능한 도서가 존재하지 않습니다.\n")
        return -1

    print(f"\n   {username} 님의 반납 가능한 도서 목록입니다.")
    print(render_table(change_book_list(retunable_book_list, 2), 'books'))

    book_id_list = return_book_ids_validation(user[0], retunable_book_list)

    if book_id_list == -1:
        return -1

    else:
        for book_id in book_id_list:
            target_book = Books().put(id=book_id)
            update_return = Loans().put(return_date=datetime.now(), return_update=True, return_book_id=book_id)

    current_loan_books = Books().get(user_id=user[0], is_available=False, order_by_info=('l.loan_date', "DESC"))

    print("\n   반납이 정상적으로 완료되었습니다.")

    print("\n   현재 대출 중인 도서의 목록입니다.")
    print(render_table(change_book_list(current_loan_books, 2), 'books'))

    return current_loan_books


def fetch_my_loan_book_list(user: Tuple):
    print(f"\n   =========         {user[1]}님의 현재 대출 도서 정보입니다.         =========\n")

    current_loan_books = Books().get(user_id=user[0], is_available=False, order_by_info=('loan_date', 'DESC'))

    print("\n   [조회 결과]")
    print(render_table(change_book_list(current_loan_books, 2), 'books'))

    return current_loan_books


def fetch_book_in_admin():
    print("\n   =========           모든 도서 정보를 조회합니다.           =========")

    books = Books().get()

    print(render_table(change_book_list(books, 3), "books"))

    return books


def create_book_in_admin():
    print("\n   =========           도서 정보를 등록합니다.           =========")

    title = name_validation("제목")
    if title == -1:
        return -1

    author = name_validation("저자")
    if author == -1:
        return -1

    publisher = name_validation("출판사")
    if publisher == -1:
        return -1

    new_book = Books(title, author, publisher).post()

    book = Books().get(order_by_info=("b.id", "DESC"), size=1)

    print("\n   도서 정보 등록이 완료되었습니다.")
    print(render_table(change_book_list(book, 1), "books"))

    return book


def update_book_in_admin():
    print("\n   =========           도서 정보를 수정합니다.           =========")

    book = existed_id_validation("books")

    if book == -1:
        return -1

    title = name_validation("제목")
    if title == -1:
        return -1

    author = name_validation("저자")
    if author == -1:
        return -1

    publisher = name_validation("출판사")
    if publisher == -1:
        return -1

    Books().put(id=book[0], new_title=title, new_author=author, new_publisher=publisher)

    updated_book = Books().get(id=book[0])

    print("\n   도서 정보 수정이 완료되었습니다.")
    print(render_table(change_book_list(updated_book, 1), "books"))

    return updated_book


def fetch_loan_in_admin():
    print("\n   =========           모든 대출 정보를 조회합니다.           =========")

    loans = Loans().get()

    print(render_table(change_loan_list(loans), "loans"))

    return loans


def create_loan_in_admin():
    print("\n   =========           대출 정보를 등록합니다.           =========")

    user = existed_id_validation("users")
    if user == -1:
        return -1

    while True:
        book = existed_id_validation("books")
        if book == -1:
            return -1

        check_book = Books().get(id=book[0])
        if not check_book[0][4]:
            print("\n  현재 대출중인 도서이므로 대출 정보 생성이 불가합니다.\n")
            continue
        else:
            break

    loan_date = datetime_validation("대출일자", "현재 시각을 입력하려면")
    if loan_date == -1:
        return -1
    loan_date = datetime.now() if loan_date is None else loan_date

    return_date = datetime_validation("반납일자", "반납일자를 미지정하려면")
    if return_date == -1:
        return -1

    new_loan = Loans(user[0], book[0], loan_date, return_date).post()
    update_book = Books().put(id=book[0])

    loan = Loans().get(order_by_info=("id", "DESC"), size=1)

    print("\n   대출 정보 등록이 완료되었습니다.")
    print(render_table(change_loan_list(loan), "loans"))

    return book


def update_loan_in_admin():
    print("\n   =========           대출 정보를 수정합니다.           =========")

    loan = existed_id_validation("loans")
    if loan == -1:
        return -1

    user = existed_id_validation("users")
    if user == -1:
        return -1

    book = existed_id_validation("books")
    if book == -1:
        return -1

    loan_date = datetime_validation("대출일자", "현재 시각을 입력하려면")
    if loan_date == -1:
        return -1

    return_date = datetime_validation("반납일자", "반납일자를 미지정하려면")
    if return_date == -1:
        return -1

    Loans().put(id=loan[0], user_id=user[0], book_id=book[0], loan_date=loan_date, return_date=return_date, return_update=True)
    updated_book = Books().put  (id=book[0])

    updated_loan = Loans().get(id=loan[0])

    print("\n   대출 정보 수정이 완료되었습니다.")
    print(render_table(change_loan_list(updated_loan), "loans"))

    return updated_loan