# Sistema de gestión de prioridades
print("=== SISTEMA DE PRIORIDAD DE PROCESOS ===\n")

uso_cpu = float(input("Uso de CPU (%): "))
uso_memoria = float(input("Uso de memoria (%): "))
tiempo_espera = int(input("Tiempo en espera (segundos): "))

print(f"\nAnálisis de proceso...")
print("-" * 50)

# Calcular score de prioridad
score_recursos = (uso_cpu + uso_memoria) / 2
score_tiempo = min(tiempo_espera / 10, 50)  # Máximo 50 puntos
score_total = score_recursos + score_tiempo

if score_total >= 120:
    prioridad = "CRÍTICA"
    nivel = 0
    accion = "Ejecutar inmediatamente"
    simbolo = "🔴"
elif score_total >= 90:
    prioridad = "MUY ALTA"
    nivel = 1
    accion = "Ejecutar en los próximos 5 segundos"
    simbolo = "🟠"
elif score_total >= 60:
    prioridad = "ALTA"
    nivel = 2
    accion = "Ejecutar en los próximos 30 segundos"
    simbolo = "🟡"
elif score_total >= 30:
    prioridad = "MEDIA"
    nivel = 3
    accion = "Ejecutar en los próximos 2 minutos"
    simbolo = "🔵"
else:
    prioridad = "BAJA"
    nivel = 4
    accion = "Ejecutar cuando haya recursos disponibles"
    simbolo = "⚪"

print(f"{simbolo} Prioridad: {prioridad} (Nivel {nivel})")
print(f"Score total: {score_total:.1f}/150")
print(f"  - Recursos: {score_recursos:.1f}")
print(f"  - Tiempo espera: {score_tiempo:.1f}")
print(f"\nAcción: {accion}")
print("-" * 50)