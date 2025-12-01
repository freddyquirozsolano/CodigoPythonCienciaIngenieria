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

# Estadísticas básicas individuales
print("Media:", df_pacientes['edad'].mean())
print("Mediana:", df_pacientes['edad'].median())
print("Moda:\n", df_pacientes['edad'].mode())
print("Desviación estándar:", df_pacientes['edad'].std())
print("Varianza:", df_pacientes['edad'].var())
print("Mínimo:", df_pacientes['edad'].min())
print("Máximo:", df_pacientes['edad'].max())
print("Cuartil 25%:", df_pacientes['edad'].quantile(0.25))

# Resumen completo (solo numéricas)
print("\nResumen estadístico (columnas numéricas):")
print(df_pacientes.describe())

# Incluir columnas no numéricas
print("\nResumen estadístico (todas las columnas):")
print(df_pacientes.describe(include='all'))

# Contar valores únicos
print("\nConteo de tipos de sangre:")
print(df_pacientes['tipo_sangre'].value_counts())

# Matriz de correlación
correlacion = df_pacientes[['edad', 'peso', 'altura']].corr()
print("\nMatriz de correlación:")
print(correlacion)
