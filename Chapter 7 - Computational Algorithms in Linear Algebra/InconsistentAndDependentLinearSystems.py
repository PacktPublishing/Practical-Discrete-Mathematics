# Inconsistent and Dependent Linear Systems

import numpy

# inconsistent system
A = numpy.array([[2, 1], [6, 3]])
b = numpy.array([3, 3])

print(numpy.linalg.solve(A,b))

# dependent system
A = numpy.array([[2, 1], [6, 3]])
b = numpy.array([1, 3])

print(numpy.linalg.solve(A,b))