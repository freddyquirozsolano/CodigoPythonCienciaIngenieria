# Análisis de ensayos de resistencia de materiales
import pandas as pd
import numpy as np

# Datos de ensayos de tracción
materiales = ['Acero A36', 'Aluminio 6061', 'Titanio Grade 5', 'Polímero ABS']
n_muestras = 10  # Muestras por material

datos_ensayo = []
np.random.seed(42)

for material in materiales:
    # Valores base aproximados (MPa)
    if material == 'Acero A36':
        base = 400
    elif material == 'Aluminio 6061':
        base = 310
    elif material == 'Titanio Grade 5':
        base = 900
    else:  # ABS
        base = 45

    for i in range(n_muestras):
        datos_ensayo.append({
            'material': material,
            'muestra_id': f"{material[:3]}-{i+1:02d}",
            'resistencia_traccion': np.random.normal(base, base * 0.05),
            'elongacion': np.random.normal(20, 3) if material != 'ABS' else np.random.normal(5, 1),
            'modulo_elasticidad': np.random.normal(200, 10) if material == 'Acero A36' else
                                  np.random.normal(70, 5) if material == 'Aluminio 6061' else
                                  np.random.normal(110, 8) if material == 'Titanio Grade 5' else
                                  np.random.normal(2.3, 0.2)
        })

df_materiales = pd.DataFrame(datos_ensayo)

# Estadísticas por material
resumen_materiales = df_materiales.groupby('material').agg({
    'resistencia_traccion': ['mean', 'std', 'min', 'max'],
    'elongacion': ['mean', 'std'],
    'modulo_elasticidad': ['mean', 'std']
}).round(2)

print("Resumen de propiedades mecánicas:")
print(resumen_materiales)

# Coeficiente de variación (CV) - medida de consistencia
cv_resistencia = df_materiales.groupby('material')['resistencia_traccion'].agg(
    lambda x: (x.std() / x.mean()) * 100
).round(2)

print("\nCoeficiente de variación de resistencia (%):")
print(cv_resistencia)

# Clasificación de muestras
def clasificar_muestra(row):
    media = df_materiales[df_materiales['material'] == row['material']]['resistencia_traccion'].mean()
    std = df_materiales[df_materiales['material'] == row['material']]['resistencia_traccion'].std()
    if row['resistencia_traccion'] < media - std:
        return 'Bajo estándar'
    elif row['resistencia_traccion'] > media + std:
        return 'Superior'
    else:
        return 'Estándar'

df_materiales['clasificacion'] = df_materiales.apply(clasificar_muestra, axis=1)

# Conteo de clasificaciones
clasificaciones = df_materiales.groupby(['material', 'clasificacion']).size().unstack(fill_value=0)
print("\nClasificación de muestras:")
print(clasificaciones)

# Relación resistencia/densidad (específica)
densidades = {
    'Acero A36': 7850,
    'Aluminio 6061': 2700,
    'Titanio Grade 5': 4430,
    'Polímero ABS': 1050
}

df_materiales['densidad'] = df_materiales['material'].map(densidades)
df_materiales['resistencia_especifica'] = df_materiales['resistencia_traccion'] / df_materiales['densidad'] * 1000

ranking = df_materiales.groupby('material')['resistencia_especifica'].mean().sort_values(ascending=False)
print("\nRanking de resistencia específica (MPa·m³/kg):")
print(ranking)
