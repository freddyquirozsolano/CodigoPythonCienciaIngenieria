sensor_datos = {
    'temperatura': 25.5,
    'humedad': 60,
    'presion': 1013.25
}

# Iterar sobre claves
for clave in sensor_datos:
    print(clave)

# Iterar sobre valores
for valor in sensor_datos.values():
    print(valor)

# Iterar sobre pares clave-valor
for clave, valor in sensor_datos.items():
    print(f"{clave}: {valor}")
