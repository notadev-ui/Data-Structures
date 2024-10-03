import numpy as np

# Create a 3-D array 
array_3d = np.array([[[1, 2, 3], [4, 5, 6]], 
                     [[7, 8, 9], [10, 11, 12]]])

print("3-D Array:\n", array_3d)

# (i) Transpose of a matrix
print(f"\nTranspose of the 3-D array : \n {array_3d.T}")

# (ii) Create two 3-D arrays for matrix multiplication
array_3d_1 = np.array([[[1, 2], [3, 4]], 
                       [[5, 6], [7, 8]]])

array_3d_2 = np.array([[[9, 8], [7, 6]], 
                       [[5, 4], [3, 2]]])

# Matrix multiplication 
multiplication = np.matmul(array_3d_1, array_3d_2)
print("\nMatrix Multiplication in the 3-D arrays:\n", multiplication)
