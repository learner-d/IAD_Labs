import numpy
import math
from Constants import *

#аналитическое описание
#y = m*x + c


#вычислить m
m = (N*sumXY - sumX*sumY) / (N*sumXX - sumX**2)

#вычислить c
c = (sumY - m*sumX) / N


#Функция подсчёта "y"

def y(x):
    return m*x + c

#Заполнение массива E
for i in range(N):
    E[i] = math.fabs(Y[i] - y(X[i]))

#Подсчет e 
e = (E*E).sum()