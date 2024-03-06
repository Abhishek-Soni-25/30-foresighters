import pandas as pd
import matplotlib.pyplot as plt

# Read the sales data from the JSON file
sales_data = pd.read_json("sales_data.json")

# Convert the 'date' column to datetime format
sales_data['date'] = pd.to_datetime(sales_data['date'])

# Extract the month from the 'date' column and create a new column for it
sales_data['month'] = sales_data['date'].dt.month

# Group the sales data by month and calculate the total sales for each month
monthly_sales = sales_data.groupby('month')['total_earning'].sum()

# Plot the monthly sales trends
plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='bar', color='skyblue')
plt.title('Monthly Sales Trends')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
