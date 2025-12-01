# Programa: Registro de signos vitales
print("=== REGISTRO DE SIGNOS VITALES ===")
print()

# Obtener datos del paciente
nombre_paciente = input("Nombre del paciente: ")
edad = int(input("Edad: "))
temperatura = float(input("Temperatura corporal (°C): "))
presion_sistolica = int(input("Presión arterial sistólica (mmHg): "))
presion_diastolica = int(input("Presión arterial diastólica (mmHg): "))
frecuencia_cardiaca = int(input("Frecuencia cardíaca (bpm): "))

# Mostrar resumen
print("\n=== RESUMEN DE SIGNOS VITALES ===")
print(f"Paciente: {nombre_paciente}, {edad} años")
print(f"Temperatura: {temperatura}°C")
print(f"Presión arterial: {presion_sistolica}/{presion_diastolica} mmHg")
print(f"Frecuencia cardíaca: {frecuencia_cardiaca} bpm")

# Análisis básico
fiebre = temperatura > 37.5
hipertenso = presion_sistolica > 140 or presion_diastolica > 90
taquicardia = frecuencia_cardiaca > 100

if fiebre:
    print("⚠️ Alerta: Temperatura elevada")
if hipertenso:
    print("⚠️ Alerta: Presión arterial elevada")
if taquicardia:
    print("⚠️ Alerta: Frecuencia cardíaca elevada")