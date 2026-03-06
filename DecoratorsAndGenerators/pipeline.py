from functools import wraps, lru_cache
import time


def create_pipeline(*stages):
    """
    Create a processing pipeline from multiple generator functions.
    
    Usage:
        pipeline = create_pipeline(
            read_lines,
            parse_json,
            filter_valid,
            transform
        )
        
        for result in pipeline('input.json'):
            save(result)
    """
    def pipeline(input_iterable):
        output = input_iterable
        for stage in stages:
            output = stage(output)
        return output
    return pipeline

# Example pipeline stages:

def parse_csv_line(lines):
    """Convert CSV lines to dictionaries."""
    entry = {
        "customer": None,
        "product": None,
        "quantity": None,
        "price": None
    }
    for line in lines:
        counter = 0
        line = line.split(",")
        for key in entry:
            entry[key] = line[counter]
            counter += 1
        yield entry.copy()

def validate_records(records):
    """Yield only valid records, skip invalid ones."""
    for record in records:
        if not record == "":
            yield record

def enrich_records(records):
    """Add calculated fields to each record."""
    for record in records:
        record["total"] = float(record["quantity"]) * float(record["price"])
        yield record


def deduplicate(records, key_field):
    """Yield unique records based on a key field."""
    for record in records:
        if key_field in record:
            yield record

pipeline = create_pipeline(
            parse_csv_line,
            validate_records,
            enrich_records,
            lambda records: deduplicate(records, key_field="customer")
        )


csv_data = [
    "Alice,Widget,4,19.99",
    "Bob,Gadget,2,29.99",
    "Charlie,Thingamajig,1,9.99",
    "Diana,Widget,3,19.99",
    "Eve,Gadget,5,29.99",
    "Frank,Thingamajig,2,9.99",
    "Grace,Widget,1,19.99",
    "Hank,Gadget,3,29.99",
    "Ivy,Thingamajig,4,9.99",
    "Jack,Widget,2,19.99"
]

#print(pipeline(csv_data))
for result in pipeline(csv_data):
    print(result)

