from time import sleep
from typing import List

from books.models import Books


FETCH_TYPE_MESSAGE = "\n   희망하시는 조회 대상 도서 정보의 번호를 입력해주세요.\n" \
                     "   [  1. 모든 도서  2. 현재 대출 가능한 도서  ]\n" \
                     "   (이전 메뉴로 돌아가려면 '-1'을 입력해주세요.)\n" \
                     "   -->  번호 입력  :  "

SEARCH_TYPE_MESSAGE = "\n   검색을 희망하는 항목에 대한 번호를 입력해주세요.\n" \
                      "   [  1. ID  2. 제목  ]\n" \
                      "   (이전 메뉴로 돌아가려면 '-1'을 입력해주세요.)\n" \
                      "   -->  번호 입력  :  "


def type_validation(message: str):
    init_message = message
    cnt = 0

    message = init_message

    while True:
        try:
            type_ = int(input(message))
            if type_ in [1, 2, -1]:
                return type_
            else:
                error_message = "\n   번호를 잘못 선택하였습니다.\n"
        except ValueError:
            error_message = "\n   번호에 해당하는 숫자를 입력해야 합니다.\n"

        cnt += 1
        message = error_message + f"   확인 후 번호를 다시 입력해주세요. ({cnt}/3)\n" \
                                   "   (이전 메뉴로 돌아가려면 '-1'을 입력해주세요.)\n" \
                                   "   -->  메뉴 입력  :  "

        if cnt == 3:
            message, cnt = init_message, 0
            print("\n   3회 이상 실패하였으므로 이전 메뉴로 돌아갑니다.")
            sleep(0.5)
            for i in range(3):
                print(f"   {3 - i}")
                sleep(0.3)
            return -1


def search_validation(search_type: int, book_list: list):
    search_type_list = {1: "ID", 2: "제목"}
    init_message = f"\n   도서의 {search_type_list[search_type]} 을/를 입력해주세요.\n" \
                    "   (이전 메뉴로 돌아가려면 '-1'을 입력해주세요.)\n" \
                   f"   -->  {search_type_list[search_type]} 입력  :  "
    cnt = 0
    message = init_message

    while True:
        item = input(message).strip()
        if item.isdigit() and int(item) == -1:
            return -1
        if search_type == 2 or (search_type == 1 and item.isdigit()):
            if search_type == 1:
                book_list: List = list(filter(lambda x: x[0] == int(item), book_list))
            elif search_type == 2:
                book_list: List = list(filter(lambda x: item in x[1], book_list))
            if not book_list:
                print(f"\n   해당 {search_type_list[search_type]} (으)로 검색한 도서는 존재하지 않습니다.\n   이전 메뉴로 돌아갑니다.")
                return []
            return book_list

        if search_type == 1 and not item.isdigit():
            error_message = "\n   ID는 숫자만 입력 가능합니다.\n"
        elif search_type == 2 and not item:
            error_message = "\n   제목은 1자 이상의 글자로 입력 가능합니다.\n"

        cnt += 1
        message = error_message +  \
                  f"   확인 후 다시 입력해주세요. ({cnt}/3)\n" + \
                   "   (이전 메뉴로 돌아가려면 '-1'을 입력해주세요.)\n" \
                  f"   -->  {search_type_list[search_type]} 입력  :  "

        if cnt == 3:
            message, cnt = init_message, 0
            print("\n   3회 이상 실패하였으므로 이전 메뉴로 돌아갑니다.")
            sleep(0.5)
            for i in range(3):
                print(f"   {3 - i}")
                sleep(0.3)
            return -1


def loan_book_ids_validation():
    loanable_book_id_list = list(map(lambda x: x[0], Books().get(is_available=True)))
    init_message = "\n   대출을 희망하는 도서의 ID를 입력해주세요.\n" \
                   "   여러 권을 대출하고자 하는 경우, 쉼표(,)로 구분하여 ID를 입력해주세요.\n" \
                   "   (이전 메뉴로 돌아가려면 '-1'을 입력해주세요.)\n" \
                   "   -->  ID 입력  :  "
    cnt = 0
    message = init_message

    while True:
        book_ids = input(message).replace(" ", "")

        try:
            book_id_list = list(map(int, book_ids.split(",")))

            if book_id_list[0] == -1:
                return -1

            if len(book_id_list) <= 1 or len(book_id_list) == len(set(book_id_list)):
                if all(book_id in loanable_book_id_list for book_id in book_id_list):
                    return book_id_list
                else:
                    error_message = "\n   요청하신 ID의 도서(들) 중 대출 불가한 도서가 포함되어 있습니다.\n   "
            else:
                error_message = "\n   숫자를 중복 입력 입력하였습니다.\n   "

        except ValueError:
            error_message = "\n   잘못된 입력입니다.\n   "

        cnt += 1
        message = error_message + f"확인 후 ID를 다시 입력해주세요. ({cnt}/3)\n" \
                                  "   여러 권을 대출하고자 하는 경우, 쉼표(,)로 구분하여 ID를 입력해주세요.\n" \
                                  "   (이전 메뉴로 돌아가려면 '-1'을 입력해주세요.)\n" \
                                  "   -->  ID 입력  :  "
        if cnt == 3:
            message, cnt = init_message, 0
            print("\n   3회 이상 실패하였으므로 이전 메뉴로 돌아갑니다.")
            sleep(0.5)
            for i in range(3):
                print(f"   {3 - i}")
                sleep(0.3)
            return -1


def return_book_ids_validation(user_id, retunable_book_list):

    returnable_book_id_list = list(map(lambda x: x[0], retunable_book_list))

    init_message = "\n   반납을 희망하는 도서의 ID를 입력해주세요.\n" \
                   "   여러 권을 반납하고자 하는 경우, 쉼표(,)로 구분하여 ID를 입력해주세요.\n" \
                   "   (이전 메뉴로 돌아가려면 '-1'을 입력해주세요.)\n" \
                   "   -->  ID 입력  :  "
    cnt = 0
    message = init_message

    while True:
        book_ids = input(message).replace(" ", "")

        try:
            book_id_list = list(map(int, book_ids.split(",")))

            if book_id_list[0] == -1:
                return -1

            if len(book_id_list) <= 1 or len(book_id_list) == len(set(book_id_list)):
                if all(book_id in returnable_book_id_list for book_id in book_id_list):
                    return book_id_list
                else:
                    error_message = "\n   요청하신 ID에 해당하는 반납 가능한 도서가 존재하지 않습니다.\n   "
            else:
                error_message = "\n   숫자를 중복 입력 입력하였습니다.\n   "

        except ValueError:
            error_message = "\n   잘못된 입력입니다.\n   "

        cnt += 1
        message = error_message + f"\n   확인 후 ID를 다시 입력해주세요. ({cnt}/3)\n" \
                                   "   여러 권을 반납하고자 하는 경우, 쉼표(,)로 구분하여 ID를 입력해주세요.\n" \
                                   "   (이전 메뉴로 돌아가려면 '-1'을 입력해주세요.)\n" \
                                   "   -->  ID 입력  :  "
        if cnt == 3:
            message, cnt = init_message, 0
            print("\n   3회 이상 실패하였으므로 이전 메뉴로 돌아갑니다.")
            sleep(0.5)
            for i in range(3):
                print(f"   {3 - i}")
                sleep(0.3)
            return -1