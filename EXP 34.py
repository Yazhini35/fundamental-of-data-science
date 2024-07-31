import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import numpy as np

# Sample data - replace this with your actual dataset
data = {
    'AnnualSpending': [15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000],
    'FrequencyOfPurchases': [10, 12, 14, 16, 18, 20, 22, 24, 26, 28],
    'AverageCartValue': [100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
}
df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
print("Dataset preview:")
print(df.head())

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# Determine the optimal number of clusters (if not known)
# Here we'll use a predefined number of clusters (e.g., 3)
optimal_clusters = 3

# Train the K-Means model
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
kmeans.fit(X_scaled)

# Assign clusters to the original data
df['Cluster'] = kmeans.labels_

# Predict the cluster for a new customer
def predict_cluster(features):
    features_scaled = scaler.transform([features])
    cluster = kmeans.predict(features_scaled)
    return cluster[0]

# User input for a new customer
print("Enter the annual spending, frequency of purchases, and average cart value of the new customer:")

annual_spending = float(input("Annual Spending ($): "))
frequency_of_purchases = float(input("Frequency of Purchases (per year): "))
average_cart_value = float(input("Average Cart Value ($): "))

new_customer_features = [annual_spending, frequency_of_purchases, average_cart_value]
predicted_cluster = predict_cluster(new_customer_features)

print(f"The new customer is assigned to Cluster {predicted_cluster}.")
