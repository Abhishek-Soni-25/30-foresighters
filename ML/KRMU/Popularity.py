import pandas as pd
import json
from collections import defaultdict

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

# Group by product ID and sum the quantity sold
product_sales = sales_df.groupby('product_id')['quantity_sold'].sum().reset_index()

# Display the total quantity sold for each product
print(product_sales)




# Sort the product sales DataFrame by 'quantity_sold' in descending order
best_selling_products = product_sales.sort_values(by='quantity_sold', ascending=False)

# Display the top-selling products
print("Top Selling Products:")
print(best_selling_products)

# Visualize the popularity of different products
import matplotlib.pyplot as plt

# Plot the top-selling products
plt.figure(figsize=(10, 6))
plt.bar(best_selling_products['product_id'], best_selling_products['quantity_sold'])
plt.xlabel('Product ID')
plt.ylabel('Quantity Sold')
plt.title('Top Selling Products')
plt.xticks(rotation=45)
plt.show()
