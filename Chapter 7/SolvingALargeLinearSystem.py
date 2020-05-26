# Solving a Large Linear System

import numpy

# Set a random seed so the code below is reproducible
numpy.random.seed(1)

# Create A and b matrices with random
A = 10*numpy.random.rand(10,10)-5
b = 10*numpy.random.rand(10)-5

# Solve Ax = b
solution = numpy.linalg.solve(A,b)
print(solution)

# To verify the solution works, show Ax - b is near 0
sum(abs(numpy.dot(A,solution) - b))