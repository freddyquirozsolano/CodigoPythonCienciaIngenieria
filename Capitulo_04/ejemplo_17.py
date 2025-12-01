# Operador OR - Al menos una condición debe ser True
temperatura = 38.0
dolor_cabeza = True

if temperatura > 37.5 or dolor_cabeza:
    print("Paciente presenta síntomas")
    print("Evaluación recomendada")

# Ejemplo robótica
bateria = 10.5
temperatura_motor = 70

if bateria < 11.0 or temperatura_motor > 65:
    print("⚠️ Sistema requiere atención")
    if bateria < 11.0:
        print("  - Batería baja")
    if temperatura_motor > 65:
        print("  - Motor sobrecalentado")

# Emergencias que requieren detención inmediata
obstaculo_frontal = True
bateria_critica = False
error_sensor = False

if obstaculo_frontal or bateria_critica or error_sensor:
    print("🛑 DETENER ROBOT")
    print("Condición de emergencia detectada")