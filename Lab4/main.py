import InData, Global, Input
import MyClustering, Clustering
import matplotlib.pyplot as plt

def main():
    print("Метод К-средних\n")
    
    #Выводим исходные данные
    print("Исходные данные:")
    print(InData.data, end='\n\n')

    Global.N_Clusters = Input.Integer("Количество кластеров (1-8): ", min=1, max=8)
    
    #Кластеризация нашим алгоритмом
    Clusters1, Centroids1 = MyClustering.Clusterize(InData.data, Global.N_Clusters)
    #Кластеризация алгоритмом с библиотеки sklearn
    Clusters2, Centroids2 = Clustering.Clusterize(InData.data, Global.N_Clusters)
    
    #Покластерный вывод
    print("\n"+"Кластеризация нашим алгоритмом:")
    for i in range(Global.N_Clusters):
        print(f"Кластер {i+1}:")
        print(Clusters1[i])
    print(f"Центроиды: {Centroids1}")

    print("\n"+"Кластеризация алгоритмом scikit-learn:")
    for i in range(Global.N_Clusters):
        print(f"Кластер {i+1}:")
        print(Clusters2[i])
    print(f"Центроиды: {Centroids2}")

    #Отображение кластеров
    fig1, ax1 = plt.subplots(1)
    fig2, ax2 = plt.subplots(1)
    for i in range(Global.N_Clusters):
        #Отображение объектов кластера
        ax1.plot(Clusters1[i][:,0], Clusters1[i][:,1], 'o', c=Global.Cluster_Colors[i], label=f"Кластер {i+1}")
        ax2.plot(Clusters2[i][:,0], Clusters2[i][:,1], 'o', c=Global.Cluster_Colors[i], label=f"Кластер {i+1}")

    #Отображение центроидов
    ax1.plot(Centroids1[:,0], Centroids1[:,1], 'r+', label='Центроид')
    ax2.plot(Centroids2[:,0], Centroids2[:,1], 'r+', label='Центроид')

    ax1.legend()
    ax1.grid(True)
    ax1.set_title("Кластеризация: наш алгоритм")

    ax2.legend()
    ax2.grid(True)
    ax2.set_title("Кластеризация: алгоритм scikit-learn")
    
    plt.show()

if __name__ == "__main__":
    main()