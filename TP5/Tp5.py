# EXO1

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import metrics

Y = np.array([[1], [2], [4], [7], [8], [10], [15], [17], [21]])
labelList = [[1], [2], [4], [7], [8], [10], [15], [17], [21]]

# Grace a linkage(le set , type de linkage) on definit le type de linkage
# The complete linkage is the oposite of single linkage

# --------------------- SINGLE LINKAGE -------------------- #

linked = linkage(Y, 'single')
cluster = AgglomerativeClustering(linkage='single')
plt.figure(figsize=(10, 7))
dendrogram(linked, orientation='top', labels=labelList,
           distance_sort='descending', show_leaf_counts=True)
plt.title('average')

#----------------------- AVERAGE LINKAGE -------------------- #

linked = linkage(Y, 'average')
plt.figure(figsize=(10, 7))
dendrogram(linked,
           orientation='top',
           labels=labelList,
           distance_sort='descending',
           show_leaf_counts=True)
plt.title('average')

#----------------------- COMPLETE LINKAGE -------------------- #

linked = linkage(Y, 'complete')
plt.figure(figsize=(10, 5))
dendrogram(linked,
           orientation='top',
           labels=labelList,
           distance_sort='descending',
           show_leaf_counts=True)
plt.title('complete')

#----------------------- WARD LINKAGE -------------------- #

linked = linkage(Y, 'ward')
plt.figure(figsize=(10, 5))
dendrogram(linked,
           orientation='top',
           labels=labelList,
           distance_sort='descending',
           show_leaf_counts=True)
plt.title('ward')
plt.show()


# --------------------- SINGLE LINKAGE -------------------- #
""" 
Single linkage : at the beggining we have as many clusters as the number of points,
the clustering occurs after calculating the distances between the nearest points in each cluster, we group the two clusters
that have the minimum distance, we repeat this processing utill having a complete heirarchy
this methode is the fastest for our data set it repeat the clustering only 5 times
"""
#----------------------- AVERAGE LINKAGE -------------------- #
"""
We calculate the average distance between the points of the clusters and cluster the two clusters that
have the minimum average distance, it will repeat the processing till having all the points in one cluster
this algorythm is less faster than the single method 
"""
#----------------------- COMPLETE LINKAGE -------------------- #
"""we compare the two farthest points in each set and cluster the two groups that have the minimum distance"""

#----------------------- WARD LINKAGE -------------------- #
""" this methode consists of comparing the variance between the datapoints of each group and clustering the
two groups that have the minimum variance """


# EXO 2

Y = np.array([[1], [2], [4], [7], [8], [10], [15], [17], [21]])
# we build the agglomerative clustering heirarchy using the single methode
linked = linkage(Y, 'single')
labelList = [[1], [2], [4], [7], [8], [10], [15], [17], [21]]
plt.figure(figsize=(10, 7))
dendrogram(linked,
           orientation='top',
           labels=labelList,
           distance_sort='descending',
           show_leaf_counts=True)
plt.show()


""" showing the difference between k-means and the agglomerative algorithms """


""" the k-means methode will take the minimum distance between each point and each mean         
    created and group on it until forming the final three clusters
"""


""" the agglomerative method will group each time a point to the nearest cluster and build each # time a sub tree untill having the complet tree"""


""" We can see that the k-means algorithme is more efficient than the agglomerative with the        # single method because, in the k-means algo, we compare all the points in each iteration to
the groups that we have instead, in the agglomerative with single method, we compare
calculate and take only one distance,here the nearest."""


# EXO3

iris = datasets.load_iris()
print(iris)
print(iris.data)
print(iris.feature_names)
print(iris.target)
print(iris.target_names)

# Here we create two dataframes one for the data and the feauteres measured another one for the species names

x = pd.DataFrame(iris.data)
x.columns = ['Sepal_Length', 'Sepal_width', 'Petal_Length', 'Petal_width']
y = pd.DataFrame(iris.target)
y.columns = ['Targets']

# We apply the k-means algorythm for the data willing to obtain three clusters
model = KMeans(n_clusters=3)

model.fit(x)
colormap = np.array(['r', 'g', 'b'])
plt.scatter(x.Petal_Length, x.Petal_width, c=colormap[y.Targets], s=40)

model1 = AgglomerativeClustering(n_clusters=3, linkage='single')
model1.fit(x)

model2 = AgglomerativeClustering(n_clusters=3, linkage='ward')
model2.fit(x)

model3 = AgglomerativeClustering(n_clusters=3, linkage='average')
model3.fit(x)

model4 = AgglomerativeClustering(n_clusters=3, linkage='complete')
model4.fit(x)

print("single", metrics.adjusted_rand_score(model1.labels_, y.Targets))

print("ward", metrics.adjusted_rand_score(model2.labels_, y.Targets))

print("average", metrics.adjusted_rand_score(model3.labels_, y.Targets))

print("coplete", metrics.adjusted_rand_score(model4.labels_, y.Targets))


""" 
The random index a function that evaluates similarity between two clusternigs
the general form is (a+b)/(a+b+c+d) where:
  -a = the number of pairs whose elements are in the same group in both clusters
  -b = the number pf pairs whose elements are in the same group in the first cluster and in
       different groups in the second cluster
  -c = the number pf pairs whose elements are in different groups in the first cluster and in
       in the same group in the second cluster
  -d = the number pf pairs whose elements are in different groups in the first cluster and in
       different groups in the second cluster

the ARI is calculating the similarity between two datasets it randomly takes pairs of indexes
and compare their similarity in the two data sets in question
The ARI is an indicator of similarity between two data sets, in fact it tells as how match
the data is similar in the two clusters in question


the ARI is more efficiant methode of calculating similarity, by taking the groups randomly
its formula is follows:
ARI =  (Index-Expected Index) / (MaxIndex-Expect) which can be semplified to :
      2(ad - bc)/ (b² + c² + 2ad + (a + d)(b + c)

1- The agglomerative clustering with "single linkage" methode is the less efficient, it shows that
the similarity between the clusters before and after using the clustering is 0.56... because of the
way of clustering in this methode

2- the "average linkage" is the most efficient method of linkage, it correspond with 0.75.. to
the original data because it takes the average of distances in each iteration instead of taking only
one distance

3- the "complete linkage" is less efficient than the average methode in this set of data its
its result is 0.64...

4- the efficient of k-means algorithm is near to the single method its similarity is 0.73
"""
