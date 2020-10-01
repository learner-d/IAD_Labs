import random
import numpy
import math

#Расстояние
def distance(o1, o2):
    return math.sqrt((o2[0]-o1[0])**2 + (o2[1]-o1[1])**2)

class Cluster:
    def __init__(self, size, id, init_center):
        self.size = size
        self.objects = numpy.zeros(shape=(size, 2))
        self.n_objects = 0
        self.id = id
        self.center = init_center
    #Добавляет объект в кластер
    def add_object(self, obj):
        self.objects[self.n_objects] = obj
        self.n_objects = self.n_objects + 1
    #Сообщает, заполнен ли кластер
    def is_filled_up(self):
        return self.n_objects == self.size
    #Перерасчитывает центроид кластера
    def recenter(self):
        self.center = numpy.array((self.objects[:,0].mean(), self.objects[:,1].mean()))
    #Очищает кластер от объектов
    def clear(self):
        self.n_objects = 0
        self.objects  = numpy.zeros(shape=(self.size, 2))

class ClusterPool:
    def __init__(self, n_clusters, cluster_size, centers):
        self.n_clusters = n_clusters
        #Кластеры
        self.clusters = []
        #Кластеры, не заполненные полностью
        self.avail_clusters = []
        
        #Заполняем коллекции кластеров
        for i in range(n_clusters):
            cluster = Cluster(cluster_size, i, centers[i])
            self.clusters.append(cluster)
            self.avail_clusters.append(cluster)
        
    #Находит ближайший кластер к заданному объекту
    def nearest_cluster(self, obj):
        i_near = 0
        min_dist = math.inf
        for i in range(len(self.avail_clusters)):
            dist = distance(self.avail_clusters[i].center, obj)
            if dist < min_dist:
                i_near = i
                min_dist = dist
        return self.avail_clusters[i_near]
        
    #Распределяет объекты по кластерам
    def assign(self, objects):
        for i in range(len(objects)):
            cluster = self.nearest_cluster(objects[i])
            cluster.add_object(objects[i])
            if cluster.is_filled_up():
                self.avail_clusters.remove(cluster)

    #Очищает кластеры от объектов
    def clear(self):
        for i in range(self.n_clusters):
            self.clusters[i].clear()
        self.avail_clusters = self.clusters.copy()

    #Возвращает коллекцию центроидов
    def get_centers(self):
        centers = numpy.zeros(shape=(self.n_clusters,2))
        for i in range(self.n_clusters):
            self.clusters[i].recenter()
            centers[i] = self.clusters[i].center
        return centers

    #Возвращает разбитые на кластеры данные
    def get_clustered_data(self):
        clustered_data = [0] * self.n_clusters
        for i in range(self.n_clusters):
            n_objects = self.clusters[i].n_objects
            clustered_data[i] = numpy.zeros(shape=(n_objects,2))
            for j in range(n_objects):
                clustered_data[i][j] = self.clusters[i].objects[j]
        return clustered_data

#Разбивает на кластеры
def Clusterize(in_data, n_clusters):
    #Задает случайные центроды
    def random_centers():
        rand_centers = numpy.zeros(shape=(n_clusters,2))
        for i in range(n_clusters):
            while True:
                rand_ind = random.randrange(0, len(in_data))
                if in_data[rand_ind] not in rand_centers:
                    rand_centers[i] = in_data[rand_ind]
                    break
        return rand_centers

    #Определяет сдвиг центроидов
    def diff(centers1, centers2):
        max_shft = 0
        for i in range(len(centers1)):
            shift = distance(centers1[i], centers2[i])
            if shift > max_shft:
                max_shft = shift
        return max_shft
    
    #Центроиды
    centers = random_centers()
    #Размер кластера
    cluster_size = math.ceil(len(in_data) / n_clusters)
    
    #Создаем пул кластеров
    Cl_Pool = ClusterPool(n_clusters, cluster_size, centers)
    
    iters = 0
    max_iters = 300
    for i in range(max_iters):
        #Распределяем объекты по кластерам
        Cl_Pool.assign(in_data)
        #Перерасчитываем центроиды
        new_centers = Cl_Pool.get_centers()

        #Проверяем смещение центроидов
        if diff(centers, new_centers) < 0.00001:
            break

        iters = iters + 1
        if iters == max_iters:
            break

        #Удаляем объекты с кластеров
        Cl_Pool.clear()
        #Меняем центроиды
        centers = new_centers

    #Возвращаем разбитые на кластеры данные
    return Cl_Pool.get_clustered_data()
    