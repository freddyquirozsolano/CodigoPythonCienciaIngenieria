# analizador_trayectorias.py
import math

def agregar_waypoint(trayectoria):
    x = float(input("Coordenada X (m): "))
    y = float(input("Coordenada Y (m): "))
    tiempo = float(input("Tiempo (s): "))
    waypoint = (x, y, tiempo)
    trayectoria.append(waypoint)

def calcular_distancia(p1, p2):
    x1, y1, _ = p1
    x2, y2, _ = p2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def analizar_trayectoria(trayectoria):
    # Calcular distancias entre waypoints consecutivos
    distancias = [calcular_distancia(trayectoria[i], trayectoria[i+1])
                  for i in range(len(trayectoria)-1)]
    
    distancia_total = sum(distancias)
    tiempo_total = trayectoria[-1][2] - trayectoria[0][2]
    velocidad_promedio = distancia_total / tiempo_total
    
    print(f"Distancia total: {distancia_total:.2f} m")
    print(f"Velocidad promedio: {velocidad_promedio:.2f} m/s")

# Ejemplo
trayectoria = [(0, 0, 0), (10, 5, 8), (20, 15, 18), (30, 10, 25)]
analizar_trayectoria(trayectoria)
