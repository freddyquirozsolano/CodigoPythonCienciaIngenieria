import numpy as np

# Multiplicación de matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Multiplicación elemento a elemento
C = A * B  # [[5, 12], [21, 32]]

# Producto matricial (dot product)
D = np.dot(A, B)  # o A @ B
# [[19 22]
#  [43 50]]

# Transpuesta
A_T = A.T  # o np.transpose(A)
print(A_T)
# [[1 3]
#  [2 4]]
