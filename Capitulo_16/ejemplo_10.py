import pandas as pd
import numpy as np

# Ejemplo con datos de ensayos clínicos
datos_ensayo = {
    'paciente_id': ['P1', 'P2', 'P3', 'P4', 'P5', 'P6'],
    'grupo': ['Control', 'Tratamiento', 'Control', 'Tratamiento', 'Control', 'Tratamiento'],
    'edad': [45, 52, 38, 61, 49, 55],
    'respuesta': [5.2, 7.8, 4.9, 8.5, 5.5, 7.2],
    'efectos_secundarios': [0, 1, 0, 2, 1, 1]
}

df_ensayo = pd.DataFrame(datos_ensayo)

# Agrupar por grupo y calcular promedio
promedios = df_ensayo.groupby('grupo').mean(numeric_only=True)
print("Promedios por grupo:")
print(promedios)
# Salida esperada:
#              edad  respuesta  efectos_secundarios
# grupo                                            
# Control      44.0   5.200000                 0.33
# Tratamiento  56.0   7.833333                 1.33

# Múltiples agregaciones
resumen = df_ensayo.groupby('grupo').agg({
    'edad': ['mean', 'std'],
    'respuesta': ['mean', 'min', 'max'],
    'efectos_secundarios': 'sum'
})
print("\nResumen con múltiples agregaciones:")
print(resumen)

# Agregación personalizada
def rango(serie):
    return serie.max() - serie.min()

rangos = df_ensayo.groupby('grupo').agg({
    'respuesta': rango,
    'edad': rango
})
print("\nRangos por grupo:")
print(rangos)

# Contar por grupo
conteo = df_ensayo.groupby('grupo').size()
print("\nConteo de pacientes por grupo:")
print(conteo)
