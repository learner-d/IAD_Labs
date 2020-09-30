import InData, Global, Input, MyClustering
import matplotlib.pyplot as plt

def main():
    print("Метод К-средних\n")
    #Выводим исходные данные
    print("Исходные данные:")
    print(InData.data, end='\n\n')

    #Разбивка на кластеры
    #(метод к-средних)
    #1 кластер 2 кластера ... 6 кластеров
    Global.N_Clusters = 7
    #Global.N_Clusters = Input.Integer("Количество кластеров (1-10): ", min=1, max=10)
    MyClustering.Clusterize(InData.data, Global.N_Clusters)
    
    #Покластерный вывод

    #Отображение графиков
    plt.plot(InData.data[:,0], ".k")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()