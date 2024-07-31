import numpy as np
import statistics

# Sample data: purchase amounts in dollars
purchase_amounts = [50, 20, 30, 20, 50, 70, 50, 80, 30, 20, 50, 30, 20, 50, 70, 50, 80, 20]

# Calculate the mean (average) purchase amount
mean_purchase_amount = np.mean(purchase_amounts)

# Identify the mode of the purchase amounts
mode_purchase_amount = statistics.mode(purchase_amounts)

# Display the results
print(f"Mean (average) purchase amount: ${mean_purchase_amount:.2f}")
print(f"Mode (average) purchase amount: ${mode_purchase_amount:.2f}")
