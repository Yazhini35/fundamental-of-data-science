import pandas as pd

# Sample data: DataFrame containing post interaction data with number of likes
data = {
    'post_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'likes': [120, 150, 150, 200, 220, 180, 150, 240, 120, 200]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate the frequency distribution of likes
likes_frequency = df['likes'].value_counts().sort_index()

# Display the frequency distribution
print("Frequency distribution of likes:")
print(likes_frequency)
