import numpy as np

# Sample data: recovery times in days
recovery_times = [5, 7, 8, 6, 7, 9, 10, 6, 5, 8, 7, 6, 9, 10, 8, 6, 5, 9, 7, 8]

# Calculate the 10th, 50th, and 90th percentiles
percentiles = np.percentile(recovery_times, [10, 50, 90])

# Display the results
print(f"10th percentile: {percentiles[0]} days")
print(f"50th percentile (median): {percentiles[1]} days")
print(f"90th percentile: {percentiles[2]} days")
