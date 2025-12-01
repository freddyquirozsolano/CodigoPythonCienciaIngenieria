# Datos del paciente
nombre_paciente = "Ana García"
edad = 45
temperatura = 37.234
presion_sistolica = 128
presion_diastolica = 82
frecuencia_cardiaca = 76
saturacion_oxigeno = 97.8
peso = 68.5
altura = 1.65
imc = peso / (altura ** 2)

# Reporte formateado profesionalmente
print("=" * 60)
print(f"{'REPORTE DE SIGNOS VITALES':^60}")
print("=" * 60)
print()
print(f"Paciente: {nombre_paciente:<30} Edad: {edad:>3} años")
print(f"Peso: {peso:>6.1f} kg       Altura: {altura:>4.2f} m       IMC: {imc:>5.2f}")
print()
print("-" * 60)
print(f"{'SIGNOS VITALES':^60}")
print("-" * 60)
print(f"Temperatura corporal:    {temperatura:>6.1f}°C")
print(f"Presión arterial:        {presion_sistolica:>3}/{presion_diastolica:<3} mmHg")
print(f"Frecuencia cardíaca:     {frecuencia_cardiaca:>6} bpm")
print(f"Saturación de oxígeno:   {saturacion_oxigeno:>6.1f}%")
print()

# Interpretación con formato condicional
if temperatura > 37.5:
    estado_temp = "⚠️ ELEVADA"
else:
    estado_temp = "✓ Normal"

print(f"Estado: {estado_temp}")
print("=" * 60)