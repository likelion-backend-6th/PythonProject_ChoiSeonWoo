from time import sleep
from typing import List

from common.validation import bool_validation, LOGOUT_MESSAGE
from users.models import Users
from users.validation import username_validation, password_validation, user_validation, password_validation2, \
    fullname_validation


def sign_up():
    print("\n   =========           회원가입을 진행합니다.           =========")

    username = username_validation()

    if username == "8":
        return login()
    elif username == "-1":
        return -1

    fullname = fullname_validation()

    if fullname == "-1":
        return -1

    password = password_validation()

    if password == "-1":
        return -1

    print(username, fullname, password)

    new_user = Users(username, fullname, password)
    new_user.post()

    print("\n   회원가입이 완료되었습니다.\n" 
          "   이어서 로그인을 바로 진행하도록 하겠습니다.")
    sleep(0.5)
    for i in range(3):
        print(f"   {3 - i}")
        sleep(0.5)
    return login()


def login() -> object:
    print("\n   ========            로그인을 진행합니다.            =========\n")

    user = user_validation()

    if user == "7":
        return sign_up()
    elif user == "-1":
        return -1

    password = password_validation2(user)

    if password == "-1":
        return -1

    print(f"\n   {user[0][2]}님, 어서오세요!  환영합니다. :) ")
    return user


def logout():
    print("\n   =======            로그아웃을 진행합니다.            ========\n")

    is_loggedout = bool_validation(LOGOUT_MESSAGE)

    if is_loggedout:
        return print("\n   로그아웃 되었습니다.\n   초기 화면으로 돌아갑니다.")
    else:
        return True


