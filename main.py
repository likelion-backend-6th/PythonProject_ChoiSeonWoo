from typing import List, Optional, Dict, Callable

from books.utils import fetch_books_list, search_book_list, loan_books, return_books
from common.database import create_table
from common.settings import TABLES, CREATE_QUERY_LISTS
from common.validation import menu_num_validation, USER_MENU_NUM_LIST, USER_MENU_INIT_MESSAGE
from users.utils import sign_up, login, logout


class LibrarySystem:
    MENU_INFO: Dict[str, str] = {
        "1": "도서 조회",
        "2": "도서 검색",
        "3": "도서 대출",
        "4": "도서 반납",
        "7": "회원 가입",
        "8": "로그인",
        "9": "로그아웃",
        "-1": "이전 메뉴",
        "007": "프로그램 종료",
    }

    MENU: Dict[str, Callable] = {
        "1": fetch_books_list,
        "2": search_book_list,
        "3": loan_books,
        "4": return_books,
        "7": sign_up,
        "8": login,
        "9": logout,
        "007": None,
    }

    MESSAGE: Dict[str, str] = {
        "welcome": "\n   === 안녕하세요. 오늘도 도서관리시스템을 이용해주셔서 감사합니다. ===\n"
                   "   ============     지금부터 시스템을 시작하겠습니다.      ============",
        "manage_user": "\n   ===========         사용자 관리 메뉴입니다.         ===========",
        "manage_book": "\n   ===========          도서 관리 메뉴입니다.          ===========",
        "bye": "\n   =======  오늘도 저희 도서관리시스템을 이용해주셔서 감사합니다. ========\n"
               "   =============           다음에 다시 이용해주세요.          ============",
    }

    def __init__(self):
        self.user: List = []

    def manage_user(self):
        print(self.MESSAGE["manage_user"])
        while not self.user:
            execute_menu_num = menu_num_validation(USER_MENU_NUM_LIST, USER_MENU_INIT_MESSAGE)
            result = self.MENU[execute_menu_num]()

            if result == -1:
                continue
            else:
                self.user = result
                break

    def manage_book(self):
        pass

    def main(self):
        print(self.MESSAGE["welcome"])
        create_table(TABLES, CREATE_QUERY_LISTS)
        while True:
            if not self.user:
                self.manage_user()


if __name__ == "__main__":
    app = LibrarySystem()
    app.main()
