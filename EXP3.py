import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the Dataset
# Sample data for the sales data
data = {
    'Date': pd.date_range(start='2023-01-01', periods=365, freq='D'),
    'Category': ['Electronics', 'Clothing', 'Home', 'Books', 'Toys', 'Electronics', 'Clothing', 'Home', 'Books', 'Toys'] * 36 + ['Electronics', 'Clothing', 'Home', 'Books', 'Toys'],
    'Sales': [1500, 500, 1000, 300, 700, 1200, 600, 1100, 350, 650] * 36 + [1600, 550, 1050, 330, 720]
}

# Create DataFrame
df = pd.DataFrame(data)

# Step 2: Aggregate Sales by Category
category_sales = df.groupby('Category')['Sales'].sum().reset_index()

# Step 3: Create Visualizations

# Line Plot
plt.figure(figsize=(10, 6))
sns.lineplot(x='Category', y='Sales', data=category_sales, marker='o')
plt.title('Sales Distribution Across Product Categories - Line Plot')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.grid(True)
plt.show()

# Scatter Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Category', y='Sales', data=category_sales, s=100)
plt.title('Sales Distribution Across Product Categories - Scatter Plot')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.grid(True)
plt.show()

# Bar Plot
plt.figure(figsize=(10, 6))
sns.barplot(x='Category', y='Sales', data=category_sales, palette='viridis')
plt.title('Sales Distribution Across Product Categories - Bar Plot')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.show()
