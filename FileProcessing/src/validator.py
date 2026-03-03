from exceptions import *

def validate_sales_record(record, line_number):
    """
    Validate a single sales record.
    
    Required fields: date, store_id, product, quantity, price
    Validation rules:
    - date must be in YYYY-MM-DD format
    - quantity must be a positive integer
    - price must be a positive number
    
    Returns: Validated record with converted types
    Raises: InvalidDataError or MissingFieldError
    """
    # make sure all entries are in the record
    for key in record:
        if key not in ["date", "store_id", "product", "quantity", "price"]:
            raise MissingFieldError
    
    # verify that date is in yyyy-mm-dd format with integers and correct range of values
    try:
        # get all values in date as a list, then verify depending on type
        dateList = record["date"].split("-")
        
        # verify all common things between dates like is integer or <= 0
        for number in dateList:
            # convert date number to integer
            number = int(number)
            if number <= 0:
                raise ValueError
            
        # make sure year, month and day are in proper range
        if dateList[0] < 1900 or dateList[0] > 2026:
            raise ValueError
        
        if dateList[1] > 12:
            raise ValueError

        if dateList[2] > 31:
            raise ValueError
        
    except ValueError as e:
        print(f"Error: {e}. Date must be valid.")
        raise InvalidDataError

    except Exception as e:
        print(f"Error: {e}. Date must be integers in yyyy-mm-dd format.")
        raise InvalidDataError
    
    # verify quantity is an integer greater than 0
    try:
        record["quantity"] = int(record["quantity"])
        if record["quantity"] <= 0:
            raise ValueError
    except Exception as e:
        print(f"Error: {e}. Quantity must be a positive integer.")
        raise InvalidDataError
    
    # verify price is a float greater than 0
    try:
        record["price"] = float(record["price"])
        if record["price"] <= 0.0:
            raise ValueError
    except Exception as e:
        print(f"Error: {e}. Price must be a positive float.")
        raise InvalidDataError
    
    return record
def validate_all_records(records):
    """
    Validate all records, collecting errors instead of stopping.
    
    Returns: Tuple of (valid_records, error_list)
    """
    valid_records = []
    error_list = []
    for i, record in enumerate(records):
        try:
            validate_sales_record(record, i)
            valid_records.append(record)
        except Exception as e:
            error_list.append(e)
    return (valid_records, error_list)