import pandas as pd

# Sample data
data = {
    'DISEASE_NAME': ['Common Cold', 'Diabetes', 'Bronchitis', 'Influenza', 'Kidney Stones'],
    'DIAGNOSED_PATIENTS': [320, 120, 100, 150, 60]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate the frequency distribution (already provided by DIAGNOSED_PATIENTS)
# Find the most common disease
most_common_disease = df.loc[df['DIAGNOSED_PATIENTS'].idxmax()]

# Display the results
print("Frequency distribution of diseases:")
print(df)

print("\nMost common disease:")
print(f"Disease: {most_common_disease['DISEASE_NAME']}")
print(f"Number of diagnosed patients: {most_common_disease['DIAGNOSED_PATIENTS']}")
