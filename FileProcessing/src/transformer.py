def calculate_totals(records):
    """
    Calculate line totals (quantity * price) for each record.
    Returns: Records with added 'total' field
    """
    # calculate new total field for every record
    for record in records:
        record["total"] = record["quantity"] * record["price"]
    return records

def aggregate_by_store(records):
    """
    Aggregate sales by store_id.
    Returns: Dict mapping store_id to total sales
    """
    # initialize new dictionary representing each store and their total sales
    storeSaleTotals = {}
    
    # grab every record and add its total to appropriate store
    for record in records:
        # check if storeSaleTotals already has an entry for specific store, create one if needed
        if record["store_id"] in storeSaleTotals:
            storeSaleTotals[record["store_id"]] += record["total"]
        else:
            storeSaleTotals[record["store_id"]] = record["total"]
    
    return storeSaleTotals

def aggregate_by_product(records):
    """
    Aggregate sales by product.
    Returns: Dict mapping product to total quantity sold
    """
    # initialize new dictionary representing each store and their total sales
    productSaleTotals = {}
    
    # grab every record and add its total to appropriate store
    for record in records:
        # check if productSaleTotals already has an entry for specific store, create one if needed
        if record["product"] in productSaleTotals:
            productSaleTotals[record["product"]] += record["total"]
        else:
            productSaleTotals[record["product"]] = record["total"]
    
    return productSaleTotals