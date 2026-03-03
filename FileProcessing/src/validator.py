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
            
        # maybe unneeded, but prevents sales from before 1900 and after 2026, also maybe could
        # use custom exception?
        if dateList[0] < 1900 or dateList[0] > 2026:
            raise ValueError
        
        if dateList[1] <=0 or dateList > 12:
            
    except Exception as e:
        print(f"Error: {e}. Date must be integers in yyyy-mm-dd format.")
        raise InvalidDataError

def validate_all_records(records):
    """
    Validate all records, collecting errors instead of stopping.
    
    Returns: Tuple of (valid_records, error_list)
    """
    pass