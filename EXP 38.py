import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, export_text
from sklearn.metrics import mean_squared_error, r2_score

# Sample data - you can replace this with your actual DataFrame
data = {
    'Mileage': [5000, 15000, 30000, 50000, 70000],
    'Age': [1, 2, 3, 5, 7],
    'Brand': ['Toyota', 'Ford', 'BMW', 'Ford', 'Toyota'],
    'EngineType': ['Hybrid', 'Petrol', 'Diesel', 'Petrol', 'Hybrid'],
    'Price': [20000, 18000, 25000, 15000, 12000]
}
df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
print(df.head())

# Select the features and target
features = ['Mileage', 'Age', 'Brand', 'EngineType']
target = 'Price'
X = df[features]
y = df[target]

# Convert categorical features to dummy variables
X = pd.get_dummies(X, drop_first=True)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the decision tree regressor
model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model's performance
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

# Function to predict price and display decision path for a new car
def predict_price(model, input_features):
    # Convert input features to DataFrame and create dummy variables
    input_df = pd.DataFrame([input_features])
    input_df = pd.get_dummies(input_df, drop_first=True)
    # Ensure input features match the model's training features
    input_df = input_df.reindex(columns=X.columns, fill_value=0)
    
    # Predict the price
    predicted_price = model.predict(input_df)[0]
    
    # Display the decision path
    decision_path = model.decision_path(input_df)
    feature_names = X.columns
    tree_rules = export_text(model, feature_names=list(feature_names))
    print("Decision Path:\n", tree_rules)
    
    return predicted_price

# Input features of a new car
new_car = {
    'Mileage': 30000,
    'Age': 3,
    'Brand': 'Toyota',
    'EngineType': 'Hybrid'
}

# Predict the price of the new car and display the decision path
predicted_price = predict_price(model, new_car)
print(f'Predicted Price: ${predicted_price:.2f}')
