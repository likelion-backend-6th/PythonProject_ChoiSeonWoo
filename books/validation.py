from time import sleep


def fetch_type_validation(fetch_type: int):
    cnt = 0
    while True:
        if fetch_type in [1, 2]:
            return fetch_type
        cnt += 1
        if cnt == 3:
            print("   3회 이상 실패하였으므로 초기 메뉴로 돌아갑니다.")
            sleep(0.5)
            for i in range(3):
                print(f"   {3 - i}")
                sleep(0.3)
            return False
        sleep(0.2)
        fetch_type = int(input(f"   잘못 입력하였습니다. 번호를 다시 입력해주세요. ({cnt}/3)  :  "))
