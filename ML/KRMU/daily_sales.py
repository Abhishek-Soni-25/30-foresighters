import pandas as pd
import matplotlib.pyplot as plt

# Load sales data
sales_data = pd.read_json("sales_data.json")

# Convert date column to datetime format
sales_data['date'] = pd.to_datetime(sales_data['date'])

# Aggregate total sales for each day

daily_sales = sales_data.groupby('date')['total_earning'].sum().reset_index()

# Plotting daily sales trends
plt.figure(figsize=(10, 6))
plt.plot(daily_sales['date'], daily_sales['total_earning'], marker='o', linestyle='-')
plt.title('Daily Sales Trends')
plt.xlabel('Date')
plt.ylabel('Total Sales Amount')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
