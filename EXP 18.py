import numpy as np

# Sample data: daily sales figures over the past month
# Replace this list with your actual daily sales data
daily_sales = np.array([200, 220, 210, 230, 250, 240, 260, 250, 270, 280,
                        290, 300, 310, 320, 330, 340, 350, 360, 370, 380,
                        390, 400, 410, 420, 430, 440, 450, 460, 470, 480,
                        490])

# Calculate the variance of the daily sales
variance = np.var(daily_sales)

# Display the result
print(f"Variance of daily sales: {variance:}")
