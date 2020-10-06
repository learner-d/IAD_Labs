import numpy
import math

X = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

Y = numpy.array([3.6, 4.4, 5.8, 6.2, 7.4, 8, 9.2, 10.4, 11.8])


N = 9

E = numpy.zeros(N)

sumX = X.sum()

sumY = Y.sum()

sumXY = (X*Y).sum()

sumXX = (X*X).sum()



