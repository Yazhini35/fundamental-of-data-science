import pandas as pd

# Sample data
data = {
    'WEATHER_CONDITION': ['Sunny', 'Rainy', 'Cloudy', 'Snowy', 'Windy'],
    'OCCURRENCES': [120, 80, 60, 30, 50]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate the frequency distribution (already provided by OCCURRENCES)
# Find the most common weather condition
most_common_weather = df.loc[df['OCCURRENCES'].idxmax()]

# Display the results
print("Frequency distribution of weather conditions:")
print(df)

print("\nMost common weather type:")
print(f"Weather Condition: {most_common_weather['WEATHER_CONDITION']}")
print(f"Number of occurrences: {most_common_weather['OCCURRENCES']}")
