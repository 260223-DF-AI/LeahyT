from datetime import datetime

def write_summary_report(filepath, valid_records, errors, aggregations):
    """
    Write a formatted summary report.
    
    Report should include:
    - Processing timestamp
    - Total records processed
    - Number of valid records
    - Number of errors (with details)
    - Sales by store
    - Top 5 products
    """
    # begin writing new file
    with open(filepath, 'w') as file:
        file.write(f"Total records processed: {len(valid_records) + len(errors)}")
        file.write(f"Number of valid records: {len(valid_records)}")
        file.write(f"Number of errors:        {len(errors)}")
        
        # write store total for each store
        for store, total in aggregations[0].items():
            file.write(f"{store} total sales: {total}")

        # write product total for each product, and get top 5 products with the most sales
        for product, total in aggregations[1].items():
            file.write(f"{product} total sales: {total}")

        topFive = sorted(aggregations[1], key=lambda x: x["total"], reverse=True)[:5]     
        file.write("Top 5 Products:")
        topCounter = 1
        for product, total in topFive.items():
            file.write(f"{topCounter}.    {product}: {total}")
            topCounter += 1   

def write_clean_csv(filepath, records):
    """
    Write validated records to a clean CSV file.
    """
    # simply write each record to a new file
    with open(filepath, "w") as file:
        for record in records:
            file.write(f"{record["date"]}, {record["store_id"]}, {record["product"]}, {record["quantity"]}, {record["price"]},")

def write_error_log(filepath, errors):
    """
    Write processing errors to a log file.
    """
    # simply write each error to a new file
    with open(filepath, "w") as file:
        for error in errors:
            file.write(error)