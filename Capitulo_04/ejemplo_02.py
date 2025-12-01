# Sistema de alertas médicas
frecuencia_cardiaca = 105
presion_sistolica = 145
saturacion_oxigeno = 94.5

print("=== SISTEMA DE MONITOREO DE PACIENTE ===\n")

if frecuencia_cardiaca > 100:
    print("⚠️ ALERTA: Taquicardia detectada")
    print(f"   Frecuencia cardíaca: {frecuencia_cardiaca} bpm")

if presion_sistolica > 140:
    print("⚠️ ALERTA: Hipertensión detectada")
    print(f"   Presión sistólica: {presion_sistolica} mmHg")

if saturacion_oxigeno < 95:
    print("⚠️ ALERTA: Saturación de oxígeno baja")
    print(f"   Saturación: {saturacion_oxigeno}%")

print("\nMonitoreo completado")