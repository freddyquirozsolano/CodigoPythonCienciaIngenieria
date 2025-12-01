# Control adaptativo de velocidad del robot
print("=== SISTEMA DE CONTROL DE VELOCIDAD ===\n")

distancia_obstaculo = float(input("Distancia al obstáculo (cm): "))
velocidad_actual = float(input("Velocidad actual (m/s): "))

print(f"\nAnalizando condiciones...")
print("-" * 50)

if distancia_obstaculo < 10:
    accion = "DETENER INMEDIATAMENTE"
    velocidad_objetivo = 0.0
    nivel_urgencia = "🔴 CRÍTICO"
    justificacion = "Colisión inminente"
elif distancia_obstaculo < 30:
    accion = "REDUCIR A VELOCIDAD MÍNIMA"
    velocidad_objetivo = 0.3
    nivel_urgencia = "🟠 ALTO"
    justificacion = "Obstáculo muy cercano"
elif distancia_obstaculo < 50:
    accion = "REDUCIR VELOCIDAD"
    velocidad_objetivo = 1.0
    nivel_urgencia = "🟡 MEDIO"
    justificacion = "Obstáculo cercano"
elif distancia_obstaculo < 100:
    accion = "MANTENER VELOCIDAD MODERADA"
    velocidad_objetivo = 2.0
    nivel_urgencia = "🟢 BAJO"
    justificacion = "Distancia segura"
else:
    accion = "VELOCIDAD MÁXIMA PERMITIDA"
    velocidad_objetivo = 3.5
    nivel_urgencia = "🟢 NINGUNO"
    justificacion = "Camino despejado"

print(f"Nivel de urgencia: {nivel_urgencia}")
print(f"Distancia: {distancia_obstaculo} cm")
print(f"Velocidad actual: {velocidad_actual:.2f} m/s")
print(f"Velocidad objetivo: {velocidad_objetivo:.2f} m/s")
print(f"\nACCIÓN: {accion}")
print(f"Justificación: {justificacion}")

# Calcular ajuste necesario
if velocidad_actual > velocidad_objetivo:
    ajuste = velocidad_actual - velocidad_objetivo
    print(f"\nReducir velocidad en: {ajuste:.2f} m/s")
elif velocidad_actual < velocidad_objetivo:
    ajuste = velocidad_objetivo - velocidad_actual
    print(f"\nAumentar velocidad en: {ajuste:.2f} m/s")
else:
    print(f"\nVelocidad óptima alcanzada")

print("-" * 50)