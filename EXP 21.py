import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load the data
transaction_data = pd.read_csv('transactions.csv')

# Extract features for clustering
X = transaction_data[['TotalAmount', 'NumItemsPurchased']]

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determine the optimal number of clusters using the Elbow method
distortions = []
K = range(1, 11)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(X_scaled)
    distortions.append(kmeans.inertia_)

# Plotting the Elbow curve
plt.figure(figsize=(8, 5))
plt.plot(K, distortions, 'bo-')
plt.xlabel('Number of clusters')
plt.ylabel('Distortion')
plt.title('Elbow Method for Optimal k')
plt.show()

# Based on the Elbow curve, choose the optimal number of clusters (k)
optimal_k = 3  # Example: Choose based on the elbow plot

# Apply K-Means clustering
kmeans = KMeans(n_clusters=optimal_k, random_state=0)
clusters = kmeans.fit_predict(X_scaled)

# Add the cluster labels to the original dataframe
transaction_data['Cluster'] = clusters

# Visualize the clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(x='TotalAmount', y='NumItemsPurchased', hue='Cluster', data=transaction_data, palette='viridis', s=100, alpha=0.8)
plt.scatter(scaler.inverse_transform(kmeans.cluster_centers_)[:, 0], scaler.inverse_transform(kmeans.cluster_centers_)[:, 1], s=200, c='red', marker='X', label='Centroids')
plt.title('K-Means Clustering of Customers')
plt.xlabel('Total Amount Spent')
plt.ylabel('Number of Items Purchased')
plt.legend()
plt.show()
