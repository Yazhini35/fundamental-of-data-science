import pandas as pd
import numpy as np
from scipy import stats

# Sample data
data =  {
    'product_title': ['Pineapple slicer', 'Levis Jeans Pant', 'Wallet', 'Salwar'],
    'product_category': ['Apparel', 'Apparel', 'Apparel', 'Apparel'],
    'star_rating': [4, 5, 5, 5],
    'review_headline': ['Really good', 'Perfect Dress', 'Love it', 'Awesome'],
    'review_date': ['2013-01-14', '2014-04-22', '2015-07-28', '2015-06-12']
}

# Create DataFrame
df = pd.DataFrame(data)

# Filter by product category
category = 'Apparel'
df_category = df[df['product_category'] == category]

# Calculate mean rating
mean_rating = df_category['star_rating'].mean()

# Calculate standard deviation and sample size
std_dev = df_category['star_rating'].std()
n = len(df_category)

# Calculate confidence interval
confidence_level = 0.95
degrees_freedom = n - 1
confidence_interval = stats.t.interval(
    confidence_level,
    degrees_freedom,
    mean_rating,
    std_dev / np.sqrt(n)
)

# Display results
print(f"Mean rating for '{category}': {mean_rating:.2f}")
print(f"95% confidence interval for the mean rating: ({confidence_interval[0]:.2f}, {confidence_interval[1]:.2f})")
