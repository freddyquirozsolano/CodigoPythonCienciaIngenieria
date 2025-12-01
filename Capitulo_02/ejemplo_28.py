# Cálculo de dosis de medicamento
peso_paciente = 70  # kg
dosis_por_kg = 5    # mg/kg
dosis_total = peso_paciente * dosis_por_kg
print(f"Dosis total: {dosis_total} mg")

# Cálculo de índice de masa corporal
peso = 70.0  # kg
altura = 1.75  # metros
imc = peso / (altura ** 2)
print(f"IMC: {imc:.2f}")

# Cálculo de frecuencia cardíaca objetivo
edad = 45
fcm = 220 - edad  # Frecuencia cardíaca máxima
fc_objetivo_min = fcm * 0.6
fc_objetivo_max = fcm * 0.8
print(f"Zona de ejercicio: {fc_objetivo_min:.0f}-{fc_objetivo_max:.0f} bpm")