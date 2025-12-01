lecturas = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Elementos del índice 2 al 5 (sin incluir el 5)
segmento = lecturas[2:5]  # [30, 40, 50]

# Primeros 3 elementos
primeros = lecturas[:3]  # [10, 20, 30]

# Últimos 3 elementos
ultimos = lecturas[-3:]  # [70, 80, 90]

# Cada 2 elementos
pares = lecturas[::2]  # [10, 30, 50, 70, 90]

# Invertir una lista
invertida = lecturas[::-1]  # [90, 80, 70, 60, 50, 40, 30, 20, 10]

print("Segmento (índices 2 a 5):", segmento)
print("Primeros 3 elementos:", primeros)