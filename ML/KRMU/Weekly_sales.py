import pandas as pd
import matplotlib.pyplot as plt

# Load sales data
sales_data = pd.read_json("sales_data.json")



# Convert 'date' column to datetime format
sales_data['date'] = pd.to_datetime(sales_data['date'])

# Group the data by week and sum the total sales amount
weekly_sales = sales_data.resample('W-Mon', on='date').sum().reset_index()

# Plot the weekly sales trends
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(weekly_sales['date'], weekly_sales['total_earning'], marker='o', linestyle='-')
plt.title('Weekly Sales Trends')
plt.xlabel('Week')
plt.ylabel('Total Sales Amount')
plt.grid(True)
plt.show()