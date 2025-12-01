import numpy as np 
# Análisis de armadura simple (Método de nodos)
# Consideremos una armadura triangular simple

# Matriz de equilibrio (ecuaciones de balance de fuerzas)
# Sistema de ecuaciones: Ax = b
# donde x son las fuerzas desconocidas en los miembros

A = np.array([
    [1,  0.707,  0],        # Nodo 1: ΣFx = 0
    [0,  0.707, -1],        # Nodo 1: ΣFy = 0
    [0,  1,      1]         # Nodo 2: ΣFy = 0
])

# Cargas aplicadas (N)
b = np.array([0, -5000, 0])  # Carga de 5000 N hacia abajo

# Resolver para fuerzas en los miembros
fuerzas = np.linalg.solve(A, b)

print("Fuerzas en los miembros:")
print(f"  Miembro 1: {fuerzas[0]:.0f} N {'(Tensión)' if fuerzas[0] > 0 else '(Compresión)'}")
print(f"  Miembro 2: {fuerzas[1]:.0f} N {'(Tensión)' if fuerzas[1] > 0 else '(Compresión)'}")
print(f"  Miembro 3: {fuerzas[2]:.0f} N {'(Tensión)' if fuerzas[2] > 0 else '(Compresión)'}")
