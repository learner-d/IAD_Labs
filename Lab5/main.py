import numpy
import math
import matplotlib.pyplot as plt

X = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
Y = numpy.array([3.6, 4.4, 5.8, 6.2, 7.4, 8, 9.2, 10.4, 11.8])

n = 9

#аналитическое описание
#y = m*x + c

#вычислить m
sumX = X.sum()
sumY = Y.sum()
sumXY = (X*Y).sum()
sumXX = (X*X).sum()
m = (n*sumXY - sumX*sumY) / (n*sumXX - sumX**2)


#вычислить c
c = (sumY - m*sumX) / n

def y(x):
    return m*x + c

E = numpy.zeros(n)
for i in range(n):
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

