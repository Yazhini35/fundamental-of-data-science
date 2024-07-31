import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

# Sample data - replace this with your actual dataset
data = {
    'Area': [1500, 2000, 2500, 1800, 2200],
    'Bedrooms': [3, 4, 4, 3, 4],
    'Location': ['Suburb', 'City', 'City', 'Suburb', 'Suburb'],
    'Price': [400000, 500000, 600000, 450000, 550000]
}
df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
print("Dataset preview:")
print(df.head())

# Convert categorical features to dummy variables
df = pd.get_dummies(df, columns=['Location'], drop_first=True)

# Select features and target
X = df.drop('Price', axis=1)
y = df['Price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Evaluate the model
y_pred = model.predict(X_test_scaled)
mse = mean_squared_error(y_test, y_pred)
print(f"Model Mean Squared Error: {mse:.2f}")

# Predict the price of a new house
def predict_price(features):
    features_scaled = scaler.transform([features])
    prediction = model.predict(features_scaled)
    return prediction[0]

# User input for a new house
print("Enter the area, number of bedrooms, and location of the new house:")

area = float(input("Area (sq ft): "))
bedrooms = int(input("Number of Bedrooms: "))
location = input("Location (Suburb/City): ")

# Convert location to dummy variables
location_dummies = [1 if location == 'City' else 0]

new_house_features = [area, bedrooms] + location_dummies
predicted_price = predict_price(new_house_features)
print(f"Predicted Price: ${predicted_price:.2f}")
