import numpy
import matplotlib.pyplot as plt
import LeastSquares, Neural
from Constants import N, X, Y

def EvalY(m, x, c):
    return m*x + c

def main():
    #аналитическое описание модели
    #y = m*x + c
    print(f"X: {X}")
    print(f"Y: {Y}")

    #Метод наименьших квадратов
    m1, c1 = LeastSquares.calculate()
    E1 = numpy.absolute(Y - (X*m1 + c1)).max()
    
    print("\n" + "Метод наименьших квадратов")
    print(f"y = m*x + c")
    print(f"m = {m1}, c = {c1}")
    print(f"E = {E1}")
    
    #Машинное обучение
    m_vec, c_vec, E_vec = Neural.train()
    indx = E_vec.argmin()
    m2 = m_vec[indx]
    c2 = c_vec[indx]
    E2 = E_vec[indx]

    print("\n" + "Машинное обучение")
    print(f"y = m*x + c")
    print(f"m = {m2}, c = {c2}")
    print(f"E = {E2}")

    #Кривая отклонений апроксимации
    fig, ax = plt.subplots(1)
    ax.set_title("Ошибки в процессе обучения")
    ax.set_xlabel("Эпоха")
    ax.set_ylabel("Отклонение (E)")
    ax.plot(E_vec)

    #Поверхность отклонений апроксимации
    #fig = plt.figure()
    #ax = fig.add_subplot(111, projection='3d')
    #ax.set_title("Ошибки в процессе обучения")
    #ax.set_xlabel("Коэффициент m")
    #ax.set_ylabel("Коэффициент c")
    #ax.set_zlabel("Отклонение (E)")
    #ax.scatter(m_vec, c_vec, E_vec)
    
    #Отображение результатов обучения
    fig, axs = plt.subplots(1, 2)
    axs[0].set_title("Метод наименьших квадратов")
    axs[0].plot(X, Y, 'o')
    axs[0].plot((X.min(), X.max()), (EvalY(m1, X.min(), c1), EvalY(m1, X.max(), c1)))
    axs[1].set_title("Машинное обучение")
    axs[1].plot(X, Y, 'o')
    axs[1].plot((X.min(), X.max()), (EvalY(m2, X.min(), c2), EvalY(m2, X.max(), c2)))
    
    plt.show()

if __name__ == "__main__":
    main()