import numpy
import math
from Constants import N, X, Y

#Возвращает коэфициенты m, c
def calculate():
    sumX = X.sum()
    sumY = Y.sum()
    sumXY = (X*Y).sum()
    sumXX = (X*X).sum()
    
    #Вычислить m
    m = (N*sumXY - sumX*sumY) / (N*sumXX - sumX**2)
    
    #Вычислить c
    c = (sumY - m*sumX) / N

    return m, c