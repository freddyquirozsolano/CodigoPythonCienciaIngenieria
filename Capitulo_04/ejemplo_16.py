# Operador AND - Ambas condiciones deben ser True
edad = 25
tiene_licencia = True

if edad >= 18 and tiene_licencia:
    print("Puede conducir")
else:
    print("No puede conducir")

# Ejemplo médico
temperatura = 37.8
tos = True
fiebre = temperatura > 37.5

if fiebre and tos:
    print("Posible infección respiratoria")
    print("Se recomienda evaluación médica")

# Múltiples condiciones con AND
presion_sistolica = 125
presion_diastolica = 85
edad_paciente = 45

if presion_sistolica > 120 and presion_diastolica > 80 and edad_paciente > 40:
    print("Paciente en riesgo de hipertensión")
    print("Monitoreo frecuente recomendado")