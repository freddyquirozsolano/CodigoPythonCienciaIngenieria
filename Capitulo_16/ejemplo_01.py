import pandas as pd
# Crear Serie desde lista
temperaturas = pd.Series([36.5, 37.2, 36.8, 37.0, 36.9])
print(temperaturas)
# Salida esperada:
# 0    36.5
# 1    37.2
# 2    36.8
# 3    37.0
# 4    36.9
# dtype: float64
# Crear Serie con índices personalizados
pacientes_fc = pd.Series(
    [72, 68, 75, 80],
    index=['Paciente A', 'Paciente B', 'Paciente C', 'Paciente D']
)
print(pacientes_fc)
# Salida esperada:
# Paciente A    72
# Paciente B    68
# Paciente C    75
# Paciente D    80
# dtype: int64

# Crear Serie desde diccionario
datos_sensor = pd.Series({
    'temperatura': 25.5,
    'humedad': 65.0,
    'presion': 1013.25
})
print(datos_sensor)
# Salida esperada:
# temperatura      25.50
# humedad          65.00
# presion        1013.25
# dtype: float64
