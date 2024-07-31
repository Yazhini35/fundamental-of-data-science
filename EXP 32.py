import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import LabelEncoder
import pickle

# Function to evaluate the model
def evaluate_model(df, features, target, model):
    X = df[features]
    y = df[target]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Predict using the model
    y_pred = model.predict(X_test)

    # Calculate evaluation metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')

    # Display metrics
    print(f"Accuracy: {accuracy:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1-Score: {f1:.2f}")

# Load the dataset
df = pd.read_csv('path_to_your_dataset.csv')  # Replace with your dataset path

# Display the first few rows of the DataFrame
print("Dataset preview:")
print(df.head())

# Load the trained model from a file
with open('path_to_your_model.pkl', 'rb') as file:  # Replace with your model path
    model = pickle.load(file)

# Get user input for feature names and target variable
features = input("Enter the feature names (comma-separated): ").strip().split(',')
target = input("Enter the target variable name: ").strip()

# Strip any extra spaces from feature names
features = [feature.strip() for feature in features]

# Encode the target variable if it's categorical
if df[target].dtype == 'object':
    le = LabelEncoder()
    df[target] = le.fit_transform(df[target])

# Evaluate the model
evaluate_model(df, features, target, model)
