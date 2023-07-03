from time import sleep

from users.models import Users

my_info = {"user": None, "is_logined": False}


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


login()

if input("로그아웃 하시겠습니까? : ") == "예":
    logout()

print(f"my_info: {my_info}")