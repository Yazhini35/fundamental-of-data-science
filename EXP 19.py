import numpy as np
from scipy import stats

# Sample data: daily temperatures in degrees Celsius
temperatures = np.array([22, 24, 21, 23, 25, 30, 19, 31, 28, 20, 24, 22, 25, 30, 29, 27, 32, 26, 23, 24])

# Calculate the variance of the temperatures
variance = np.var(temperatures)

# Calculate the Z-scores for identifying outliers
z_scores = np.abs(stats.zscore(temperatures))

# Define a threshold for identifying outliers (e.g., Z-score > 2)
threshold = 2
outliers = np.where(z_scores > threshold)

# Display the results
print(f"Variance of temperatures: {variance:.2f}")

print("\nPotential outliers (indices and values):")
for index in outliers[0]:
    print(f"Index: {index}, Temperature: {temperatures[index]}")
