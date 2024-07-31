import numpy as np
sales_data = np.array([1000, 1500, 2000, 2500])
total_sales = np.sum(sales_data)
print("Total sales for the year:", total_sales)
percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100
print("Percentage increase in sales from Q1 to Q4:", percentage_increase)
