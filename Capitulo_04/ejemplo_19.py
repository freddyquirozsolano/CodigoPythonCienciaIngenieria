# Combinación compleja de operadores
edad = 30
experiencia = 5
certificacion = True
disponible = True

# Criterios de contratación
if (edad >= 25 and experiencia >= 3) and (certificacion or experiencia >= 10):
    if disponible:
        print("✓ Candidato ACEPTADO")
        print("Cumple todos los requisitos")
    else:
        print("⏸ Candidato CALIFICADO pero no disponible")
else:
    print("✗ Candidato NO CALIFICADO")

# Sistema médico complejo
temperatura = 38.5
tos = True
dificultad_respiratoria = False
contacto_covid = True
dias_sintomas = 3

# Evaluación de riesgo COVID-19
if (temperatura > 37.5 or tos or dificultad_respiratoria) and contacto_covid:
    print("🔴 RIESGO ALTO - Prueba COVID recomendada")
elif (temperatura > 37.5 or tos) and dias_sintomas > 5:
    print("🟡 RIESGO MEDIO - Evaluación médica recomendada")
elif temperatura > 37.5 or tos or dificultad_respiratoria:
    print("🟢 RIESGO BAJO - Monitorear síntomas")
else:
    print("✓ Sin síntomas relevantes")