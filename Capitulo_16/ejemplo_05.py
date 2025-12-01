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

# Seleccionar columna (retorna Serie)
edades = df_pacientes['edad']
print(edades)

# Seleccionar múltiples columnas (retorna DataFrame)
df_basico = df_pacientes[['nombre', 'edad']]
print(df_basico)

# Seleccionar filas por índice (loc usa etiquetas)
print(df_pacientes.loc[0])         # Primera fila
print(df_pacientes.loc[0:2])       # Filas 0, 1, 2 (inclusivo)

# Seleccionar por posición (iloc usa índices numéricos)
print(df_pacientes.iloc[0])        # Primera fila
print(df_pacientes.iloc[0:2])      # Filas 0, 1 (exclusivo)

# Filtrado condicional
mayores_40 = df_pacientes[df_pacientes['edad'] > 40]
print(mayores_40)

# Filtrado múltiple
jovenes_ligeros = df_pacientes[
    (df_pacientes['edad'] < 35) & (df_pacientes['peso'] < 70)
]
print(jovenes_ligeros)

# Selección específica
print(df_pacientes.loc[1, 'nombre'])                # Valor específico: 'Juan'
print(df_pacientes.loc[0:2, ['nombre', 'edad']])    # Subconjunto
