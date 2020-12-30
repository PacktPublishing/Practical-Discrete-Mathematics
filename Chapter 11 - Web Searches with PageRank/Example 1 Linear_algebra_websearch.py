#Creating the initial importance matrix (v) and transition matrix A
import numpy as np
v = np.array([[0.2, 0.2, 0.2, 0.2, 0.2]])
A = np.array([[0, 0.5, 0.33, 1, 0],
              [0.25, 0, 0 ,0, 0],
              [0.25, 0, 0, 0, 0],
              [0.25, 0.5, 0.33, 0, 1],
              [0.25, 0, 0.33, 0, 0]])


#Raising the transition matrix to different powers
from numpy.linalg import matrix_power
A_2 = matrix_power(A, 2)
A_3 = matrix_power(A, 3)
A_4 = matrix_power(A, 4)
A_5 = matrix_power(A, 5)
A_6 = matrix_power(A, 6)
A_7 = matrix_power(A, 7)
A_8 = matrix_power(A, 8)
A_9 = matrix_power(A, 9)
A_10 = matrix_power(A, 10)
A_11 = matrix_power(A, 11)
A_12 = matrix_power(A, 12)
A_13 = matrix_power(A, 13)


#Calculating importance vectors
c1 = np.matmul(A,v.T)
c2 = np.matmul(A_2,v.T)
c3 = np.matmul(A_3, v.T)
c4 = np.matmul(A_4, v.T)
c5 = np.matmul(A_5, v.T)
c6 = np.matmul(A_6, v.T)
c7 = np.matmul(A_7, v.T)
c8 = np.matmul(A_8, v.T)
c9 = np.matmul(A_9, v.T)
c10 = np.matmul(A_10, v.T)
c11 = np.matmul(A_11, v.T)
c12 = np.matmul(A_12, v.T)
c13 = np.matmul(A_13, v.T)


#Printing the importance vectors
np.set_printoptions(precision=3)
print("C1:  ",c1.T)
print("C2:  ",c2.T)
print("C3:  ",c3.T)
print("C4:  ",c4.T)
print("C5:  ",c5.T)
print("C6:  ",c6.T)
print("C7:  ",c7.T)
print("C8:  ",c8.T)
print("C9:  ",c9.T)
print("C10: ",c10.T)
print("C11: ",c11.T)
print("C12: ",c12.T)
print("C13: ",c13.T)