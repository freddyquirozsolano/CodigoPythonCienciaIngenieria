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

# Agregar nueva columna calculada
df_pacientes['imc'] = df_pacientes['peso'] / (df_pacientes['altura'] ** 2)

# Agregar columna condicional con función
def clasificar_imc(imc):
    if imc < 18.5:
        return 'Bajo peso'
    elif imc < 25:
        return 'Normal'
    elif imc < 30:
        return 'Sobrepeso'
    else:
        return 'Obesidad'

df_pacientes['clasificacion'] = df_pacientes['imc'].apply(clasificar_imc)

# O usando numpy.where
df_pacientes['es_adulto_mayor'] = np.where(
    df_pacientes['edad'] >= 60, 'Sí', 'No'
)

# Modificar valores específicos
df_pacientes.loc[df_pacientes['nombre'] == 'Juan', 'peso'] = 79.5

# Renombrar columnas
df_pacientes.rename(columns={'peso': 'peso_kg', 'altura': 'altura_m'}, inplace=True)

# Eliminar columnas
df_pacientes.drop('clasificacion', axis=1, inplace=True)

# Alternativa (más segura, no modifica inplace)
# df_pacientes = df_pacientes.drop(['clasificacion'], axis=1)

print(df_pacientes)
