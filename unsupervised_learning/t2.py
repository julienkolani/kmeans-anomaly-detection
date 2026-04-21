"""import numpy as np

def repair(l1, l2):
    nl = []
    for i, e in enumerate(l1):
        if e:
            nl.append(e)
        else:
            nl.append(l2[i])
    return nl

def repair2(l1, l2):
    return [cluster if cluster 
                else l2[i] for i, cluster in enumerate(l1)]



l1 = [[3], [48], [273, 34], []]
l2 = [2, 3, 9, 13]

nl = repair(l1, l2)


print("repair", repair(l1, l2))

result = [np.mean(e) for e in nl]

print("result", result)

"""

import random
import numpy as np

def repair(l1, l2):
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
    clusters = [[] for _ in range(k)]

    for _ in range(max_iterations):
        # Reset clusters
        clusters = [[] for _ in range(k)]

        # Assign each number to the closest centroid
        for num in numbers:
            tmp_centroid = [abs(num - c) for c in centroids]
            closest_centroid = np.argmin(tmp_centroid)
            clusters[closest_centroid].append(num)

        # Compute new centroids as the mean of each cluster


        new_centroids = [np.mean(cluster) if cluster \
                          else centroids[i] for i, cluster in enumerate(clusters)]




        # Check convergence (if centroids don’t change)
        if new_centroids == prev_centroids:
            break

        prev_centroids = new_centroids
        centroids = new_centroids

    return clusters, numbers

# Generate a list of 10 random numbers between 0 and 100
random_numbers = [random.randint(0, 100) for _ in range(10)]
k = 3  # Desired number of clusters
print("Nombres générés :", random_numbers)

# Find groups using K-Means
groups, numbers = k_means_clustering(random_numbers, k)

# Display results
for i, group in enumerate(groups):
    print(f"Groupe {i+1} : {group}")

# Compute centroids from the clusters
centroids = [np.mean(cluster) if cluster else None for cluster in groups]


# Implémentation avec sklearn
from sklearn.cluster import KMeans

X = np.array(numbers).reshape(-1, 1)
kmeans = KMeans(n_clusters=k, random_state=0, n_init="auto").fit(X)
print("Labels :", kmeans.labels_)
print("Centroïdes :", kmeans.cluster_centers_)