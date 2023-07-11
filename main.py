from typing import List, Dict, Callable

from books.core import fetch_book_list, search_book_list, loan_books, return_books, fetch_my_loan_book_list, \
                        fetch_book_in_admin, create_book_in_admin, update_book_in_admin, \
                        fetch_loan_in_admin, create_loan_in_admin, update_loan_in_admin
from common.core import create_table, stand_by
from common.settings import TABLES, CREATE_QUERY_LISTS, ADMIN_USER_ID_LIST
from common.utils import waiting, clearing, wait_clear, clear_wait_clear
from common.validation import USER_MENU_NUM_LIST, USER_MENU_INIT_MESSAGE, BOOK_MENU_NUM_LIST, BOOK_MENU_INIT_MESSAGE, \
                              ADMIN_MENU_NUM_LIST, ADMIN_MENU_INIT_MESSAGE, TERMINATE_MESSAGE, \
                              menu_num_validation, bool_validation
from users.core import sign_up, login, logout, fetch_user_in_admin, create_user_in_admin, update_user_in_admin


class LibrarySystem:
    MENU_INFO: Dict[str, str] = {
        "1": "도서 조회",   "2": "도서 검색",   "3": "도서 대출",    "4": "도서 반납",    "5": "나의 대출 도서",
        "7": "회원 가입",   "8": "로그인",      "9": "로그아웃",    "-1": "이전 메뉴",    "007": "프로그램 종료",
        "11": "유저 조회",  "12": "유저 등록",  "13": "유저 수정",
        "21": "도서 조회",  "22": "도서 등록",  "23": "도서 수정",
        "31": "대출 조회",  "32": "대출 등록",  "33": "대출 수정",
    }

    MENU: Dict[str, Callable] = {
        "1": fetch_book_list, "2": search_book_list, "3": loan_books, "4": return_books, "5": fetch_my_loan_book_list,
        "7": sign_up,  "8": login,  "9": logout,
        "11": fetch_user_in_admin,  "12": create_user_in_admin,  "13": update_user_in_admin,
        "21": fetch_book_in_admin,  "22": create_book_in_admin,  "23": update_book_in_admin,
        "31": fetch_loan_in_admin,  "32": create_loan_in_admin,  "33": update_loan_in_admin,
    }

    MESSAGE: Dict[str, str] = {
        "welcome": "\n   === 안녕하세요. 오늘도 도서관리시스템을 이용해주셔서 감사합니다. ===\n"
                   "   ============     지금부터 시스템을 시작하겠습니다.      ============",
        "manage_user": "\n   ===========         사용자 관리 메뉴입니다.         ===========",
        "manage_book": "\n   ===========          도서 관리 메뉴입니다.          ===========",
        "bye": "\n   =======  오늘도 저희 도서관리시스템을 이용해주셔서 감사합니다. ========\n"
               "   =============           다음에 다시 이용해주세요.          ============",
        "terminate": "\n   ===========         시스템 종료 안내         ==========="

    }

    def __init__(self):
        self.user: List = []

    def manage_user(self):
        print(self.MESSAGE["manage_user"])
        while not self.user:
            execute_menu_num = menu_num_validation(USER_MENU_NUM_LIST, USER_MENU_INIT_MESSAGE)

            clearing()
            if execute_menu_num == "007":
                result = self.terminate()
            else:
                result = self.MENU[execute_menu_num]()

            if result == -1:
                clearing()
                print(self.MESSAGE["manage_user"])
                continue
            else:
                self.user = result
                break

    def manage_book(self):

        while True:
            print(self.MESSAGE["manage_book"])
            result = 0
            if self.user[0][0] in ADMIN_USER_ID_LIST:
                execute_menu_num = menu_num_validation(ADMIN_MENU_NUM_LIST, ADMIN_MENU_INIT_MESSAGE)
            else:
                execute_menu_num = menu_num_validation(BOOK_MENU_NUM_LIST, BOOK_MENU_INIT_MESSAGE)

            clearing()

            if execute_menu_num == "007":
                result = self.terminate()

            elif execute_menu_num in ["1", "3", "4", "5"]:
                result = self.MENU[execute_menu_num](self.user[0])

            elif execute_menu_num in [
                                        "2", "11", "12", "13", "14", "21", "22", "23", "24",
                                        "31", "32", "33", "34"
                                      ]:
                result = self.MENU[execute_menu_num]()

            if result == -1:
                break

            if execute_menu_num == "9":
                current_user_info = self.MENU[execute_menu_num]()

                if current_user_info is None:
                    self.user = current_user_info
                    break

            move_input = input("\n   이전 메뉴로 돌아갑니다. 아무 키나 눌러주세요.")
            clearing()

    def terminate(self):
        print("\n   =======            시스템 종료 화면            =======\n")
        is_stood_by = bool_validation(TERMINATE_MESSAGE)

        if is_stood_by:
            self.user = None
            clearing()
            return stand_by()
        else:
            return -1

    def main(self):
        clearing()
        print(self.MESSAGE["welcome"])
        create_table(TABLES, CREATE_QUERY_LISTS)

        while True:
            if not self.user:
                wait_clear()
                self.manage_user()
            wait_clear()
            self.manage_book()

            if self.user:
                continue


if __name__ == "__main__":
    app = LibrarySystem()
    app.main()
