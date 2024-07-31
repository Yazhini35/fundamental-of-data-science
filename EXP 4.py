import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the Dataset
# Sample data for monthly temperature and rainfall
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Temperature': [30, 32, 35, 40, 45, 50, 55, 54, 50, 45, 35, 30],
    'Rainfall': [2.1, 1.8, 2.5, 3.0, 3.2, 3.5, 3.8, 3.7, 3.4, 3.0, 2.5, 2.2]
}

# Create DataFrame
df = pd.DataFrame(data)

# Step 2: Create Visualizations

# Line Plot for Temperature
plt.figure(figsize=(10, 6))
sns.lineplot(x='Month', y='Temperature', data=df, marker='o', color='red')
plt.title('Monthly Temperature')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Line Plot for Rainfall
plt.figure(figsize=(10, 6))
sns.lineplot(x='Month', y='Rainfall', data=df, marker='o', color='blue')
plt.title('Monthly Rainfall')
plt.xlabel('Month')
plt.ylabel('Rainfall (inches)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Scatter Plot for Temperature
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Month', y='Temperature', data=df, s=100, color='red')
plt.title('Monthly Temperature')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Scatter Plot for Rainfall
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Month', y='Rainfall', data=df, s=100, color='blue')
plt.title('Monthly Rainfall')
plt.xlabel('Month')
plt.ylabel('Rainfall (inches)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
