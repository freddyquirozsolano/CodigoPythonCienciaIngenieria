coordenadas = (10, 20, 30)

# Acceso por índice (igual que listas)
x = coordenadas[0]  # 10
z = coordenadas[-1]  # 30

# Slicing
primeros_dos = coordenadas[:2]  # (10, 20)

# Concatenación (crea nueva tupla)
punto1 = (1, 2)
punto2 = (3, 4)
linea = punto1 + punto2  # (1, 2, 3, 4)

# Repetición
base = (0,)
ceros = base * 5  # (0, 0, 0, 0, 0)

# Desempaquetado
x, y, z = coordenadas  # x=10, y=20, z=30

print("Coordenadas:", coordenadas)