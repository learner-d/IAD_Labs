import numpy
import math
import matplotlib.pyplot as plt
from Constants import *

#аналитическое описание
#y = m*x + c

#вычислить m
m = (N*sumXY - sumX*sumY) / (N*sumXX - sumX**2)


#вычислить c
c = (sumY - m*sumX) / N

def y(x):
    return m*x + c

for i in range(N):
    E[i] = math.fabs(Y[i] - y(X[i]))

e = (E*E).sum()

print(f"X: {X}")
print(f"Y: {Y}")
print(f"y = {m}*x + {c}")
print(f"E: {E}")
print(f"e = {e}")


#plt.plot(X, Y, 'o')
#plt.plot((X.min(), X.max()), (y(X.min()), y(X.max())))
#plt.grid(True)
#plt.show()

