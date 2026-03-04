import pandas as pd

def load_data(filepath):
    # create a new dataframe, then clean it with clean_data()
    df = pd.read_csv(filepath)
    clean_data(df)
    return df

def explore_data(df):
    """
    Print basic statistics about the dataset:
    - Shape (rows, columns)
    - Data types
    - Missing value counts
    - Basic statistics for numeric columns
    - Date range covered
    """
    # print tons of relevant data for the dataframe 
    print(df)
    print()
    print(f"The dataset has {df.shape[0]} rows, and {df.shape[1]} columns.")
    print()
    print("For each column, the type is:")
    for column in df.columns:
        print(f"{column}: {df.dtypes[column]}")
    print()    
    print(f"Data ranges from {df["order_date"].min().date()} to {df["order_date"].max().date()}")
    print()
    print(f"Total missing values: {df.isna().sum().sum()}")

def clean_data(df):
    """
    Clean the dataset:
    - Remove duplicates
    - Fill or drop missing values (document your strategy)
    - Standardize text columns (strip whitespace, consistent case)
    - Add calculated columns: 'total_amount' = quantity * unit_price
    """
    # drop duplicates and na's
    df.drop_duplicates()
    df.dropna(axis = 0, inplace = True, how = "any")

    # strip whitespace from strings
    df["customer_id"] = df["customer_id"].str.strip()
    df["product_name"] = df["product_name"].str.strip()
    df["category"] = df["category"].str.strip()
    df["region"] = df["region"].str.strip()

    df["order_date"] = pd.to_datetime(df["order_date"], errors='coerce')

    pass

def add_time_features(df):
    """
    Add time-based features:
    - day_of_week (0=Monday, 6=Sunday)
    - month
    - quarter
    - is_weekend (boolean)
    """
    pass

df = load_data("orders.csv")
explore_data(df)