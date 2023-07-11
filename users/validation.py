import re
from typing import List
from time import sleep

from users.models import Users


def username_validation():
    init_message = "\n   가입에 사용할 사용자명을 입력해주세요.\n" \
                   "   이미 가입된 회원의 경우, 로그인 메뉴로 이동하시려면 숫자 8을 입력해주세요.\n" \
                   "   (상위 메뉴로 돌아가려면 '-1'을 입력해주세요.)\n" \
                   "   --->  입력  :  "
    cnt = 0
    message = init_message
    match = "^(?=[a-z\d][-a-z\d_]{5,}$)(?!.*[-_]{2})[a-z\d][a-z\d_-]*$"
    validation = re.compile(match)
    users = Users().get()

    while True:
        username = input(message)

        if username in ["-1", "8"]:
            return username

        elif validation.match(username) is None or username.count("-") + username.count("_") > 2:
            error_message = "\n   알파벳 소문자로 시작하고 소문자, 숫자, 특수문자를 포함한 6자리 이상로 작성해주세요." \
                            "\n   특수문자는 하이픈(-)과 언더바(_)만 1개까지 사용 가능합니다.\n"
        elif any(user[1] == username for user in users):
            error_message = "\n   이미 가입된 정보가 있습니다.\n"
        else:
            return username

        cnt += 1
        message = error_message + f"   확인 후 사용자명을 다시 입력해주세요. ({cnt}/3)\n" \
                                   "   (상위 메뉴로 돌아가려면 '-1'을 입력해주세요.)\n" \
                                   "   -->  사용자명 입력  :  "

        if cnt == 3:
            message, cnt = init_message, 0
            print("   3회 이상 실패하였으므로 상위 메뉴로 돌아갑니다.")
            sleep(0.5)
            for i in range(3):
                print(f"   {3 - i}")
                sleep(0.3)
            return "-1"


def fullname_validation():
    init_message = "\n   성함을 입력해주세요.\n" \
                   "   (상위 메뉴로 돌아가려면 '-1'을 입력해주세요.)\n" \
                   "   --->  비밀번호 입력  :  "
    cnt = 0
    message = init_message
    match = "^(?=.*[A-Za-z])[A-Za-z](?:[A-Za-z\s]{0,1}[A-Za-z]){3,}$|^[가-힣]{2,}$"
    validation = re.compile(match)

    while True:
        fullname = input(message)
        if fullname == "-1" or validation.match(fullname) is not None:
            return fullname

        cnt += 1
        message = f"\n   2자 이상의 한글 혹은 5자 이상의 영문으로 작성해주세요. ({cnt}/3)\n" \
                  "   영문의 경우, 중간에 최대 1개의 공백을 허용합니다.\n" \
                  "   확인 후 성함을 다시 입력해주세요.\n" \
                  "   (상위 메뉴로 돌아가려면 '-1'을 입력해주세요.)\n" \
                  "   -->  성함 입력  :  "

        if cnt == 3:
            message, cnt = init_message, 0
            print("   3회 이상 실패하였으므로 상위 메뉴로 돌아갑니다.")
            sleep(0.5)
            for i in range(3):
                print(f"   {3 - i}")
                sleep(0.3)
            return "-1"



def password_validation():
    init_message = "\n   사용할 비밀번호를 입력해주세요.\n" \
                   "   (상위 메뉴로 돌아가려면 '-1'을 입력해주세요.)\n" \
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
                  "   (상위 메뉴로 돌아가려면 '-1'을 입력해주세요.)\n" \
                  "   -->  비밀번호 입력  :  "

        if cnt == 3:
            message, cnt = init_message, 0
            print("   3회 이상 실패하였으므로 상위 메뉴로 돌아갑니다.")
            sleep(0.5)
            for i in range(3):
                print(f"   {3 - i}")
                sleep(0.3)
            return "-1"


def user_validation():
    init_message = "   사용자명을 입력해주세요.\n" \
                   "   회원가입을 진행하시려면 숫자 7을 입력해주세요.\n" \
                   "   (상위 메뉴로 돌아가려면 '-1'을 입력해주세요.)\n" \
                   "   --->  입력  :  "
    cnt = 0
    message = init_message

    while True:
        username = input(message)
        if username in ["-1", "7"]:
            return username
        elif username.strip() != "":
            user = Users().get(username=username)
            if user:
                return user

        cnt += 1
        message = f"\n   조회되는 유저 정보가 없습니다. ({cnt}/3)\n" \
                   "   2자 이상의 한글 혹은 5자 이상의 영문으로 작성해주세요.\n" \
                   "   (상위 메뉴로 돌아가려면 '-1'을 입력해주세요.)\n" \
                   "   확인 후 사용자명을 다시 입력해주세요.\n" \
                   "   -->  사용자명 입력  :  "

        if cnt == 3:
            message, cnt = init_message, 0
            print("   3회 이상 실패하였으므로 상위 메뉴로 돌아갑니다.")
            sleep(0.5)
            for i in range(3):
                print(f"   {3 - i}")
                sleep(0.3)
            return "-1"


def password_validation2(user: List):
    init_message = "\n   비밀번호를 입력해주세요.\n" \
                   "   (상위 메뉴로 돌아가려면 '-1'을 입력해주세요.)\n" \
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
                  "   (상위 메뉴로 돌아가려면 '-1'을 입력해주세요.)\n" \
                  "   확인 후 다시 입력해주세요.\n" \
                  "   -->  비밀번호 입력  :  "

        if cnt == 3:
            print("   3회 이상 실패하였으므로 상위 메뉴로 돌아갑니다.")
            sleep(0.5)
            for i in range(3):
                print(f"   {3 - i}")
                sleep(0.3)
            return "-1"


def user_id_validation():
    init_message = "\n   유저의 ID를 입력해주세요.\n" \
                   "   (상위 메뉴로 돌아가려면 '-1'을 입력해주세요.)\n" \
                   "   --->  입력  :  "
    cnt = 0
    users = Users().get()
    message = init_message

    while True:
        try:
            user_id = int(input(message))
            if user_id == -1:
                return -1
            elif all(user[0] != user_id for user in users):
                error_message = "\n   해당 ID의 유저가 존재하지 않습니다.\n"
            for user in users:
                if user[0] == user_id:
                    return user
        except ValueError:
            error_message = "\n   ID는 숫자만 입력해야 합니다.\n"

        cnt += 1
        message = error_message + f"   확인 후 ID를 다시 입력해주세요. ({cnt}/3)\n" \
                                   "   (상위 메뉴로 돌아가려면 '-1'을 입력해주세요.)\n" \
                                   "   -->  메뉴 입력  :  "

        if cnt == 3:
            print("   3회 이상 실패하였으므로 상위 메뉴로 돌아갑니다.")
            sleep(0.5)
            for i in range(3):
                print(f"   {3 - i}")
                sleep(0.3)
            return -1