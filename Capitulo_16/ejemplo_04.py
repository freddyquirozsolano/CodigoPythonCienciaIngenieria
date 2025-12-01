import pandas as pd

# Desde diccionario
datos_pacientes = {
    'nombre': ['María', 'Juan', 'Ana', 'Carlos'],
    'edad': [45, 32, 28, 51],
    'peso': [65.5, 78.2, 58.9, 85.0],
    'altura': [1.65, 1.78, 1.60, 1.75],
    'tipo_sangre': ['O+', 'A+', 'B-', 'AB+']
}

df_pacientes = pd.DataFrame(datos_pacientes)
print(df_pacientes)
# Salida esperada:
#     nombre  edad  peso  altura tipo_sangre
# 0    María    45  65.5    1.65          O+
# 1     Juan    32  78.2    1.78          A+
# 2      Ana    28  58.9    1.60          B-
# 3   Carlos    51  85.0    1.75         AB+


# Desde lista de diccionarios
sensores = [
    {'id': 'S1', 'tipo': 'temperatura', 'valor': 25.5},
    {'id': 'S2', 'tipo': 'humedad', 'valor': 65.0},
    {'id': 'S3', 'tipo': 'presion', 'valor': 1013.25}
]

df_sensores = pd.DataFrame(sensores)
print(df_sensores)

# Ver primeras filas
print(df_pacientes.head())          # Por defecto 5 filas
print(df_pacientes.head(2))         # Primeras 2 filas

# Ver últimas filas
print(df_pacientes.tail())

# Información general
print(df_pacientes.info())
# Salida esperada:
# lass 'pandas.core.frame.DataFrame'>
# RangeIndex: 4 entries, 0 to 3
# Data columns (total 5 columns):
#  #   Column        Non-Null Count  Dtype  
# ---  ------        --------------  -----  
#  0   nombre        4 non-null      object 
#  1   edad          4 non-null      int64  
#  2   peso          4 non-null      float64
#  3   altura        4 non-null      float64
#  4   tipo_sangre   4 non-null      object 
# dtypes: float64(2), int64(1), object(2)

# Estadísticas descriptivas
print(df_pacientes.describe())
# Salida esperada:
#            edad      peso    altura
# count   4.000000   4.000000  4.000000
# mean   39.000000  71.900000  1.695000
# std    10.440307  11.665584  0.081854
# min    28.000000  58.900000  1.600000
# 25%    31.000000  63.425000  1.637500
# 50%    38.500000  71.850000  1.700000
# 75%    47.000000  80.425000  1.757500
# max    51.000000  85.000000  1.780000

# Dimensiones
print(f"Filas: {df_pacientes.shape[0]}, Columnas: {df_pacientes.shape[1]}")
print(f"Columnas: {df_pacientes.columns.tolist()}")
