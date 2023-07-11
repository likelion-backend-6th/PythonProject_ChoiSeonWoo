from typing import List, Optional

from books.models import Books, Loans
from common.utils import waiting
from users.models import Users

USER_MENU_NUM_LIST = ["7", "8", "007"]
USER_MENU_INIT_MESSAGE = "   7. 회원가입   8. 로그인   007. 프로그램 종료\n\n"
BOOK_MENU_NUM_LIST = ["1", "2", "3", "4", "5", "9", "007"]
BOOK_MENU_INIT_MESSAGE = "   1. 도서 조회   2. 도서 검색   3. 도서 대출   4. 도서 반납   5. 나의 대출 도서\n" \
                         "   9. 로그아웃   007. 프로그램 종료\n\n"

ADMIN_MENU_NUM_LIST = BOOK_MENU_NUM_LIST + ["11", "12", "13", "21", "22", "23", "31", "32", "33"]
ADMIN_MENU_INIT_MESSAGE = BOOK_MENU_INIT_MESSAGE + \
                          "   ===========              관리자 메뉴               ===========\n\n" \
                          "   11. 유저 조회   12. 유저 등록   13. 유저 수정\n" \
                          "   21. 도서 조회   22. 도서 등록   23. 도서 수정\n" \
                          "   31. 대출 조회   32. 대출 등록   33. 대출 수정\n\n"

LOGOUT_MESSAGE = "로그아웃"
TERMINATE_MESSAGE = "시스템을 대기모드로 전환"
SEARCH_LOANABLE_MESSAGE = "대출 가능한 도서를 먼저 검색"
PASSWORD_MESSAGE = "비밀번호를 변경"


def menu_num_validation(menu_num_list: List, menu_init_message: str) -> str:
    init_message = "\n   다음을 확인하여 메뉴의 번호를 입력해주세요 .\n" + \
                   menu_init_message + \
                   "   -->  메뉴 입력  :  "
    cnt = 0
    message = init_message

    while True:
        run_menu_num = input(message)

        if run_menu_num.isdigit():
            if run_menu_num in menu_num_list:
                return run_menu_num
            else:
                error_message = "\n   입력하신 번호에 대한 메뉴가 존재하지 않습니다.\n"
        else:
            error_message = "\n   메뉴에 해당하는 숫자를 입력해야 합니다.\n"

        cnt += 1
        message = error_message + f"   확인 후 번호를 다시 입력해주세요. ({cnt}/3)\n" \
                                  "   -->  메뉴 입력  :  "
        if cnt == 3:
            message, cnt = init_message, 0
            print("\n   3회 이상 실패하였으므로 이전 메뉴로 돌아갑니다.")
            waiting()


def bool_validation(execute_meessage: str) -> Optional[bool]:
    init_message = f"\n   {execute_meessage} 하시겠습니까? (Y/n)\n" \
                    "   --->  입력  :  "
    cnt = 0
    message = init_message

    while True:
        bool_type = input(message)
        if bool_type.lower() in ["y", "yes", "예", "네"]:
            return True
        elif bool_type.lower() in ["n", "no", "아니오"]:
            return False
        cnt += 1
        message = f"\n   올바른 값을 입력해주세요. ({cnt}/3)\n" \
                  "   -->  (Y/N) 입력  :  "

        if cnt == 3:
            print("\n   3회 이상 실패하였으므로 이전 메뉴로 돌아갑니다.")
            waiting()

            return None


def stand_by_validation() -> int:
    init_message = f"\n   다음 메뉴를 확인하여 번호를 입력해주세요.\n" \
                    "   1.  시스탬 재가동   2. 대기 유지   3. 시스템 완전 종료\n" \
                    "   --->  번호 입력  :  "
    cnt = 0

    message = init_message

    while True:
        type_ = input(message)
        if type_ in ["1", "2", "3"]:
            return int(type_)

        cnt += 1
        message = f"   번호를 잘못 입력하였습니다. ({cnt}/3)\n" \
                   " 확인 후 번호를 다시 입력해주세요.\n" \
                   "   -->  메뉴 입력  :  "

        if cnt == 3:
            message, cnt = init_message, 0
            print("\n   잠시 후 다시 이용해주세요.")
            waiting()

            return 2


def existed_id_validation(target):
    item_list = {
        "users": ["유저", Users],
        "books": ["도서", Books],
        "loans": ["대출", Loans]
    }

    init_message = f"\n   {item_list[target][0]}의 ID를 입력해주세요.\n" \
                   "   (상위 메뉴로 돌아가려면 '-1'을 입력해주세요.)\n" \
                   "   --->  입력  :  "
    cnt = 0
    if target == "loans":
        item_list[target][1]().get(return_date_info=("NULL", True))
    objects = item_list[target][1]().get()
    message = init_message

    while True:
        try:
            object_id = int(input(message))
            if object_id == -1:
                return -1
            elif all(object_[0] != object_id for object_ in objects):
                error_message = f"\n   해당 ID의 {item_list[target][0]} 이/가 존재하지 않습니다.\n"
            for object_ in objects:
                if object_[0] == object_id:
                    return object_
        except ValueError:
            error_message = "\n   ID는 숫자만 입력해야 합니다.\n"

        cnt += 1
        message = error_message + f"   확인 후 ID를 다시 입력해주세요. ({cnt}/3)\n" \
                                   "   (상위 메뉴로 돌아가려면 '-1'을 입력해주세요.)\n" \
                                   "   -->  메뉴 입력  :  "

        if cnt == 3:
            print("\n   3회 이상 실패하였으므로 상위 메뉴로 돌아갑니다.")
            waiting()

            return -1