import numpy as np

# Sample data: response times in milliseconds
response_times = [120, 150, 200, 300, 250, 100, 170, 180, 220, 90]

# Calculate the 25th, 50th, and 75th percentiles
percentiles = np.percentile(response_times, [25, 50, 75])

# Display the results
print(f"25th percentile: {percentiles[0]} ms")
print(f"50th percentile (median): {percentiles[1]} ms")
print(f"75th percentile: {percentiles[2]} ms")
