# Sistema de navegación de robot móvil
import math

# Trayectoria como lista de coordenadas (x, y)
trayectoria = [(0, 0), (10, 5), (20, 15), (30, 10), (40, 20)]

# Calcular distancia entre puntos consecutivos
distancias = []
for i in range(len(trayectoria) - 1):
    x1, y1 = trayectoria[i]
    x2, y2 = trayectoria[i + 1]
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    distancias.append(dist)

distancia_total = sum(distancias)

print(f"Distancia total recorrida: {distancia_total:.2f} unidades")
print(f"Número de waypoints: {len(trayectoria)}")

for i, dist in enumerate(distancias):
    print(f"Distancia entre waypoint {i} y {i + 1}: {dist:.2f} unidades")