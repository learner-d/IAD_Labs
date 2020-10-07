import numpy
import math
import random
from Constants import N, X, Y

N_Epochs = 300
TrainRate = 0.009

#возвращает максимальное по модулю E
#возвращает x в точке максимального отколонения
def error(m, c):
    err_vec = numpy.absolute(Y - (X*m + c))
    return err_vec.max()

#дельта-коррекция
def correction(w, E):
    return w * E * TrainRate

def correct(m, c, E):
    m1 = m + correction(m, E)
    m2 = m - correction(m, E)
    c1 = c + correction(c, E)
    c2 = c - correction(c, E)
    
    E1 = error(m1, c1)
    E2 = error(m2, c2)

    if E1 < E2:
        return m1, c1, E1
    else:
        return m2, c2, E2

#Возвращает векторы m, c, E
def train():
    m_vec = numpy.zeros(N_Epochs)
    c_vec = numpy.zeros(N_Epochs)
    E_vec = numpy.zeros(N_Epochs)
    
    m = random.uniform(0, 0.5)
    c = random.uniform(0, 0.5)
    E = error(m, c)

    for i in range(N_Epochs):
        m, c, E = correct(m, c, E)
        m_vec[i] = m
        c_vec[i] = c
        E_vec[i] = E

    return m_vec, c_vec, E_vec