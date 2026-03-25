import csv
import datetime
import random
import string

# Generate a random customer name
def generate_customer_name():
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10))

# Generate a random email
def generate_email():
    username = ''.join(random.choices(string.ascii_lowercase, k=5))
    domain = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    return f"{username}@{domain}.com"

# Generate a random order date
def generate_order_date():
    return (datetime.datetime.now() + datetime.timedelta(days=random.randint(-30, 30))).strftime("%Y-%m-%d")

# Generate a random amount
def generate_amount():
    return random.randint(-100, 1000)

# Generate a random status
def generate_status():
    return random.choice(['pending', 'completed', 'cancelled'])

# Generate sample data with data quality issues
def generate_sample_data():
    sample_data = []
    for i in range(50):
        row = {
            'order_id': i,
            'customer_name': generate_customer_name(),
            'email': generate_email(),
            'order_date': generate_order_date(),
            'amount': generate_amount(),
            'status': generate_status()
        }
        if i < 3:
            row['customer_name'] = None
        if i < 2:
            row['order_id'] = random.randint(0, 49)
        if i < 2:
            row['amount'] = -generate_amount()
        if i == 4:
            row['email'] = 'invalidemail.com'
        if i == 9:
            row['order_date'] = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d")
        sample_data.append(row)
    return sample_data

# Write sample data to a CSV file
def write_to_csv(sample_data):
    with open('sample_data.csv', 'w', newline='') as csvfile:
        fieldnames = ['order_id', 'customer_name', 'email', 'order_date', 'amount', 'status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in sample_data:
            writer.writerow(row)

sample_data = generate_sample_data()
write_to_csv(sample_data)