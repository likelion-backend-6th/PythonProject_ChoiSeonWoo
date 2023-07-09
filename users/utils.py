from time import sleep
from typing import List

from users.models import Users
from users.validation import username_validation, password_validation, user_validation, password_validation2

my_info = {"user": None, "is_logined": False}


def sign_up(progress: List):
    print("===========           회원가입을 진행합니다.           ==========\n")
    progress.append("8")

    username = username_validation()
    if username == "8":
        return login(progress)

    fullname = input("   성함을 입력해주세요. : ")

    password = password_validation()

    print(username, fullname, password)

    new_user = Users(username, fullname, password)
    new_user.post()

    print("회원가입이 완료되었습니다.")
    print("이어서 로그인을 바로 진행하도록 하겠습니다.")
    sleep(0.5)
    for i in range(3):
        print(3 - i)
        sleep(0.5)
    return login(progress)


def login(progress: List) -> object:
    print("===========            로그인을 진행합니다.            ==========\n")
    usr_cnt, pw_cnt = 0, 0


    user = user_validation()
    if user == "7":
        progress.append("7")
        return sign_up(progress)

    password = password_validation2(user)

    my_info["user"] = user
    my_info["is_logined"] = True
    print(f"   {my_info['user'][2]}님, 어서오세요. 환영합니다")
    print(my_info)
    return my_info


def logout(progress: List) -> object:
    print("   로그아웃 되었습니다.")
    my_info["user"] = None
    my_info["is_logined"] = False
    return my_info

