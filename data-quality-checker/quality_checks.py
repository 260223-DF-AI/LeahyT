import pandas as pd

def check_nulls(df: pd.DataFrame) -> dict:
    """
    Check for null values in the DataFrame and return a dictionary of columns with null values.
    """
    null_columns = df.columns[df.isnull().any()].tolist()
    return {"null_columns": null_columns}

def check_duplicates(df: pd.DataFrame) -> list:
    """
    Check for duplicates in the DataFrame and return a list of columns with duplicate values.
    """
    duplicate_columns = []
    for col in df.columns:
        if df[col].duplicated().sum() > 0:
            duplicate_columns.append(col)
    return duplicate_columns

def check_negative_values(df: pd.DataFrame) -> dict:
    """
    Check for negative values in the DataFrame and return a dictionary of columns with negative values.
    """
    # Convert values in the DataFrame to numeric types
    df = df.select_dtypes(include=['int64', 'float64']).copy()
    negative_columns = df.columns[(df < 0).any()].tolist()
    return {"negative_columns": negative_columns}

def check_future_dates(df: pd.DataFrame) -> dict:
    """
    Check for future dates in the DataFrame and return a dictionary of columns with future dates.
    """
    future_columns = df.columns[(df > pd.Timestamp.now()).any()].tolist()
    return {"future_columns": future_columns}

def check_email_format(df: pd.DataFrame) -> dict:
    """
    Check for email format in the DataFrame and return a dictionary of columns with invalid email format.
    """
    invalid_email_columns = df.columns[df['email'].str.contains('@') == False].tolist()
    return {"invalid_email_columns": invalid_email_columns}