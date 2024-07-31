import numpy as np

# Sample data: daily temperature readings for each city over a year
# Each row represents a city, and each column represents a day
# For example: temperatures[0] is the data for City 1, temperatures[1] is the data for City 2, and so on.
temperatures = np.array([
    [15, 16, 17, 16, 15, 14, 13, 14, 15, 16, 17, 18] * 30,  # City 1
    [10, 12, 13, 15, 16, 17, 18, 17, 16, 15, 14, 13] * 30,  # City 2
    [20, 22, 24, 26, 27, 28, 30, 29, 28, 27, 25, 23] * 30   # City 3
])

# Calculate the mean temperature for each city
mean_temperatures = np.mean(temperatures, axis=1)

# Calculate the standard deviation of temperature for each city
std_devs = np.std(temperatures, axis=1)

# Determine the city with the highest temperature range
temp_ranges = np.ptp(temperatures, axis=1)  # ptp is "peak-to-peak" (max - min)
city_highest_range = np.argmax(temp_ranges)

# Find the city with the most consistent temperature (lowest standard deviation)
city_most_consistent = np.argmin(std_devs)

# Display the results
print("Mean temperatures for each city:")
for i, mean_temp in enumerate(mean_temperatures, start=1):
    print(f"City {i}: {mean_temp:.2f}°C")

print("\nStandard deviation of temperatures for each city:")
for i, std_dev in enumerate(std_devs, start=1):
    print(f"City {i}: {std_dev:.2f}°C")

print(f"\nCity with the highest temperature range: City {city_highest_range + 1}")

print(f"City with the most consistent temperature (lowest standard deviation): City {city_most_consistent + 1}")
