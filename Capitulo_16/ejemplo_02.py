import pandas as pd
# Crear Serie desde lista
temperaturas = pd.Series([36.5, 37.2, 36.8, 37.0, 36.9])
print(temperaturas)

# Crear Serie con índices personalizados
pacientes_fc = pd.Series(
    [72, 68, 75, 80],
    index=['Paciente A', 'Paciente B', 'Paciente C', 'Paciente D']
)
print(pacientes_fc)

# Crear Serie desde diccionario
datos_sensor = pd.Series({
    'temperatura': 25.5,
    'humedad': 65.0,
    'presion': 1013.25
})
print(datos_sensor)

# Acceder a elementos
print(pacientes_fc['Paciente A'])  # 72
print(pacientes_fc[0])             # También por posición: 72

# Operaciones vectorizadas
temperaturas_f = temperaturas * 9/5 + 32  # Convertir a Fahrenheit
print(temperaturas_f)

# Filtrado
alta_fc = pacientes_fc[pacientes_fc > 70]
print(alta_fc)
# Paciente A    72
# Paciente C    75
# Paciente D    80

# Estadísticas descriptivas
print(f"Promedio: {temperaturas.mean():.2f}")
print(f"Máximo: {temperaturas.max():.2f}")
print(f"Mínimo: {temperaturas.min():.2f}")
print(f"Desviación estándar: {temperaturas.std():.2f}")
