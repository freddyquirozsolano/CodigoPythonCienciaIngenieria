# Robot navegando y evitando obstáculos
print("=== SISTEMA DE NAVEGACIÓN AUTÓNOMA ===\n")

waypoints = [
    (10, 5), (20, 10), (30, 15), (40, 20), 
    (50, 25), (60, 30), (70, 35), (80, 40)
]

# Simular obstáculos en ciertas posiciones
obstaculos = [(30, 15), (60, 30)]

posicion_actual = (0, 0)
waypoint_alcanzados = 0

print(f"Ruta planificada: {len(waypoints)} waypoints")
print(f"Obstáculos conocidos: {len(obstaculos)}\n")

for i, waypoint in enumerate(waypoints):
    print(f"Waypoint {i+1}: {waypoint}")
    
    # Verificar si hay obstáculo
    if waypoint in obstaculos:
        print(f"  ⚠️ OBSTÁCULO DETECTADO en {waypoint}")
        print(f"  → Saltando este waypoint")
        continue  # Saltar este waypoint
    
    # Simular movimiento
    distancia = ((waypoint[0] - posicion_actual[0])**2 + 
                 (waypoint[1] - posicion_actual[1])**2)**0.5
    
    print(f"  → Moviéndose desde {posicion_actual}")
    print(f"  → Distancia: {distancia:.2f} metros")
    print(f"  ✓ Waypoint alcanzado")
    
    posicion_actual = waypoint
    waypoint_alcanzados += 1
    print()

print("=" * 50)
print(f"Navegación completada")
print(f"Waypoints alcanzados: {waypoint_alcanzados}/{len(waypoints)}")
print(f"Waypoints evitados: {len(obstaculos)}")
print(f"Posición final: {posicion_actual}")