import numpy as np

# Sistema: 2x + 3y = 8
#          4x - y = 2

A = np.array([[2, 3], [4, -1]])
b = np.array([8, 2])

# Resolver Ax = b
x = np.linalg.solve(A, b)
print(f"Solución: x={x[0]:.2f}, y={x[1]:.2f}")
