import InData, Global, Input, Clustering

def main():
    print("Метод К-средних\n")
    #Выводим исходные данные
    print("Исходные данные:")
    print(InData.data, end='\n\n')

    #Разбивка на кластеры
    #(метод к-средних)
    #1 кластер 2 кластера ... 6 кластеров
    Clustering.N_Clusters = Input.Integer("Количество кластеров (1-10): ", min=1, max=10)
    
    #Покластерный вывод

    #Отображение графиков

if __name__ == "__main__":
    main()