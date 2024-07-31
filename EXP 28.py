import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Create a sample dataframe
data = {
    'customer_id': [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    'amount_spent': [120, 150, 80, 90, 110, 130, 170, 90, 100, 140, 140, 160, 100, 95, 130],
    'items_purchased': [2, 3, 1, 2, 2, 1, 2, 2, 3, 2, 3, 3, 1, 2, 2]
}

transaction_data = pd.DataFrame(data)

# Save the dataframe to a CSV file
transaction_data.to_csv('transaction_data.csv', index=False)

# Load the dataset
data = pd.read_csv('transaction_data.csv')

# Preprocess the data
data.dropna(inplace=True)
customer_data = data.groupby('customer_id').agg({
    'amount_spent': 'sum',
    'items_purchased': 'sum'
}).reset_index()

# Feature scaling
scaler = StandardScaler()
customer_data_scaled = scaler.fit_transform(customer_data[['amount_spent', 'items_purchased']])

# Elbow method to determine the optimal number of clusters
sse = []
for k in range(1, 6):  # Adjusted to 5 as we have only 5 customers
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(customer_data_scaled)
    sse.append(kmeans.inertia_)

# Plot the elbow curve
plt.plot(range(1, 6), sse, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('SSE')
plt.title('Elbow Method')
plt.show()

# Apply K-Means with the chosen number of clusters (assume 3 for this example)
kmeans = KMeans(n_clusters=3, random_state=42)
customer_data['cluster'] = kmeans.fit_predict(customer_data_scaled)

# Visualize the clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(data=customer_data, x='amount_spent', y='items_purchased', hue='cluster', palette='viridis')
plt.title('Customer Segments')
plt.xlabel('Total Amount Spent')
plt.ylabel('Total Items Purchased')
plt.show()

customer_data.head()
