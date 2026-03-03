from file_reader import *
from validator import *
from transformer import *
from report_writer import *

def process_sales_file(input_path, output_dir):
    """
    Main processing pipeline.
    
    1. Read the input file
    2. Validate all records
    3. Transform valid records
    4. Generate reports
    5. Handle any errors gracefully
    
    Returns: ProcessingResult with statistics
    """
    try:
        recordDictionary = read_csv_file(input_path)
        recordsAndErrors = validate_all_records(recordDictionary)
        recordDictionary = recordsAndErrors[0]
        errors = recordsAndErrors[1]
        recordDictionary = calculate_totals(recordDictionary)
        aggregatedTotals = [aggregate_by_store(recordDictionary), aggregate_by_product(recordDictionary)]
        write_summary_report(output_dir, recordDictionary, errors, aggregatedTotals)
        return True
    except Exception as e:
        print(e)
        return False

if __name__ == "__main__":
    process_sales_file("sample_sales.csv", "Summary_Report.txt")