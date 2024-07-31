import pandas as pd
import matplotlib.pyplot as plt

# Sample data for monthly sales
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Sales': [1500, 1800, 1700, 2000, 2300, 2100, 2500, 2700, 2600, 3000, 3200, 3100]
}

# Create DataFrame
df = pd.DataFrame(data)

# Bar Plot for Monthly Sales
plt.figure(figsize=(10, 6))
plt.bar(df['Month'], df['Sales'], color='skyblue')
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
