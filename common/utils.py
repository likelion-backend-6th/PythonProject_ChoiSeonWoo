import sys
from typing import Iterable, List

import pandas as pd
from pandas import DataFrame
from tabulate import tabulate

from common.database import DatabaseManager
from common.validation import stand_by_validation


def create_table(tables: List, queries: List):
    for table, query in zip(tables, queries):
        DatabaseManager(table, query).execute_query()


def iter_to_df(iterable_data: Iterable, column_names: List) -> DataFrame:
    df = pd.DataFrame(iterable_data, columns=column_names)
    df.index = range(1, len(df) + 1)
    return df


def stand_by():
    while True:
        print("\n   =======            시스템 대기 화면            =======")
        is_stood_by = stand_by_validation()
        if is_stood_by == 1:
            return -1
        if is_stood_by == 3:
            sys.exit()


def render_table(data, table_name):
    headers = []
    if table_name =="users":
        headers = ["ID", "사용자명", "성함"]
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