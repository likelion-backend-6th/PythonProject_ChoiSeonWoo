import re
from time import sleep

from users.models import Users
from users.validation import username_validation, password_validation, user_validation, password_validation2

my_info = {"user": None, "is_logined": False}


def sign_up():
    print("===========           회원가입을 진행합니다.           ==========")
    users = Users().get()

    message = "   가입에 사용할 사용자명을 입력해주세요.\n" \
              "   이미 가입된 회원의 경우, 로그인 메뉴로 이동하시려면 숫자 1을 입력해주세요.\n" \
              "   --->  입력  :  "
    username = input(message)
    if username == "1":
        return login()
    username = username_validation(username, users)
    if not username:
        return sign_up()

    fullname = input("성함을 입력해주세요. : ")

    password = input("비밀번호를 입력해주세요. : ")
    password = password_validation(password)
    if not password:
        return sign_up()

    print(username, fullname, password)

    new_user = Users(username, fullname, password)
    new_user.post()

    print("회원가입이 완료되었습니다.")
    print("이어서 로그인을 바로 진행하도록 하겠습니다.")
    sleep(0.5)
    for i in range(3):
        print(3 - i)
        sleep(0.5)
    return login()


def login() -> object:
    print("===========            로그인을 진행합니다.            ==========\n")
    usr_cnt, pw_cnt = 0, 0

    message = "   사용자명을 입력해주세요.\n" \
              "   회원가입을 진행하시려면 숫자 1을 입력해주세요.\n" \
              "   --->  입력  :  "
    username = input(message)
    if username == "1":
        return sign_up()
    user = user_validation(username)
    if not user:
        return login()

    password = input("   비밀번호를 입력해주세요. : ")
    password_matched = password_validation2(password, user)
    if not password_matched:
        return login()

    my_info["user"] = user
    my_info["is_logined"] = True
    print(f"   {my_info['user'][2]}님, 어서오세요. 환영합니다")
    print(my_info)
    return my_info


def logout() -> object:
    print("   로그아웃 되었습니다.")
    my_info["user"] = None
    my_info["is_logined"] = False
    return my_info

