import re
from typing import List
from time import sleep

from users.models import Users


def username_validation():
    init_message = "   가입에 사용할 사용자명을 입력해주세요.\n" \
                   "   이미 가입된 회원의 경우, 로그인 메뉴로 이동하시려면 숫자 8을 입력해주세요.\n" \
                   "   (이전 메뉴로 돌아가려면 '-1'을 입력해주세요.)\n" \
                   "   --->  입력  :  "
    cnt = 0
    message = init_message
    users = Users().get()

    while True:
        username = input(message).replace(" ", "")
        username_check = map(lambda x: x[1] == username, users)
        if username in ["-1", "8"] or True not in username_check:
            return username

        cnt += 1
        message = f"\n   이미 가입된 정보가 있습니다. ({cnt}/3)\n"\
                   "   확인 후 사용자명을 다시 입력해주세요.\n" \
                   "   (이전 메뉴로 돌아가려면 '-1'을 입력해주세요.)\n" \
                   "   -->  사용자명 입력  :  "

        if cnt == 3:
            message, cnt = init_message, 0
            print("   3회 이상 실패하였으므로 초기 메뉴로 돌아갑니다.")
            sleep(0.5)
            for i in range(3):
                print(f"   {3 - i}")
                sleep(0.5)
            return "-1"


def password_validation():
    init_message = "   가입에 사용할 비밀번호를 입력해주세요.\n" \
                   "   (이전 메뉴로 돌아가려면 '-1'을 입력해주세요.)\n" \
                   "   --->  비밀번호 입력  :  "
    cnt = 0
    message = init_message
    match = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
    validation = re.compile(match)

    while True:
        password = input(message)
        if password == "-1" or validation.match(password) is not None:
            return password

        cnt += 1
        message = f"\n   비밀번호는 하나 이상의 문자, 숫자, 특수문자를 포함하여 8자리 이상으로 작성해주세요. ({cnt}/3)\n" \
                   "   확인 후 비밀번호를 다시 입력해주세요.\n" \
                   "   (이전 메뉴로 돌아가려면 '-1'을 입력해주세요.)\n" \
                   "   -->  비밀번호 입력  :  "

        if cnt == 3:
            message, cnt = init_message, 0
            print("   3회 이상 실패하였으므로 초기 메뉴로 돌아갑니다.")
            sleep(0.5)
            for i in range(3):
                print(f"   {3 - i}")
                sleep(0.5)
            return "-1"


def user_validation():
    init_message = "   사용자명을 입력해주세요.\n" \
                   "   회원가입을 진행하시려면 숫자 7을 입력해주세요.\n" \
                   "   (이전 메뉴로 돌아가려면 '-1'을 입력해주세요.)\n" \
                   "   --->  입력  :  "
    cnt = 0
    message = init_message

    while True:
        username = input(message)
        if username in ["-1", "7"]:
            return username
        user = Users().get(username=username)
        if user:
            return user

        cnt += 1
        message = f"\n   조회되는 유저 정보가 없습니다. ({cnt}/3)\n" \
                   "   (이전 메뉴로 돌아가려면 '-1'을 입력해주세요.)\n" \
                   "   확인 후 사용자명을 다시 입력해주세요.\n" \
                   "   -->  사용자명 입력  :  "

        if cnt == 3:
            message, cnt = init_message, 0
            print("   3회 이상 실패하였으므로 초기 메뉴로 돌아갑니다.")
            sleep(0.5)
            for i in range(3):
                print(f"   {3 - i}")
                sleep(0.5)
            return "-1"


def password_validation2(user: List):
    init_message = "   비밀번호를 입력해주세요.\n" \
                   "   (이전 메뉴로 돌아가려면 '-1'을 입력해주세요.)\n" \
                   "   --->  입력  :  "
    cnt = 0
    message = init_message

    while True:
        password = input(message)
        if password == "-1":
            return password
        if user[0][-1] == password:
            return True
        cnt += 1
        message = f"\n   비밀번호가 일치하지 않습니다. ({cnt}/3)\n" \
                   "   (이전 메뉴로 돌아가려면 '-1'을 입력해주세요.)\n" \
                   "   확인 후 다시 입력해주세요.\n" \
                   "   -->  비밀번호 입력  :  "

        if cnt == 3:
            print("   3회 이상 실패하였으므로 초기 메뉴로 돌아갑니다.")
            sleep(0.5)
            for i in range(3):
                print(f"   {3 - i}")
                sleep(0.5)
            return "-1"