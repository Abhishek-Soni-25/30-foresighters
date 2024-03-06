import json
import random
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker instance
fake = Faker()

# Function to generate unique bill ID
def generate_bill_id():
    return fake.uuid4()

# Function to generate fake sales record for a day
def generate_sales_record(date):
    sales = []
    total_earning = 0
    for product_id in range(1, 16):  # Assuming 15 products
        quantity_sold = random.randint(1, 50)  # Random quantity sold
        unit_price = random.randint(10, 100)  # Random unit price
        total_earning += quantity_sold * unit_price
        sales.append({"product_id": product_id, "quantity_sold": quantity_sold, "unit_price": unit_price})
    return {"date": date.strftime("%Y-%m-%d"), "sales": sales, "total_earning": total_earning}

# Function to generate fake customer bill
def generate_customer_bill(sales_record):
    bill_id = generate_bill_id()
    total_amount = 0
    bill_items = []
    for sale in sales_record["sales"]:
        product_id = sale["product_id"]
        quantity_sold = sale["quantity_sold"]
        unit_price = sale["unit_price"]
        amount = unit_price * quantity_sold
        total_amount += amount
        bill_items.append({"product_id": product_id, "quantity_sold": quantity_sold, "unit_price": unit_price, "amount": amount})
    return {"bill_id": bill_id, "date": sales_record["date"], "total_amount": total_amount, "items": bill_items}

# Generate sales records and customer bills data for a year
sales_records = []
customer_bills = []
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
current_date = start_date

while current_date <= end_date:
    sales_record = generate_sales_record(current_date)
    customer_bill = generate_customer_bill(sales_record)
    sales_records.append(sales_record)
    customer_bills.append(customer_bill)
    current_date += timedelta(days=1)

# Save sales records to sales_record.json
with open("sales_record.json", "w") as f:
    json.dump(sales_records, f, indent=4)

# Save customer bills to customer_bills.json
with open("customer_bills.json", "w") as f:
    json.dump(customer_bills, f, indent=4)

print("Sales records and customer bills data generated successfully.")
