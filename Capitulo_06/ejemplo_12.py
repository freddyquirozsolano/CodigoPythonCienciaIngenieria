# Sistema de monitoreo de signos vitales
# Datos de un paciente durante 24 horas

frecuencias_cardiacas = [72, 68, 75, 80, 78, 71, 69, 73, 76, 82, 88, 90]
presiones_sistolicas = [120, 118, 125, 130, 128, 122, 119, 121, 135, 138, 140, 142]
temperaturas = [36.5, 36.6, 36.4, 36.7, 36.8, 37.0, 37.2, 37.5, 37.3, 36.9, 36.7, 36.6]

# Análisis usando listas
fc_promedio = sum(frecuencias_cardiacas) / len(frecuencias_cardiacas)
fc_maxima = max(frecuencias_cardiacas)
fc_minima = min(frecuencias_cardiacas)

# Detectar valores anormales
taquicardia = [fc for fc in frecuencias_cardiacas if fc > 100]
hipertension = [ps for ps in presiones_sistolicas if ps > 140]
fiebre = [t for t in temperaturas if t > 37.5]

print(f"FC Promedio: {fc_promedio:.1f} bpm")
print(f"Alertas de taquicardia: {len(taquicardia)} lecturas")
print(f"Alertas de hipertensión: {len(hipertension)} lecturas")
print(f"Alertas de fiebre: {len(fiebre)} lecturas")