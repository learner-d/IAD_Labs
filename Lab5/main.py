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
    print(f"X: {X}")
    Y1 = numpy.array([EvalY(m1, x, c1) for x in X])
    print(f"Y: {Y1}")
    
    #Нейронная сеть
    print("\n" + "Нейронная сеть")
    E_min = float(input("Пороговая погрешность (E_min): "))
    m_vec, c_vec, E_vec = Neural.train(E_min)
    indx = E_vec.argmin()
    m2 = m_vec[indx]
    c2 = c_vec[indx]
    E2 = E_vec[indx]

    print(f"y = m*x + c")
    print(f"m = {m2}, c = {c2}")
    print(f"E = {E2}")
    print(f"X: {X}")
    Y2 = numpy.array([EvalY(m2, x, c2) for x in X])
    print(f"Y: {Y2}")

    #Кривая отклонений апроксимации
    fig, ax = plt.subplots(1)
    ax.set_title("Ошибки в процессе обучения")
    ax.set_xlabel("Эпоха")
    ax.set_ylabel("Отклонение (E)")
    ax.plot(E_vec)
    ax.plot((0, len(E_vec)-1), (E2, E2), label = f"Emin = {E2}")
    ax.legend()
    
    #Отображение результатов обучения
    fig, axs = plt.subplots(1, 2)
    axs[0].set_title("Метод наименьших квадратов")
    axs[0].plot(X, Y, 'o')
    axs[0].plot((X.min(), X.max()), (EvalY(m1, X.min(), c1), EvalY(m1, X.max(), c1)))
    axs[1].set_title("Нейронная сеть")
    axs[1].plot(X, Y, 'o')
    axs[1].plot((X.min(), X.max()), (EvalY(m2, X.min(), c2), EvalY(m2, X.max(), c2)))
    
    plt.show()

if __name__ == "__main__":
    main()