import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    'City': ['CityA', 'CityA', 'CityA', 'CityB', 'CityB', 'CityB', 'CityC', 'CityC', 'CityC'],
    'Temperature': [23.5, 25.1, 22.9, 30.2, 29.8, 31.4, 18.5, 17.9, 19.1]
}

df = pd.DataFrame(data)

# Group the data by city
grouped = df.groupby('City')

# Calculate mean temperature for each city
mean_temperatures = grouped['Temperature'].mean()

# Calculate standard deviation of temperature for each city
std_dev_temperatures = grouped['Temperature'].std()

# Calculate the temperature range for each city (max - min)
temperature_ranges = grouped['Temperature'].max() - grouped['Temperature'].min()

# Find the city with the highest temperature range
city_with_highest_range = temperature_ranges.idxmax()
highest_range = temperature_ranges.max()

# Find the city with the most consistent temperature (lowest standard deviation)
city_with_lowest_std_dev = std_dev_temperatures.idxmin()
lowest_std_dev = std_dev_temperatures.min()

# Print results
print("Mean Temperatures for each city:")
print(mean_temperatures)
print("\nStandard Deviation of Temperatures for each city:")
print(std_dev_temperatures)
print("\nCity with the highest temperature range:")
print(f"{city_with_highest_range}: {highest_range:.2f}")
print("\nCity with the most consistent temperature:")
print(f"{city_with_lowest_std_dev}: {lowest_std_dev:.2f}")

# Save results to a new DataFrame
results_df = pd.DataFrame({
    'Mean Temperature': mean_temperatures,
    'Standard Deviation': std_dev_temperatures,
    'Temperature Range': temperature_ranges
})

# Print results DataFrame
print("\nResults DataFrame:")
print(results_df)

# Optionally, save the results to a new CSV file
results_df.to_csv('temperature_analysis_results.csv')
