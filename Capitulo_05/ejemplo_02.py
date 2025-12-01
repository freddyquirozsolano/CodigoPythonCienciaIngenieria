# Sistema de monitoreo que se detiene cuando signos vitales son estables
print("=== SISTEMA DE MONITOREO DE PACIENTE ===\n")

frecuencia_cardiaca = 110  # bpm inicial elevada
lecturas = 0
max_lecturas = 10

print("Iniciando monitoreo continuo...")

while frecuencia_cardiaca > 100 and lecturas < max_lecturas:
    lecturas += 1
    print(f"Lectura {lecturas}: FC = {frecuencia_cardiaca} bpm")
    
    # Simular estabilización gradual
    frecuencia_cardiaca -= 5
    
    if frecuencia_cardiaca > 100:
        print("  ⚠️ Taquicardia - Continuar monitoreo")
    else:
        print("  ✓ Frecuencia normalizada")

print(f"\nMonitoreo completado después de {lecturas} lecturas")
print(f"Frecuencia cardíaca final: {frecuencia_cardiaca} bpm")