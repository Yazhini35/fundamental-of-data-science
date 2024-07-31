import numpy as np

# Sample data: monthly expenses of different departments (in dollars)
# Each row represents a department, and each column represents a month
expenses = np.array([
    [2000, 2100, 2200, 2300, 2400],  # Department 1
    [1500, 1600, 1700, 1800, 1900],  # Department 2
    [3000, 3100, 3200, 3300, 3400]   # Department 3
])

# Calculate the variance of the monthly expenses for each department
variance = np.var(expenses, axis=1)

# Calculate the covariance matrix of the monthly expenses
covariance_matrix = np.cov(expenses)

# Display the results
print("Variance of monthly expenses for each department:")
print(variance)

print("\nCovariance matrix of monthly expenses:")
print(covariance_matrix)
