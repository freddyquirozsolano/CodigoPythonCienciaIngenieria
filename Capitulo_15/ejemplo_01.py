import numpy as np
# Desde una lista
temperaturas = np.array([36.5, 37.2, 36.8, 37.0, 36.9])
print(temperaturas)  # [36.5 37.2 36.8 37.  36.9]

# Array 2D (matriz)
coordenadas = np.array([[0, 0], [10, 5], [20, 15]])
print(coordenadas)
# [[ 0  0]
#  [10  5]
#  [20 15]]

# Arrays especiales
ceros = np.zeros(5)           # [0. 0. 0. 0. 0.]
unos = np.ones((3, 4))        # Matriz 3x4 de unos
identidad = np.eye(3)         # Matriz identidad 3x3
aleatorio = np.random.rand(5) # 5 números aleatorios [0, 1)

# Secuencias
rango = np.arange(0, 10, 2)   # [0 2 4 6 8] (inicio, fin, paso)
lineal = np.linspace(0, 1, 5) # [0.   0.25 0.5  0.75 1.  ] (5 puntos equidistantes)
