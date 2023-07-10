import sys
from typing import Iterable, List

import pandas as pd
from pandas import DataFrame

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
