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

# Si deseas cargar datos desde un archivo, puedes usar:
# Desde archivo CSV
# df = pd.read_csv('datos.csv')

# Desde Excel
# df = pd.read_excel('datos.xlsx', sheet_name='Hoja1')
