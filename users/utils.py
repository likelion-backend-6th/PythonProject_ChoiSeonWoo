import re
from time import sleep

from users.models import Users

my_info = {"user": None, "is_logined": False}



def sign_up():
    usr_cnt, pw_cnt = 0, 0

    users = Users().get()

    username = input("사용자명을 입력해주세요. : ")
    username_check = map(lambda x: x[1] == username, users)
    while True in username_check:
        usr_cnt += 1
        username = input(f"이미 가입된 정보가 있습니다. ({usr_cnt}/3)  사용자명을 다시 입력해주세요. : ")
        username_check = map(lambda x: x[1] == username, users)
        if usr_cnt == 3:
            print("3회 이상 실패하였으므로 초기 메뉴로 돌아갑니다.")
            sleep(0.5)
            for i in range(3):
                print(3 - i)
                sleep(0.5)
            sign_up()

    fullname = input("성함을 입력해주세요. : ")

    password = input("비밀번호를 입력해주세요. : ")

    match = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
    validation = re.compile(match)

    while validation.match(str(password)) == None:
        pw_cnt += 1
        password = input(f"비밀번호는 하나 이상의 문자, 숫자, 특수문자를 포함하여 8자리 이상으로 작성해주세요. ({pw_cnt}/3)  : ")
        if pw_cnt == 3:
            print("3회 이상 실패하였으므로 초기 메뉴로 돌아갑니다.")
            sleep(0.5)
            for i in range(3):
                print(3 - i)
                sleep(0.5)
            sign_up()

    new_user = Users(username, fullname, password)
    new_user.post()

    print("회원가입이 완료되었습니다.")
    print("이어서 로그인을 바로 진행하도록 하겠습니다.")
    return login()

def login() -> object:
    usr_cnt, pw_cnt = 0, 0

    username = input("사용자명을 입력해주세요. : ")
    user = Users(username).get()
    while not user:
        usr_cnt += 1
        username = input(f"조회되는 정보가 없습니다. ({usr_cnt}/3)  사용자명을 다시 입력해주세요. : ")
        user = Users(username).get()
        if usr_cnt == 3:
            print("3회 이상 실패하였으므로 초기 메뉴로 돌아갑니다.")
            sleep(0.5)
            for i in range(3):
                print(3 - i)
                sleep(0.5)
            login()

    password = input("비밀번호를 입력해주세요. : ")
    while user[0][-1] != password:
        pw_cnt += 1
        password = input(f"비밀번호가 일치하지 않습니다. ({pw_cnt}/3)  다시 입력해주세요. : ")
        if pw_cnt == 3:
            print("3회 이상 실패하였으므로 초기 메뉴로 돌아갑니다.")
            sleep(0.5)
            for i in range(3):
                print(3 - i)
                sleep(0.5)
            login()

    my_info["user"] = user
    my_info["is_logined"] = True
    print(f"{my_info['user'][0][2]}님, 어서오세요. 환영합니다")
    print(my_info)
    return my_info


def logout() -> object:
    print("로그아웃 되었습니다.")
    my_info["user"] = None
    my_info["is_logined"] = False
    return my_info


# login()
#
# if input("로그아웃 하시겠습니까? : ") == "예":
#     logout()
#
# print(f"my_info: {my_info}")


sign_up()