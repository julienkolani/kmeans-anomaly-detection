from turtle import title
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import adjusted_rand_score

# Load the Iris dataset
iris = load_iris()
X = iris.data  # Features
y_true = iris.target  # True labels (for comparison)

# Display the first few rows
df = pd.DataFrame(X, columns=iris.feature_names)
print(df.head())

# Apply K-means with k=3
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
y_pred = kmeans.fit_predict(X)

# Display the cluster centers
print("Cluster centers:")
print(kmeans.cluster_centers_)

# Reduce the dimensionality of the data using PCA
X_reduced = PCA().fit_transform(X)

# Import the necessary module for 3D plotting
import mpl_toolkits

# Create a 3D plot to visualize the reduced data
fig = plt.figure(1, figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

scatter = ax.scatter(
    X_reduced[:, 0],
    X_reduced[:, 1],
    X_reduced[:, 2],
    c=y_true
)

# Set labels and title for the 3D plot
ax.set(
    title='Data in 3D Dimensions',
    xlabel='1st Dimension',
    ylabel='2nd Dimension',
    zlabel='3rd Dimension',
)

# Hide tick labels for clarity
ax.xaxis.set_ticklabels([])
ax.yaxis.set_ticklabels([])
ax.zaxis.set_ticklabels([])

# Show the plot
plt.show()
