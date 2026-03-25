import pandas as pd
from quality_checks import check_nulls, check_duplicates, check_negative_values, check_future_dates, check_email_format

def generate_report(df: pd.DataFrame):
    """
    Generate a data quality report for the given DataFrame.
    """
    report = {
        'generated': pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S'),
        'file': 'sample_data.csv',
        'total_rows': len(df),
        'summary': {
            'checks': {
                'null_values': {
                    'status': 'WARNING',
                    'issues_found': check_nulls(df)['null_columns']
                },
                'duplicates': {
                    'status': 'FAIL',
                    'issues_found': check_duplicates(df)  # Use the list returned by check_duplicates
                },
                'negative_values': {
                    'status': 'WARNING',
                    'issues_found': check_negative_values(df)['negative_columns']
                },
                'future_dates': {
                    'status': 'WARNING',
                    'issues_found': check_future_dates(df)['future_columns']
                },
                'email_format': {
                    'status': 'WARNING',
                    'issues_found': check_email_format(df)['invalid_email_columns']
                }
            }
        },
        'detailed_results': {
            'null_values': check_nulls(df),
            'duplicates': check_duplicates(df),
            'negative_values': check_negative_values(df),
            'future_dates': check_future_dates(df),
            'email_format': check_email_format(df)
        }
    }
    return report

# Example usage
df = pd.read_csv('sample_data.csv')
report = generate_report(df)
print(report)