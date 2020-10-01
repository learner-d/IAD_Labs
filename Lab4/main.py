import InData, Global, Input, MyClustering
import matplotlib.pyplot as plt

def main():
    print("Метод К-средних\n")
    
    #Выводим исходные данные
    print("Исходные данные:")
    print(InData.data, end='\n\n')

    #Разбивка на кластеры
    #(метод к-средних)
    Global.N_Clusters = Input.Integer("Количество кластеров (1-10): ", min=1, max=10)
    Global.Clusters = MyClustering.Clusterize(InData.data, Global.N_Clusters)
    
    #Покластерный вывод
    for i in range(Global.N_Clusters):
        print(f"Кластер {i+1}:")
        print(Global.Clusters[i], end='\n\n')

    #Отображение графиков
    for i in range(Global.N_Clusters):
        plt.plot(Global.Clusters[i][:,0], Global.Clusters[i][:,1], c=Global.Cluster_Colors[i], ls='', marker='o', label=f"Кластер {i+1}")

    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()