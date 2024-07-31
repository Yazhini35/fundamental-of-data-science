import pandas as pd
from scipy import stats

# Sample data - replace this with your actual conversion rate data
data = {
    'Design': ['A'] * 100 + ['B'] * 100,
    'ConversionRate': [0.1, 0.12, 0.14, 0.13, 0.15, 0.11, 0.13, 0.14, 0.15, 0.12] * 20 +
                      [0.2, 0.22, 0.23, 0.21, 0.25, 0.24, 0.22, 0.21, 0.23, 0.25] * 20
}
df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
print("Dataset preview:")
print(df.head())

# Separate the data by design
group_A = df[df['Design'] == 'A']['ConversionRate']
group_B = df[df['Design'] == 'B']['ConversionRate']

# Perform a two-sample t-test
t_stat, p_value = stats.ttest_ind(group_A, group_B, equal_var=False)  # Welch's t-test

# Output the results
print(f"T-statistic: {t_stat:.2f}")
print(f"P-value: {p_value:.4f}")

# Interpret the results
alpha = 0.05  # significance level
if p_value < alpha:
    print("There is a statistically significant difference in the mean conversion rates between website designs A and B.")
else:
    print("There is no statistically significant difference in the mean conversion rates between website designs A and B.")
