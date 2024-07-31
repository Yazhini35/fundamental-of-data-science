import pandas as pd
data = {
    'bedrooms': [3, 4, 2, 3, 5],
    'square_footage': [1500, 2500, 900, 1800, 3200],
    'sale_price': [300000, 500000, 200000, 350000, 650000]
}

house_data = pd.DataFrame(data)
print(house_data)
average_bedrooms = house_data['bedrooms'].mean()
print("Average number of bedrooms:", average_bedrooms)
average_square_footage = house_data['square_footage'].mean()
print("Average square footage:", average_square_footage)
average_sale_price = house_data['sale_price'].mean()
print("Average sale price:", average_sale_price)
house_max_square_footage = house_data.loc[house_data['square_footage'].idxmax()]
print("House with maximum square footage:")
print(house_max_square_footage)
house_max_sale_price = house_data.loc[house_data['sale_price'].idxmax()]
print("House with highest sale price:")
print(house_max_sale_price)
