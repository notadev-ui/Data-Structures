"""write a program in python to create 
a 2x2 matrix and determine the following:"""

import numpy as np
# define the 2*2 matrix #
matrix1 = np.array([[4,6],[8,10]])
print(f"\n matrix1:\n {matrix1}")

#(i) Data type#
print(f"\n Data type : \n {matrix1.dtype}") 

#(ii) Rank of the matrix#
print(f"\n rank:\n {matrix1.ndim}")

#(iii) Order of the matrix#
print(f"\n Order of the matrix :\n {matrix1.shape}")

#(iv) Convert the matrix into 1-D array#
print(f"\n 1-D array:\n {matrix1.flatten()}")

"""(v) Create another 2x2 matrix and perform addition, 
subtraction, and division  operations"""

matrix2 = np.array([[2,3],[4,5]])
print(f"\n matrix2 :\n {matrix2}")

# (i) Matrix Addition
add= np.add(matrix1, matrix2)
print("\n Matrix Add:\n", add)

# (ii) Matrix Subtraction
sub = np.subtract(matrix1, matrix2)
print("\nMatrix Subtraction:\n", sub)

# (iii) Matrix Division

division = np.divide(matrix1, matrix2)
print("\nMatrix Division:\n", division)

