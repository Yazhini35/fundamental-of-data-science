import numpy as np
sales_data = np.array([
    [10, 15.5, 155.0],
    [20, 10.0, 200.0],
    [15, 20.0, 300.0]
])
average_price_per_unit = np.mean(sales_data[:, 1])
print("Average price of all products sold:", average_price_per_unit)
