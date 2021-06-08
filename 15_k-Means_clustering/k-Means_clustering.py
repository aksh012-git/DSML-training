# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 08:49:52 2021

@author: Aksh
"""


"""
unsupervised learning algorithms-->

--Search on google 
K-means clustering. --> https://www.youtube.com/watch?v=CLKW6uWJtTc
KNN (k-nearest neighbors)
Hierarchal clustering.
Anomaly detection.
Neural Networks.
Principle Component Analysis.
Independent Component Analysis.
Apriori algorithm.

search points--->
WCSS(Whitin cluster sum of square)
elbow method - https://www.youtube.com/watch?v=FqIGui0rwh4&t=108s

use of elbow method is find a best k value.
k value means how many cluster i tack and make best output

"""

#----------------------------------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#----------------------------------------------------------------------------------------------------------
dataset = pd.read_csv('Mall_Customers.csv')
#see data set all are input column

#----------------------------------------------------------------------------------------------------------
#we put only last two column as input
x = dataset.iloc[:, [3,4]].values

#----------------------------------------------------------------------------------------------------------
#Using elbow mwthod find how many cluster are use, find optimal number of cluster
from sklearn.cluster import KMeans
wcss = []

#in range i put 1 to 10 cluster 
for i in range (1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

"""
n_clusters --> The number of clusters to form as well as the number of centroids to generate.
init --> 'k-means++' : selects initial cluster centers for k-mean clustering in a smart way to speed up convergence. 
max_iter --> Maximum number of iterations of the k-means algorithm for a single run. 
 n_init -->  Number of time the k-means algorithm will be run with different centroid seeds.adjuting centroid points
 inertia_ --> search on google
"""

#----------------------------------------------------------------------------------------------------------
#see graph and check which cluster provide you optimal solution
plt.plot(range(1,11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('wcss')
plt.savefig("optimalSolution.png")


#see graph, after 5 cluster graph are linearlly so use 5 for optimal solution

#----------------------------------------------------------------------------------------------------------
# Applying k-means to the mall dataset
kmeans = KMeans(n_clusters = 5, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)


#----------------------------------------------------------------------------------------------------------
y_kmeans = kmeans.fit_predict(x)

#see y_kmeans , our all data devide into 5 cluster 0 to 4


#----------------------------------------------------------------------------------------------------------
#centroid points of our 5 clusters
print(kmeans.cluster_centers_[:, :])


#----------------------------------------------------------------------------------------------------------
# Visualising the clusters
#see our all cluste
#plt.scatter(x[conditions, column], x[conditions, column], size of point, c = 'red', label = 'Cluster - 1')
plt.scatter(x[y_kmeans==0, 0], x[y_kmeans==0, 1], s = 100, c = 'red', label = 'Cluster - 1')
plt.scatter(x[y_kmeans==1, 0], x[y_kmeans==1, 1], s = 100, c = 'blue', label = 'Cluster - 2')
plt.scatter(x[y_kmeans==2, 0], x[y_kmeans==2, 1], s = 100, c = 'green', label = 'Cluster - 3')
plt.scatter(x[y_kmeans==3, 0], x[y_kmeans==3, 1], s = 100, c = 'cyan', label = 'Cluster - 4')
plt.scatter(x[y_kmeans==4, 0], x[y_kmeans==4, 1], s = 100, c = 'magenta', label = 'Cluster - 5')
#for centroid points 
#plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c='yellow', label = 'Centroids')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c='yellow', label = 'Centroids')
plt.title('Clusters of Clients')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.savefig("allCluster.png")

#----------------------------------------------------------------------------------------------------------












