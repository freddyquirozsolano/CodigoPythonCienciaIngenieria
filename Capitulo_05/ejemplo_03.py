# Robot busca objetivo hasta encontrarlo o agotar batería
print("=== SISTEMA DE NAVEGACIÓN AUTÓNOMA ===\n")

distancia_objetivo = 100  # metros
posicion_actual = 0
bateria = 100  # porcentaje
velocidad = 5  # metros por iteración

print(f"Objetivo a {distancia_objetivo} metros")
print(f"Batería: {bateria}%\n")

iteracion = 0
while posicion_actual < distancia_objetivo and bateria > 10:
    iteracion += 1
    
    # Avanzar
    posicion_actual += velocidad
    bateria -= 2  # Consumo por iteración
    
    distancia_restante = distancia_objetivo - posicion_actual
    
    print(f"Iteración {iteracion}:")
    print(f"  Posición: {posicion_actual}m")
    print(f"  Batería: {bateria}%")
    print(f"  Distancia restante: {max(0, distancia_restante)}m")
    
    if distancia_restante <= 0:
        print("  ✓ OBJETIVO ALCANZADO")
    elif bateria <= 10:
        print("  ⚠️ BATERÍA CRÍTICA")
    print()

if posicion_actual >= distancia_objetivo:
    print("✓ Misión exitosa")
else:
    print("✗ Misión abortada por batería baja")