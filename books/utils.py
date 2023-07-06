from time import sleep
from typing import List

from books.models import Books


def fetch_books_list() -> List:
    message = [
        "   희망하시는 조회 대상 도서 정보의 번호를 입력해주세요.",
        "   [  1. 모든 도서  2. 현재 대출 가능한 도서  ]",
        "   -->  번호 입력  :  "
    ]
    message = ("\n").join(message)

    while True:

        books = Books()

        fetch_type = int(input(message))

        if fetch_type == 1:
            books_list: List = books.get()
            return books_list
        elif fetch_type == 2:
            books_list: List = books.get(is_available=True)
            return books_list
        else:
            print(" \n   잘못 입력하셨습니다. 확인 후 다시 입력해주세요. \n")
            sleep(0.4)