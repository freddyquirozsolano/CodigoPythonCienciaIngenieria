# Datos del sensor (llegan como strings desde puerto serial)
voltaje_texto = "3.85"
distancia_texto = "125"
temperatura_texto = "28.5"

# Convertir para procesamiento
voltaje = float(voltaje_texto)
distancia_cm = int(distancia_texto)
temperatura = float(temperatura_texto)

# Convertir distancia a metros
distancia_m = distancia_cm / 100.0

# Determinar estado del sensor
sensor_activo = voltaje > 3.3  # Booleano
print(f"Sensor activo: {sensor_activo}")
print(f"Distancia: {distancia_m:.2f} metros")