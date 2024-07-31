import pandas as pd
import pandas as pd

# Sample data to create the DataFrame
data = {
    'OrderID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'CustomerID': [101, 102, 103, 104, 101, 102, 105, 106, 107, 108],
    'ProductID': [1001, 1002, 1003, 1001, 1002, 1003, 1001, 1002, 1003, 1001],
    'Quantity': [2, 1, 5, 3, 2, 1, 4, 1, 2, 5],
    'TotalPrice': [20.0, 15.0, 50.0, 30.0, 20.0, 15.0, 40.0, 15.0, 30.0, 50.0]
}

# Create DataFrame
df = pd.DataFrame(data)
print(df)


# Step 2: Basic Exploration
print("Basic Info:")
print(df.info())
print("\nBasic Statistics:")
print(df.describe())
print("\nFirst 5 Rows:")
print(df.head())

# Step 3: Data Cleaning
# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Drop duplicates
df.drop_duplicates(inplace=True)

# Step 4: Data Analysis
# Total Revenue
total_revenue = df['TotalPrice'].sum()
print("\nTotal Revenue: $", total_revenue)

# Top 5 Customers by Total Spend
top_customers = df.groupby('CustomerID')['TotalPrice'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Customers by Total Spend:")
print(top_customers)

# Top 5 Products by Quantity Sold
top_products = df.groupby('ProductID')['Quantity'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Products by Quantity Sold:")
print(top_products)

# Number of Orders per Customer
orders_per_customer = df['CustomerID'].value_counts()
print("\nNumber of Orders per Customer:")
print(orders_per_customer.head(5))

# Average Order Value
average_order_value = df['TotalPrice'].mean()
print("\nAverage Order Value: $", average_order_value)
