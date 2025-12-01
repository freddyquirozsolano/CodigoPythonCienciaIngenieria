# Análisis de datos médicos con módulos estándar
import statistics
import datetime

# Registros de temperatura de un paciente
temperaturas = [36.5, 37.2, 36.8, 37.0, 36.9, 37.5, 36.7]

# Análisis estadístico
promedio = statistics.mean(temperaturas)
desviacion = statistics.stdev(temperaturas)
mediana = statistics.median(temperaturas)

print(f"Temperatura promedio: {promedio:.2f}°C")
print(f"Desviación estándar: {desviacion:.2f}")
print(f"Mediana: {mediana}°C")

# Timestamp del registro
registro = datetime.datetime.now()
print(f"\nRegistro realizado: {registro.strftime('%Y-%m-%d %H:%M')}")

# Clasificación
if promedio > 37.5:
    print("ALERTA: Fiebre detectada")
elif promedio < 36:
    print("ALERTA: Hipotermia detectada")
else:
    print("Temperatura normal")