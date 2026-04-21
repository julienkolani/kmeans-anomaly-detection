import random
import numpy as np

def repair(l1, l2):
    """
    Repairs the first list by replacing its False values with the corresponding values from the second list.

    :param l1: First list of values.
    :param l2: Second list of values.
    :return: A new list where False values from l1 are replaced by corresponding values from l2.
    """
    nl = []
    for i, e in enumerate(l1):
        if e:
            nl.append(e)
        else:
            nl.append(l2[i])
    return nl

def k_means_clustering(numbers, k, max_iterations=100):
    """
    Groups numbers into k clusters using the K-Means algorithm.

    :param numbers: List of numbers to group.
    :param k: Desired number of clusters.
    :param max_iterations: Maximum number of iterations.
    :return: List of clusters (each cluster is a list of numbers).
    """
    numbers.sort()  # Sort numbers for consistency
    centroids = random.sample(numbers, k)  # Initialize k random centroids
    prev_centroids = None
    clusters = [[] for _ in range(k)]  # Create empty clusters

    for _ in range(max_iterations):
        # Reset clusters
        clusters = [[] for _ in range(k)]

        # Assign each number to the closest centroid
        for num in numbers:
            tmp_centroid = [abs(num - c) for c in centroids]  # Compute distance to centroids
            closest_centroid = np.argmin(tmp_centroid)  # Find the closest centroid
            clusters[closest_centroid].append(num)  # Assign number to the closest cluster

        # Compute new centroids as the mean of each cluster
        new_centroids = [np.mean(cluster) if cluster else centroids[i] for i, cluster in enumerate(clusters)]

        # Check convergence (if centroids don’t change)
        if new_centroids == prev_centroids:
            break

        prev_centroids = new_centroids
        centroids = new_centroids

    return clusters

# Generate a list of 10 random numbers between 0 and 100
random_numbers = [random.randint(0, 100) for _ in range(10)]
k = 3  # Desired number of clusters
print("Generated numbers:", random_numbers)

# Find groups using K-Means
groups = k_means_clustering(random_numbers, k)

# Display results
for i, group in enumerate(groups):
    print(f"Group {i+1}: {group}")

import matplotlib.pyplot as plt

def plot_1d_clusters(numbers, clusters, centroids):
    """
    Plots 1D clustered points with centroids highlighted.

    :param numbers: List of original numbers.
    :param clusters: List of clusters (each cluster is a list of numbers).
    :param centroids: List of cluster centroids.
    """
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    
    plt.figure(figsize=(10, 2))
    
    for i, cluster in enumerate(clusters):
        # Plot cluster points
        plt.scatter(cluster, [i] * len(cluster), color=colors[i % len(colors)], label=f'Cluster {i+1}', s=100, edgecolors='black')
        
        # Plot centroid
        plt.scatter(centroids[i], i, color=colors[i % len(colors)], marker='X', s=200, edgecolors='black', label=f'Centroid {i+1}')

    plt.yticks([])  # Hide y-axis since it's 1D
    plt.xlabel("Values")
    plt.title("1D K-Means Clustering Visualization with Centroids")
    plt.legend()
    plt.grid(axis='x', linestyle='--', alpha=0.6)
    
    plt.show()

# Compute centroids from the clusters
centroids = [np.mean(cluster) if cluster else None for cluster in groups]

# Plot the clusters with centroids
plot_1d_clusters(random_numbers, groups, centroids)
