# Procesamiento de señal ECG con eliminación de artefactos
print("=== PROCESAMIENTO DE SEÑAL ECG ===\n")

# Señal ECG simulada con algunos artefactos
ecg_signal = [72, 75, 78, 500, 74, 76, 78, 80, 82, -100, 
              79, 76, 74, 72, 70, 1000, 72, 75, 78, 80]

print(f"Muestras totales: {len(ecg_signal)}")
print("Rango normal: 60-100 bpm\n")

señal_limpia = []
artefactos_detectados = 0

for i, valor in enumerate(ecg_signal):
    # Detectar artefactos (valores fuera de rango fisiológico)
    if valor < 40 or valor > 200:
        artefactos_detectados += 1
        print(f"⚠️ Muestra {i}: Artefacto detectado ({valor}) - OMITIDO")
        continue  # Saltar este valor
    
    señal_limpia.append(valor)

print(f"\nARTEFACTOS DETECTADOS: {artefactos_detectados}")
print(f"MUESTRAS VÁLIDAS: {len(señal_limpia)}")

if len(señal_limpia) > 0:
    fc_promedio = sum(señal_limpia) / len(señal_limpia)
    fc_maxima = max(señal_limpia)
    fc_minima = min(señal_limpia)
    
    print(f"\nANÁLISIS DE SEÑAL LIMPIA:")
    print(f"Frecuencia cardíaca promedio: {fc_promedio:.1f} bpm")
    print(f"FC máxima: {fc_maxima} bpm")
    print(f"FC mínima: {fc_minima} bpm")
    
    if fc_promedio > 100:
        print("\n⚠️ Taquicardia detectada")
    elif fc_promedio < 60:
        print("\n⚠️ Bradicardia detectada")
    else:
        print("\n✓ Frecuencia cardíaca normal")