import numpy
from sklearn.cluster import KMeans

#Разбивает на кластеры алгоритмом scikit-learn
def Clusterize(in_data, n_clusters):
    #Список кластеров
    clusters = [0] * n_clusters
    
    for i in range(n_clusters):
        clusters[i] = []
    
    #Кластеризатор
    clusterer = KMeans(n_clusters)
    clusterer.fit(in_data)

    #Массив с индексами кластеров
    cluster_indexed_data = clusterer.predict(in_data)

    #Формируем список кластеров    
    for i in range(len(in_data)):
        cluster_ind = cluster_indexed_data[i]
        clusters[cluster_ind].append(in_data[i])

    for i in range(len(clusters)):
        clusters[i] = numpy.array(clusters[i])

    #Центроиды
    centers = clusterer.cluster_centers_

    return clusters, centers

