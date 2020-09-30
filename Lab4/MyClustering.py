import random
import numpy
import math

class Cluster():
    def __init__(self, size, id):
        self.size = size
        self.objects = numpy.zeros(shape(size, 2))
        self.n_objects = 0
        self.id = id
    #Добавляет объект в кластер
    def add_object(self, obj):
        self.objects[n_objects] = obj
        self.n_objects = self.n_objects + 1
    #Сообщает, заполнен ли кластер
    def is_filled_up(self):
        return self.n_objects == self.size
    #Сообщает центроид кластера
    def center(self):
        return (self.objects[:,0].mean(), self.objects[:,1].mean())

#Разбивает на кластеры
def Clusterize(in_data, n_clusters):
    #Расстояние
    def distance(o1, o2):
        return math.sqrt((o2[0]-o1[0])**2 + (o2[1]-o1[1])**2)

    #задает случайные центроды
    def random_centers():
        rand_centers = numpy.zeros(n_clusters)
        for i in range(n_clusters):
            while True:
                rand_ind = random.randrange(0, len(in_data))
                if in_data[rand_ind] not in rand_centers:
                    rand_centers[i] = in_data[rand_ind]
                    break
    
    #Центроиды
    centers = random_centers()
    #Всего объектов
    n_objects = len(in_data)
    #Размер кластера
    cluster_size = math.floor(n_objects / n_clusters)
    #Кластеры
    #clusters = numpy.zeros(shape=(n_clusters,cluster_size,2))

    while True:
        pass