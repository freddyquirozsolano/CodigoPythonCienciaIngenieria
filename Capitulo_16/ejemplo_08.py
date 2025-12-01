import pandas as pd
import numpy as np

# Datos de ejemplo
datos_pacientes = {
    'nombre': ['María', 'Juan', 'Ana', 'Carlos'],
    'edad': [45, 32, 28, 51],
    'peso': [65.5, 78.2, 58.9, 85.0],
    'altura': [1.65, 1.78, 1.60, 1.75],
    'tipo_sangre': ['O+', 'A+', 'B-', 'AB+']
}

df_pacientes = pd.DataFrame(datos_pacientes)

# Ver tipos de datos
print("Tipos de datos originales:")
print(df_pacientes.dtypes)

# Convertir tipos
df_pacientes['edad'] = df_pacientes['edad'].astype('float')
df_pacientes['tipo_sangre'] = df_pacientes['tipo_sangre'].astype('category')

print("\nTipos de datos después de conversión:")
print(df_pacientes.dtypes)

# Convertir a datetime
fechas = pd.Series(['2025-01-01', '2025-01-02', '2025-01-03'])
fechas_dt = pd.to_datetime(fechas)
print("\nFechas convertidas a datetime:")
print(fechas_dt)

# Convertir strings a numérico (maneja errores)
valores_str = pd.Series(['10', '20', 'error', '30'])
valores_num = pd.to_numeric(valores_str, errors='coerce')
# 'coerce' convierte errores a NaN

print("\nValores numéricos (errores convertidos a NaN):")
print(valores_num)
# Salida esperada:
# [10.0, 20.0, NaN, 30.0]
