import numpy as np
A = np.array([[3,1], [1,3]])
l, v = np.linalg.eig(A)
print("The eigenvalues are:\n ",l)
print("The eigenvectors are:\n ", v)