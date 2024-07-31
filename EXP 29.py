import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Create a sample dataframe simulating transaction data
data = {
    'customer_id': [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    'amount_spent': [120, 150, 80, 90, 110, 130, 170, 90, 100, 140, 140, 160, 100, 95, 130],
    'frequency_of_visits': [5, 7, 3, 4, 6, 5, 8, 4, 4, 7, 6, 8, 3, 4, 6]
}

transaction_data = pd.DataFrame(data)

# Step 2: Load and preprocess the dataset
transaction_data.dropna(inplace=True)
customer_data = transaction_data.groupby('customer_id').agg({
    'amount_spent': 'sum',
    'frequency_of_visits': 'sum'
}).reset_index()

# Step 3: Feature scaling
scaler = StandardScaler()
customer_data_scaled = scaler.fit_transform(customer_data[['amount_spent', 'frequency_of_visits']])

# Step 4: Elbow method to determine the optimal number of clusters
sse = []
for k in range(1, 6):  # Adjusted to 5 as we have only 5 unique customers in sample data
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

# Step 5: Visualize the clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(data=customer_data, x='amount_spent', y='frequency_of_visits', hue='cluster', palette='viridis')
plt.title('Customer Segments')
plt.xlabel('Total Amount Spent')
plt.ylabel('Frequency of Visits')
plt.show()

customer_data.head()
