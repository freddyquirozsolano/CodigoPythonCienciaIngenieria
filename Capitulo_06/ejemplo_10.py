# Forma tradicional con bucle
cuadrados = []
for i in range(10):
    cuadrados.append(i ** 2)

# Mismo resultado con list comprehension
cuadrados = [i ** 2 for i in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
