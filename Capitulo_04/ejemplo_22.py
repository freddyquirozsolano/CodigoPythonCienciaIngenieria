# Sistema de control de semáforo con sensores
print("=== CONTROL DE SEMÁFORO INTELIGENTE ===\n")

hora = int(input("Hora actual (0-23): "))
dia_semana = input("Día de la semana (lunes-domingo): ").lower()
vehiculos_norte = int(input("Vehículos esperando (Norte): "))
vehiculos_sur = int(input("Vehículos esperando (Sur): "))
vehiculos_este = int(input("Vehículos esperando (Este): "))
vehiculos_oeste = int(input("Vehículos esperando (Oeste): "))
emergencia_detectada = input("¿Emergencia detectada? (s/n): ").lower() == 's'

print("\n" + "=" * 60)
print("ANÁLISIS DE TRÁFICO")
print("=" * 60)

# Calcular flujos principales
flujo_ns = vehiculos_norte + vehiculos_sur  # Norte-Sur
flujo_eo = vehiculos_este + vehiculos_oeste  # Este-Oeste

# Determinar dirección con mayor tráfico
if flujo_ns > flujo_eo:
    direccion_principal = "Norte-Sur"
    flujo_principal = flujo_ns
else:
    direccion_principal = "Este-Oeste"
    flujo_principal = flujo_eo

# Decisión de semáforo
if emergencia_detectada:
    print("🚨 MODO EMERGENCIA")
    print("Semáforo: INTERMITENTE")
    print("Acción: Todos los vehículos deben ceder el paso")
    print("Duración: Hasta que pase vehículo de emergencia")

else:
    # Horario pico
    es_hora_pico = (7 <= hora <= 9) or (17 <= hora <= 19)
    es_dia_laboral = dia_semana in ['lunes', 'martes', 'miércoles', 'jueves', 'viernes']
    
    if es_hora_pico and es_dia_laboral:
        print("⏰ HORARIO PICO DETECTADO")
        
        if flujo_principal > 20:
            print(f"🚦 MODO: Prioridad a {direccion_principal}")
            print(f"Verde {direccion_principal}: 90 segundos")
            print(f"Verde dirección secundaria: 30 segundos")
        else:
            print("🚦 MODO: Estándar horario pico")
            print("Verde ambas direcciones: 60 segundos")
    
    # Horario nocturno
    elif hora >= 22 or hora <= 6:
        print("🌙 HORARIO NOCTURNO")
        
        if flujo_principal < 3:
            print("🚦 MODO: Intermitente")
            print("Amarillo intermitente en todas direcciones")
        else:
            print("🚦 MODO: Ciclos cortos")
            print("Verde ambas direcciones: 30 segundos")
    
    # Horario normal
    else:
        print("☀️ HORARIO NORMAL")
        
        if flujo_principal > 15:
            print(f"🚦 MODO: Prioridad a {direccion_principal}")
            print(f"Verde {direccion_principal}: 60 segundos")
            print(f"Verde dirección secundaria: 40 segundos")
        else:
            print("🚦 MODO: Balanceado")
            print("Verde ambas direcciones: 45 segundos")

print(f"\nTráfico total: {flujo_ns + flujo_eo} vehículos")
print(f"Flujo Norte-Sur: {flujo_ns} vehículos")
print(f"Flujo Este-Oeste: {flujo_eo} vehículos")
print("=" * 60)