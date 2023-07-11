from time import sleep
from typing import List, Optional

USER_MENU_NUM_LIST = ["7", "8", "007"]
USER_MENU_INIT_MESSAGE = "   7. 회원가입   8. 로그인   007. 프로그램 종료\n"
BOOK_MENU_NUM_LIST = ["1", "2", "3", "4", "5", "9", "007"]
BOOK_MENU_INIT_MESSAGE = "   1. 도서 조회   2. 도서 검색   3. 도서 대출   4. 도서 반납   5. 나의 대출 도서\n" \
                         "   9. 로그아웃   007. 프로그램 종료\n"

LOGOUT_MESSAGE = "로그아웃"
TERMINATE_MESSAGE = "시스템을 대기모드로 전환"
SEARCH_LOANABLE_MESSAGE = "대출 가능한 도서를 먼저 검색"


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
            print("   3회 이상 실패하였으므로 이전 메뉴로 돌아갑니다.")
            sleep(0.5)
            for i in range(3):
                print(f"   {3 - i}")
                sleep(0.3)


def bool_validation(execute_meessage: str) -> Optional[bool]:
    init_message = f"   {execute_meessage} 하시겠습니까? (Y/n)\n" \
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
            sleep(0.5)
            for i in range(3):
                print(f"   {3 - i}")
                sleep(0.5)

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
            sleep(0.5)
            for i in range(3):
                print(f"   {3 - i}")
                sleep(0.5)
            return 2