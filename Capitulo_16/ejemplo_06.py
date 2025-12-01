import pandas as pd
import numpy as np

# Crear DataFrame con valores faltantes
datos_con_nan = {
    'sensor_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
    'temperatura': [25.5, np.nan, 26.8, 25.2, np.nan],
    'humedad': [60, 65, np.nan, 58, 62],
    'presion': [1013, 1015, 1012, np.nan, 1014]
}

df_sensores = pd.DataFrame(datos_con_nan)

# Detectar valores faltantes
print("Valores faltantes (True donde hay NaN):")
print(df_sensores.isnull())

print("\nConteo de NaN por columna:")
print(df_sensores.isnull().sum())
# Salida esperada:
# sensor_id      0
# temperatura    2
# humedad        1
# presion        1
# dtype: int64

# Eliminar filas con cualquier NaN
df_limpio = df_sensores.dropna()
print("\nDataFrame después de dropna():")
print(df_limpio)
# Solo quedaría la fila 0 si no hubiera más valores NaN

# Eliminar columnas con NaN
df_sin_col_nan = df_sensores.dropna(axis=1)
print("\nColumnas sin NaN:")
print(df_sin_col_nan.columns.tolist())

# Rellenar valores faltantes
# Con un valor específico
df_relleno_cero = df_sensores.fillna(0)
print("\nRellenado con ceros:")
print(df_relleno_cero)

# Con la media de la columna
df_sensores['temperatura'] = df_sensores['temperatura'].fillna(
    df_sensores['temperatura'].mean()
)
print("\nTemperaturas rellenadas con la media:")
print(df_sensores['temperatura'])

# Forward fill (usar valor anterior)
df_ffill = df_sensores.ffill()
print("\nForward fill:")
print(df_ffill)

# Backward fill (usar valor siguiente)
df_bfill = df_sensores.bfill()
print("\nBackward fill:")
print(df_bfill)

# Interpolación lineal
df_interpolado = df_sensores.interpolate()
print("\nInterpolación lineal:")
print(df_interpolado)
