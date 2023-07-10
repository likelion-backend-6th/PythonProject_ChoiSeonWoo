from typing import List, Optional, Dict, Callable

from books.utils import fetch_books_list, search_book_list, loan_books, return_books
from common.database import create_table
from common.settings import TABLES, CREATE_QUERY_LISTS
from common.validation import menu_num_validation, USER_MENU_NUM_LIST, USER_MENU_INIT_MESSAGE
from users.utils import sign_up, login, logout


class LibrarySystem:

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
        "welcome": "=== 안녕하세요. 오늘도 도서관리시스템을 이용해주셔서 감사합니다. ===\n"
                   "===========     지금부터 시스템을 시작하겠습니다.      ==========",
    }

    progress: List= []
    user: Optional[Dict] = None

    def manage_user(self):
        execute_menu_num = menu_num_validation(USER_MENU_NUM_LIST, USER_MENU_INIT_MESSAGE, self.progress)
        self.user = self.MENU[execute_menu_num](self.progress)

    def manage_book(self):
        pass

    def main(self):
        create_table(TABLES, CREATE_QUERY_LISTS)
        self.manage_user()


if __name__ == "__main__":
    app = LibrarySystem()
    app.main()