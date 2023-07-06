from time import sleep
from typing import List, Union

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


def search_book_list(book_lists: List) -> Union[List, str]:
    message1 = [
        "\n   검색을 희망하는 항목에 대한 번호를 입력해주세요.",
        "   [  1. ID  2. 제목  ]",
        "   -->  번호 입력  :  "
    ]
    message1 = ("\n").join(message1)

    search_type_list = {1: "ID", 2: "제목"}

    while True:
        search_type = int(input(message1))

        message2 = [
            f"\n   도서의 {search_type_list[search_type]} 을/를 입력해주세요.",
            f"   -->  {search_type_list[search_type]} 입력  :  "
        ]
        message2 = ("\n").join(message2)

        target = input(message2)

        if search_type == 1:
            result: List = list(filter(lambda x: x[0] == int(target), book_lists))
            result = result[0] if result else "해당 도서는 존재하지 않습니다."
        elif search_type == 2:
            result: List = list(filter(lambda x: target in x[1], book_lists))
            result = result if result else "해당 도서는 존재하지 않습니다."

        return result