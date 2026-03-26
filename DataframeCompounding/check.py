import pandas as pd

def calculate_order_total(orders_df):
    """
    Calculate total per order including tax.

    This function takes a dataframe containing order information and calculates
    the total for each order. It does this by:

    1. Calculating the total for each line item (quantity x unit_price)
    2. Calculating the tax for each line item (line_total x 0.08)
    3. Calculating the total for each line item including tax (line_total + tax)
    4. Grouping the dataframe by order_id and calculating the subtotal,
       total tax, and grand total for each order.
    """
    orders_df['line_total'] = orders_df['quantity'] * orders_df['unit_price']
    orders_df['tax'] = orders_df['line_total'] * 0.08
    orders_df['line_with_tax'] = orders_df['line_total'] + orders_df['tax']
    
    totals = orders_df.groupby('order_id').agg(
        subtotal=('line_total', 'sum'),
        total_tax=('tax', 'sum'),
        grand_total=('line_with_tax', 'sum')
    ).reset_index()
    
    return orders_df, totals

df = pd.read_csv('test_data.csv')
print("no function runs yet")
print(df)

newdf, totals = calculate_order_total(df)
print("one function run so far")
print(newdf)
print(totals)

newdf, totals = calculate_order_total(newdf)
print("two function runs so far")
print(newdf)
print(totals)