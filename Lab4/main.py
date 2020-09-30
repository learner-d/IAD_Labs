import InData, Global, Input, MyClustering

def main():
    print("Метод К-средних\n")
    #Выводим исходные данные
    print("Исходные данные:")
    print(InData.data, end='\n\n')

    #Разбивка на кластеры
    #(метод к-средних)
    #1 кластер 2 кластера ... 6 кластеров
    MyClustering.N_Clusters = Input.Integer("Количество кластеров (1-10): ", min=1, max=10)
    MyClustering.Clusterize(InData.data)
    
    #Покластерный вывод

    #Отображение графиков

if __name__ == "__main__":
    main()