import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

# Step 1: Create a sample dataframe
data = {
    'age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    'gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F'],
    'blood_pressure': [120, 130, 125, 140, 135, 145, 150, 155, 160, 165],
    'cholesterol': [200, 220, 210, 230, 240, 250, 260, 270, 280, 290],
    'outcome': ['Good', 'Bad', 'Good', 'Bad', 'Good', 'Bad', 'Good', 'Bad', 'Good', 'Bad']
}

patient_data = pd.DataFrame(data)
patient_data.to_csv('patient_data.csv', index=False)

# Step 2: Load and preprocess the dataset
data = pd.read_csv('patient_data.csv')

# Encode categorical variables
label_encoder = LabelEncoder()
data['gender'] = label_encoder.fit_transform(data['gender'])
data['outcome'] = label_encoder.fit_transform(data['outcome'])

# Split the dataset into features and target variable
X = data.drop('outcome', axis=1)
y = data['outcome']

# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Step 3: Build and train the KNN model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Step 4: Evaluate the model
y_pred = knn.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Display the results
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 Score: {f1:.2f}")
print("Classification Report:")
print(report)
