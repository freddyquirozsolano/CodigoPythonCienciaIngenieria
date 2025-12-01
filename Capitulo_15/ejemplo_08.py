import numpy as np

# Simular señal ECG
frecuencia_muestreo = 500  # Hz
duracion = 3  # segundos
t = np.linspace(0, duracion, frecuencia_muestreo * duracion)

# Simular latidos cardíacos (frecuencia cardíaca: 70 bpm)
frecuencia_cardiaca = 70 / 60  # Hz
ecg = np.sin(2 * np.pi * frecuencia_cardiaca * t)

# Agregar ruido realista
ruido = np.random.normal(0, 0.1, len(t))
ecg_ruidoso = ecg + ruido

# Calcular estadísticas
amplitud_promedio = np.mean(np.abs(ecg_ruidoso))
desviacion_std = np.std(ecg_ruidoso)
valor_maximo = np.max(ecg_ruidoso)
valor_minimo = np.min(ecg_ruidoso)

print(f"Amplitud promedio: {amplitud_promedio:.3f}")
print(f"Desviación estándar: {desviacion_std:.3f}")
print(f"Rango: {valor_minimo:.3f} a {valor_maximo:.3f}")
