import pandas as pd
from dateutil import parser
from pandas.errors import ParserError
import datetime, re

def last_date(df, current_index, date_column):
    fill_date = 1
    new_date = ""
    while True:
        if df[date_column][current_index-fill_date] and df[date_column][current_index-fill_date] != "nan" and df[date_column][current_index-fill_date] != "n/a" and "nan" not in str(df[date_column][current_index-fill_date]):
            new_date = df[date_column][current_index-fill_date]
            break
        fill_date += 1
    return new_date

def convert_dates_to_mmddyyyy_format(csv_path, date_column):
    df = pd.read_csv(csv_path, on_bad_lines='skip')
    for i, date_str in enumerate(df[date_column]):
        try:
            date_obj = parser.parse(str(date_str), fuzzy=True)
            if date_obj.year >= 1900:
                df.at[i, date_column] = date_obj.strftime('%m/%d/%Y')
            else:
                df.at[i, date_column] = "n/a"
        except ValueError:
            df.at[i, date_column] = "n/a"
    df.to_csv(csv_path, index=False)

convert_dates_to_mmddyyyy_format("./0_archive_wayback_urls/wayback_stats.csv", "app_last_updated")
