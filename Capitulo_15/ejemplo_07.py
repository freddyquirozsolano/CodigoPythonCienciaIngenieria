import numpy as np

matriz = np.array([[1, 2], [3, 4]])

# Determinante
det = np.linalg.det(matriz)
print(f"Determinante: {det:.2f}")  # -2.00

# Inversa
inv = np.linalg.inv(matriz)
print("Inversa:")
print(inv)

# Valores y vectores propios
valores, vectores = np.linalg.eig(matriz)
print("Valores propios:", valores)

# Norma de un vector
vector = np.array([3, 4])
norma = np.linalg.norm(vector)  # √(3² + 4²) = 5.0
