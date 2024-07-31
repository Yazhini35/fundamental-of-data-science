import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Sample data - replace this with your actual dataset
data = {
    'Symptom1': [1, 0, 1, 1, 0, 1, 0, 1, 1, 0],
    'Symptom2': [0, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    'Symptom3': [1, 1, 0, 1, 0, 0, 1, 1, 0, 1],
    'Condition': [1, 0, 1, 1, 0, 1, 0, 1, 1, 0]
}
df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
print("Dataset preview:")
print(df.head())

# Select features and target
X = df[['Symptom1', 'Symptom2', 'Symptom3']]
y = df['Condition']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the KNN classifier
k = int(input("Enter the value of k (number of neighbors): "))
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X_train_scaled, y_train)

# Evaluate the model
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Predict for new patient
def predict_condition(features, k):
    features_scaled = scaler.transform([features])
    prediction = model.predict(features_scaled)
    return prediction[0]

# User input for new patient
symptom1 = int(input("Enter Symptom1 (0 or 1): "))
symptom2 = int(input("Enter Symptom2 (0 or 1): "))
symptom3 = int(input("Enter Symptom3 (0 or 1): "))

new_patient_features = [symptom1, symptom2, symptom3]
condition = predict_condition(new_patient_features, k)
print(f"Predicted Condition for the new patient: {'Condition' if condition == 1 else 'No Condition'}")
