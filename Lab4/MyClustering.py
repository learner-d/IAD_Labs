import random
import numpy

#Разбивает на кластеры
def Clusterize(in_data, n_clusters):
    #задает случайные центроды
    def random_centers():
        rand_centers = numpy.zeros(n_clusters)
        for i in range(n_clusters):
            while True:
                rand_ind = random.randrange(0, len(in_data))
    
    #Центроиды
    centers = random_centers()
    #Кластеры