import re
from typing import List
from time import sleep


def username_validation(username: str, users: List):
    usr_cnt = 0
    while True:
        username_check = map(lambda x: x[1] == username, users)
        if True not in username_check:
            return True  # 중복 검사 통과
        usr_cnt += 1
        if usr_cnt == 3:
            print("3회 이상 실패하였으므로 초기 메뉴로 돌아갑니다.")
            sleep(0.5)
            for i in range(3):
                print(3 - i)
                sleep(0.5)
            return False  # 중복 검사 실패
        username = input(f"이미 가입된 정보가 있습니다. ({usr_cnt}/3)  사용자명을 다시 입력해주세요. : ")