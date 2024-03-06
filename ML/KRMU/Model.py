
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error

sales_data = pd.read_json('customer_bills.json')

inventory_data = pd.read_json('inventory.json')


'''print("Sales Data:")  # Displaying the first few rows of the sales data
print(sales_data.head())


print("\nInventory Data:")  # Displaying the first few rows of the inventory data
print(inventory_data.head())
'''

'''# Check for missing values in the sales data
sales_missing_values = sales_data.isnull().sum()
print("Missing values in sales data:")
print(sales_missing_values)'''

"""# Check for missing values in the inventory data
inventory_missing_values = inventory_data.isnull().sum()
print("Missing values in inventory data:")
print(inventory_missing_values)
"""



import json

# Load sales data from JSON file
with open("sales_data.json", "r") as file:
    sales_data = json.load(file)

# Flatten the sales data
flattened_sales = []
for entry in sales_data:
    date = entry["date"]
    for sale in entry["sales"]:
        sale["date"] = date
        flattened_sales.append(sale)

# Convert flattened sales data to DataFrame
sales_df = pd.DataFrame(flattened_sales)

# Display the DataFrame
print(sales_df.head()) 




import pandas as pd

# Assuming you have loaded the sales data into a DataFrame named 'sales_df'
# If not, load the sales data from the appropriate source

# Step 1: Calculate the average daily sales for each product
daily_product_sales = sales_df.groupby(['product_id', 'date'])['quantity_sold'].sum().reset_index()
average_daily_sales = daily_product_sales.groupby('product_id')['quantity_sold'].mean().reset_index()

# Step 2: Forecast weekly demand for each product
days_in_week = 7
forecasted_demand = average_daily_sales.copy()
forecasted_demand['weekly_demand'] = forecasted_demand['quantity_sold'] * days_in_week

# Display the forecasted demand for each product
print(forecasted_demand)


