# range(stop) - desde 0 hasta stop-1
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop) - desde start hasta stop-1
for i in range(2, 7):
    print(i)  # 2, 3, 4, 5, 6

# range(start, stop, step) - con incremento personalizado
for i in range(0, 20, 5):
    print(i)  # 0, 5, 10, 15

# Contar hacia atrás
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

# Convertir range a lista para visualizar
numeros = list(range(1, 11))
print(numeros)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]