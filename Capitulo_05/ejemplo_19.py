# Robot explora y mapea un entorno en cuadrícula
print("=== SISTEMA DE MAPEO DEL ENTORNO ===\n")

# Grid del entorno: 0=libre, 1=obstáculo, 2=sin explorar
grid = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 2],
    [0, 0, 0, 0, 2],
    [1, 0, 1, 0, 2],
    [0, 0, 0, 2, 2]
]

filas = len(grid)
columnas = len(grid[0])

print("MAPA DEL ENTORNO:")
print("  ", end="")
for j in range(columnas):
    print(f"{j} ", end="")
print()

for i in range(filas):
    print(f"{i} ", end="")
    for j in range(columnas):
        if grid[i][j] == 0:
            simbolo = "·"  # Espacio libre
        elif grid[i][j] == 1:
            simbolo = "█"  # Obstáculo
        else:
            simbolo = "?"  # Sin explorar
        print(f"{simbolo} ", end="")
    print()

# Análisis del entorno
espacios_libres = 0
obstaculos = 0
areas_sin_explorar = 0

for i in range(filas):
    for j in range(columnas):
        if grid[i][j] == 0:
            espacios_libres += 1
        elif grid[i][j] == 1:
            obstaculos += 1
        else:
            areas_sin_explorar += 1

total_celdas = filas * columnas
porcentaje_explorado = ((total_celdas - areas_sin_explorar) / total_celdas) * 100

print(f"\nESTADÍSTICAS DEL MAPA:")
print(f"Total de celdas: {total_celdas}")
print(f"Espacios libres: {espacios_libres}")
print(f"Obstáculos: {obstaculos}")
print(f"Sin explorar: {areas_sin_explorar}")
print(f"Progreso de exploración: {porcentaje_explorado:.1f}%")

# Encontrar mejor ruta (simplificado: más espacios libres consecutivos)
mejor_fila = 0
max_espacios_libres = 0

for i in range(filas):
    espacios_consecutivos = 0
    for j in range(columnas):
        if grid[i][j] == 0:
            espacios_consecutivos += 1
    
    if espacios_consecutivos > max_espacios_libres:
        max_espacios_libres = espacios_consecutivos
        mejor_fila = i

print(f"\nRUTA SUGERIDA:")
print(f"Fila {mejor_fila} tiene {max_espacios_libres} espacios libres consecutivos")