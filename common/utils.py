from typing import Iterable, List

import pandas as pd
from pandas import DataFrame


def iter_to_df(iterable_data: Iterable, column_names: List) -> DataFrame:
    df = pd.DataFrame(iterable_data, columns=column_names)
    df.index = range(1, len(df) + 1)
    return df

