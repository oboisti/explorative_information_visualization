from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import helper_functions.constants as c

def get_one_day_from_df(df, first_day, current_day_number):
    """Returns only the rows corresponding to the given day from the dataframe"""
    start_day = first_day + timedelta(days = current_day_number%365)
    next_day = start_day + timedelta(days = 1)

    return df[(df.index >= start_day) & (df.index < next_day)]

def get_one_average_day_from_df(df: pd.DataFrame, first_date: datetime, current_day_number: datetime, average_over: int, multipliers: np.array(int)) -> pd.DataFrame:
    """Return rows for one day. The rows have been formed by averaging the values over several days."""
    if average_over < 2:
        return get_one_day_from_df(df, first_date, current_day_number)

    original_date = first_date + timedelta(days = current_day_number%365)
    next_date = original_date + timedelta(days = 1)

    this_day= df[(df.index >= original_date) & (df.index < next_date)]

    for i in range(1, average_over):
        current_date = first_date + timedelta(days = (current_day_number + i)%365)
        next_date = current_date + timedelta(days = 1)
        next_day = df[(df.index >= current_date) & (df.index < next_date)]
        next_day.index = next_day.index + pd.DateOffset((original_date - current_date).days)
        this_day = this_day.combine(next_day, lambda a, b: a+b)

    return pd.DataFrame(this_day/average_over) * multipliers
