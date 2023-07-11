import os
from time import sleep
import sys


def clear_current_line():
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")


def clear_specific_line(line_number):
    for _ in range(line_number):
        clear_current_line()
        sys.stdout.write("\n")


def waiting():
    sleep(0.15)
    print("", end="   ")
    for i in range(3):
        print(".", end="", flush=True)
        sleep(0.15)
    clear_specific_line(3)


def clearing():
    os.system('cls' if os.name == 'nt' else 'clear')


def wait_clear():
    waiting()
    clearing()


def clear_wait_clear():
    clearing()
    waiting()
    clearing()
