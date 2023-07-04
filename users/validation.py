import re
from typing import List
from time import sleep


def username_validation(username: str, users: List):
    usr_cnt = 0
    while True:
        username_check = map(lambda x: x[1] == username, users)
        if True not in username_check:
            return username  # 중복 검사 통과
        usr_cnt += 1
        if usr_cnt == 3:
            print("3회 이상 실패하였으므로 초기 메뉴로 돌아갑니다.")
            sleep(0.5)
            for i in range(3):
                print(3 - i)
                sleep(0.5)
            return False  # 중복 검사 실패
        username = input(f"이미 가입된 정보가 있습니다. ({usr_cnt}/3)  사용자명을 다시 입력해주세요. : ")


def password_validation(password: str, users: List):
    pw_cnt = 0

    match = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
    validation = re.compile(match)

    while True:
        if validation.match(password) is not None:
            return password
        pw_cnt += 1
        if pw_cnt == 3:
            print("3회 이상 실패하였으므로 초기 메뉴로 돌아갑니다.")
            sleep(0.5)
            for i in range(3):
                print(3 - i)
                sleep(0.5)
            return False
        password = input(f"비밀번호는 하나 이상의 문자, 숫자, 특수문자를 포함하여 8자리 이상으로 작성해주세요. ({pw_cnt}/3)  : ")
