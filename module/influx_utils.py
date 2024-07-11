from datetime import datetime, timedelta
import pandas as pd

def ticks_to_rfc3339(ticks: int) -> str:
    """
    Convert a tick value (100 nanoseconds intervals since 1601-01-01) to a datetime string in RFC3339 format.
    
    :param ticks: The number of ticks.
    :return: A string representing the datetime in RFC3339 format.
    """
    # Convert ticks to seconds (100 nanoseconds per tick)
    seconds = ticks / 10_000_000

    # Convert seconds to days
    days = seconds / (60 * 60 * 24)

    # Adjust for the epoch of Excel (109205 days difference between 1601-01-01 and 1899-12-31)
    excel_epoch_adjustment = 109205
    excel_days = days - excel_epoch_adjustment

    # Separate the date and time parts
    date_part = int(excel_days)
    time_part = excel_days - date_part

    # Convert to a datetime object
    excel_start_date = datetime(1899, 12, 30)  # Excel's epoch start date (2 days before 1900-01-01)
    result_date = excel_start_date + timedelta(days=date_part)
    result_time = timedelta(days=time_part)

    # Combine date and time parts
    result_datetime = result_date + result_time

    # Format the result in RFC3339 format
    result_str = result_datetime.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

    return result_str

def generate_headers_from_dataframe(df):
    """
    Generate headers string based on DataFrame column data types.

    Parameters:
    - df (pandas.DataFrame): The DataFrame to generate headers from.

    Returns:
    - str: Generated headers string.
    """
    headers_temp = "#datatype "
    for column, dtype in df.dtypes.items():
        if column == "_time":
            headers_temp += "dateTime:RFC3339"
        elif dtype == "float64":
            headers_temp += ",double"
        elif dtype == "object":
            headers_temp += ",string"

    return headers_temp