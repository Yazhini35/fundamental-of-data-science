import pandas as pd

# Sample data: DataFrame containing sales data with customer ages
data = {
    'customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'purchase_amount': [100, 150, 200, 250, 300, 350, 400, 450, 500, 550],
    'age': [22, 35, 40, 29, 23, 45, 32, 38, 26, 41]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate the frequency distribution of ages
age_frequency = df['age']

# Display the frequency distribution
print("Frequency distribution of customer ages:")
print(age_frequency)
