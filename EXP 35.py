import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

# Sample data - replace this with your actual dataset
data = {
    'UsageMinutes': [200, 150, 300, 400, 250, 350, 150, 500, 600, 250],
    'ContractDuration': [12, 24, 6, 12, 24, 12, 6, 36, 36, 12],
    'Churn': [0, 0, 1, 1, 0, 1, 0, 1, 1, 0]
}
df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
print("Dataset preview:")
print(df.head())

# Select features and target
X = df[['UsageMinutes', 'ContractDuration']]
y = df['Churn']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the Logistic Regression model
model = LogisticRegression(random_state=42)
model.fit(X_train_scaled, y_train)

# Evaluate the model
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")
print("Confusion Matrix:")
print(conf_matrix)

# Predict churn status of a new customer
def predict_churn(features):
    features_scaled = scaler.transform([features])
    prediction = model.predict(features_scaled)
    return "Churn" if prediction[0] == 1 else "No Churn"

# User input for a new customer
print("Enter the usage minutes and contract duration of the new customer:")

usage_minutes = float(input("Usage Minutes: "))
contract_duration = float(input("Contract Duration (months): "))

new_customer_features = [usage_minutes, contract_duration]
predicted_churn = predict_churn(new_customer_features)
print(f"Predicted Churn Status: {predicted_churn}")
