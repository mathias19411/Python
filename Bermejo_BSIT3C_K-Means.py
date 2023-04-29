#K-means Clustering
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Generating the two random lists of 300 integers between 1 and 100,000
np.random.seed(42) #sets the random seed for NumPy's random number generator to the value 42
randomIntegers1 = np.random.randint(1, 100001, size=300)
randomIntegers2 = np.random.randint(1, 100001, size=300)

#Generating the First Scatter Plot
plt.scatter(randomIntegers1,randomIntegers2)
plt.title('Scatter Plot of the integers')
plt.xlabel('Random Integer 1')
plt.ylabel('Random Integer 2') 
plt.show()

# Create the feature matrix by stacking the two lists horizontally
X = np.column_stack((randomIntegers1, randomIntegers2))

# Perform k-means clustering with 5 random centroids
kmeans = KMeans(n_clusters=5, init='random', max_iter=2, tol=0, n_init=1).fit(X)

# Initial Plot of the data points and centroids
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='X', s=300, c='red')
plt.title('Initial K-means with 5 Clusters')
plt.xlabel('Random Integer 1')
plt.ylabel('Random Integer 2')
# plt.legend()
plt.show()

# Perform k-means clustering with 5 random centroids
kmeans = KMeans(n_clusters=5, init='random', max_iter=40, tol=0, n_init=1).fit(X)

# Final Plot of the data points and centroids
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='X', s=300, c='red')
plt.title('Final K-means with 5 Clusters')
plt.xlabel('Random Integer 1')
plt.ylabel('Random Integer 2')
# plt.legend()
plt.show()