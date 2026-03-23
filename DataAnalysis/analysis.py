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

    df["total_amount"] = df["quantity"] * df["unit_price"]
    pass

def add_time_features(df):
    """
    Add time-based features:
    - day_of_week (0=Monday, 6=Sunday)
    - month
    - quarter
    - is_weekend (boolean)
    """
    df["day_of_week"] = df["order_date"].dt.weekday
    df["month"] = df["order_date"].dt.month
    df["quarter"] = df["order_date"].dt.quarter
    df["is_weekend"] = df["day_of_week"] >= 5

def sales_by_category(df):
    """
    Calculate total sales and order count by category.
    Returns: DataFrame with columns [category, total_sales, order_count, avg_order_value]
    Sorted by total_sales descending.
    """
    result = (
        df.assign(sales=df["quantity"] * df["unit_price"])
        .groupby("category")
        .agg(
            total_amount=("sales", "sum"),
            order_count=("order_id", "count"),
            avg_order_value=("sales", "mean")
        )
        .reset_index()
        .sort_values(by="total_amount", ascending=False)
    )

    return result

def sales_by_region(df):
    """
    Calculate total sales by region.
    Returns: DataFrame with columns [region, total_sales, percentage_of_total]
    """
    df = df.assign(sales=df["quantity"] * df["unit_price"])

    # total sales across all regions
    total_sales_all = df["sales"].sum()

    # group by region
    result = (
        df.groupby("region")
        .agg(total_sales=("sales", "sum"))
        .reset_index()
    )

    # calculate percentage of total
    result["percentage_of_total"] = (result["total_sales"] / total_sales_all) * 100

    return result

def top_products(df, n=10):
    """
    Find top N products by total sales.
    Returns: DataFrame with columns [product_name, category, total_sales, units_sold]
    """
    
    result = (
        df.groupby("product_name")
        .agg(
            category=("category","first"),
            total_sales=("total_amount", "sum"),
            units_sold=("quantity", "sum")
            )
        .sort_values(by="total_sales", ascending=False)
    )
    
    return result

def daily_sales_trend(df):
    """
    Calculate daily sales totals.
    Returns: DataFrame with columns [date, total_sales, order_count]
    """
    result = (
        df.groupby("day_of_week")
        .agg(
            category=("order_date","first"),
            total_sales=("total_amount", "sum"),
            order_count=("order_id", "sum")
            )
        .sort_values(by="total_sales", ascending=False)
    )
    return result

def customer_analysis(df):
    """
    Analyze customer purchasing behavior.
    Returns: DataFrame with columns [customer_id, total_spent, order_count, 
             avg_order_value, favorite_category]
    """
    result = (
        df.groupby("customer_id")
        .agg(
            total_spent=("total_amount","sum"),
            order_count=("customer_id", "sum"),
            avg_order_value=("total_amount", "mean"),
            favorite_category=("category", lambda x: x.mode()[0])
            )
        .sort_values(by="total_spent", ascending=False)
    )
    return result

def weekend_vs_weekday(df):
    """
    Compare weekend vs weekday sales.
    Returns: Dict with weekend and weekday total sales and percentages.
    """
    pass

df = load_data("orders.csv")
print(df)
# print(sales_by_region(df))
# print(top_products(df))
add_time_features(df)
print(customer_analysis(df))