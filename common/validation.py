from time import sleep
from typing import List

USER_MENU_NUM_LIST = ["7", "8", "007"]
USER_MENU_INIT_MESSAGE = "   7. 회원가입   8. 로그인   007. 프로그램 종료\n"
BOOK_MENU_NUM_LIST = ["1", "2", "3", "4", "9", "0", "007"]
BOOK_MENU_INIT_MESSAGE = "   1. 도서 조회   2. 도서 검색   3. 도서 대출   4. 도서 반납\n" \
                         "   9. 로그아웃   0. 이전 메뉴   007. 프로그램 종료\n"

LOGOUT_MESSAGE = "로그아웃"
TERMINATE_MESSAGE = "시스템 종료"


def menu_num_validation(menu_num_list: List, menu_init_message: str):
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
            print("   3회 이상 실패하였으므로 초기 메뉴로 돌아갑니다.")
            sleep(0.5)
            for i in range(3):
                print(f"   {3 - i}")
                sleep(0.3)


def bool_validation(execute_meessage: str):
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
        message = f"\n   {execute_meessage} 여부를 바르게 입력해주세요. ({cnt}/3)\n" \
                  "   -->  (Y/N) 입력  :  "

        if cnt == 3:
            print("\n   3회 이상 실패하였으므로 초기 메뉴로 돌아갑니다.")
            sleep(0.5)
            for i in range(3):
                print(f"   {3 - i}")
                sleep(0.5)

            return None