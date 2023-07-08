from time import sleep
from typing import List

from books.models import Books


def fetch_type_validation(fetch_type: int):
    cnt = 0
    while True:
        if fetch_type in [1, 2]:
            return fetch_type
        cnt += 1
        if cnt == 3:
            print("   3회 이상 실패하였으므로 초기 메뉴로 돌아갑니다.")
            sleep(0.5)
            for i in range(3):
                print(f"   {3 - i}")
                sleep(0.3)
            return False
        sleep(0.2)
        fetch_type = int(input(f"   잘못 입력하였습니다. 번호를 다시 입력해주세요. ({cnt}/3)  :  "))


def search_type_validation(search_type: int):
    cnt = 0
    while True:
        if search_type in [1, 2]:
            return search_type
        cnt += 1
        if cnt == 3:
            print("   3회 이상 실패하였으므로 초기 메뉴로 돌아갑니다.")
            sleep(0.5)
            for i in range(3):
                print(f"   {3 - i}")
                sleep(0.3)
            return False
        sleep(0.2)
        search_type = int(input(f"   잘못 입력하였습니다. 번호를 다시 입력해주세요. ({cnt}/3)  :  "))


def loan_book_ids_validation() -> List:
    loanable_book_id_list = list(map(lambda x: x[0], Books().get(is_available=True)))
    cnt = 0

    message3 = "\n   대출을 희망하는 도서의 ID를 입력해주세요.\n" \
               "   여러 권을 대출하고자 하는 경우, 쉼표(,)로 구분하여 ID를 입력해주세요.\n" \
               "   -->  ID 입력  :  "

    book_ids = input(message3).replace(" ", "")
    if not book_ids:
        return []
    book_id_list = list(map(int, book_ids.split(",")))

    while True:
        if len(book_id_list) <= 1 or len(book_id_list) == len(set(book_id_list)):
            if all(book_id in loanable_book_id_list for book_id in book_id_list):
                return book_id_list
            else:
                error_message = "   요청하신 ID에 해당하는 대출 가능한 도서가 존재하지 않습니다.\n   "
        else:
            error_message = "   숫자를 중복 입력 입력하였습니다."
        cnt += 1
        if cnt == 3:
            print("   3회 이상 실패하였으므로 초기 메뉴로 돌아갑니다.")
            sleep(0.5)
            for i in range(3):
                print(f"   {3 - i}")
                sleep(0.3)
            return loan_book_ids_validation()
        sleep(0.2)

        message3 = error_message + f"ID를 다시 입력해주세요. ({cnt}/3)  :  \n" \
                   "   여러 권을 대출하고자 하는 경우, 쉼표(,)로 구분하여 ID를 입력해주세요.\n" \
                   "   -->  ID 입력  :  "
        book_ids = input(message3)
        book_id_list = book_ids.replace(" ", "").split(",")
        book_id_list = list(map(int, book_id_list))


def return_book_ids_validation(user_id) -> List:
    returnable_book_id_list = list(map(lambda x: x[0], Books().get(is_available=False, user_id=user_id)))
    cnt = 0
    print(f"returnable_book_id_list: {returnable_book_id_list}")
    message4 = "\n   반납을 희망하는 도서의 ID를 입력해주세요.\n" \
               "   여러 권을 반납하고자 하는 경우, 쉼표(,)로 구분하여 ID를 입력해주세요.\n" \
               "   -->  ID 입력  :  "

    book_ids = input(message4).replace(" ", "")
    if not book_ids:
        return []
    book_id_list = list(map(int, book_ids.split(",")))

    while True:
        if len(book_id_list) <= 1 or len(book_id_list) == len(set(book_id_list)):
            if all(book_id in returnable_book_id_list for book_id in book_id_list):
                return book_id_list
            else:
                error_message = "   요청하신 ID에 해당하는 반납 가능한 도서가 존재하지 않습니다.\n   "
        else:
            error_message = "   숫자를 중복 입력 입력하였습니다."
        cnt += 1
        if cnt == 3:
            print("   3회 이상 실패하였으므로 초기 메뉴로 돌아갑니다.")
            sleep(0.5)
            for i in range(3):
                print(f"   {3 - i}")
                sleep(0.3)
            return return_book_ids_validation(user_id)
        sleep(0.2)

        message4 = error_message + f"ID를 다시 입력해주세요. ({cnt}/3)  :  \n" \
                   "   여러 권을 반납하고자 하는 경우, 쉼표(,)로 구분하여 ID를 입력해주세요.\n" \
                   "   -->  ID 입력  :  "
        book_ids = input(message4)
        book_id_list = book_ids.replace(" ", "").split(",")
        book_id_list = list(map(int, book_id_list))