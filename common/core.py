import csv
import sys
from time import sleep
from typing import List
from tabulate import tabulate

from books.models import Books
from common.database import DatabaseManager
from common.utils import clearing, wait_clear
from common.validation import stand_by_validation


def create_table(tables: List, queries: List):
    for table, query in zip(tables, queries):
        DatabaseManager(table, query).execute_query()


def stand_by():
    while True:
        print("\n   =======            시스템 대기 화면            =======")
        is_stood_by = stand_by_validation()
        if is_stood_by == 1:
            wait_clear()
            return -1
        if is_stood_by == 3:
            sleep(0.3)
            print("\n   =======            시스템을 종료합니다.            =======")
            wait_clear()
            sys.exit()
        clearing()


def render_table(data, table_name):
    headers = []
    if table_name =="users":
        headers = ["ID", "사용자명", "성함", "패스워드"]
    elif table_name =="books":
        headers = ["ID", "제목", "저자", "출판사", "대출가능여부", "대출일", "반납일"]
        headers = headers[:len(data[0])+1]
    elif table_name == "loans":
        headers = ["ID", "사용자 ID", "도서 ID", "대출일", "반납일"]

    table = tabulate(data, headers=headers, tablefmt="fancy_grid",
                     showindex=True, numalign='center', stralign='left', maxcolwidths=30)
    table_lines = table.split("\n")
    table_lines_modified = ["   " + line for line in table_lines]
    table = "\n".join(table_lines_modified)

    return table


def from_csv_to_db(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i == 0:
                continue
            if row[2] and row[3] and row[4]:
                Books(row[2], row[3], row[4]).post()
