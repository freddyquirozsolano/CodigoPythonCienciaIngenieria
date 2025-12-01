# Monitoreo de robot móvil
bateria = 10.5  # Voltios
temperatura_motor = 68  # Celsius
distancia_obstaculo = 15  # cm

print("=== SISTEMA DE SEGURIDAD DEL ROBOT ===\n")

if bateria < 11.0:
    print("⚠️ ADVERTENCIA: Batería baja")
    print(f"   Nivel de batería: {bateria}V")
    print("   Acción recomendada: Regresar a base de carga")

if temperatura_motor > 65:
    print("⚠️ ADVERTENCIA: Motor sobrecalentado")
    print(f"   Temperatura: {temperatura_motor}°C")
    print("   Acción recomendada: Reducir velocidad")

if distancia_obstaculo < 20:
    print("⚠️ ADVERTENCIA: Obstáculo cercano")
    print(f"   Distancia: {distancia_obstaculo} cm")
    print("   Acción recomendada: Detener movimiento")