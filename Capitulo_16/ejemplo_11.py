# Análisis de signos vitales de pacientes en UCI
import pandas as pd
import numpy as np

# Crear dataset de ejemplo
np.random.seed(42)
n_registros = 100

datos_uci = {
    'timestamp': pd.date_range('2025-01-01', periods=n_registros, freq='1H'),
    'paciente_id': np.random.choice(['P001', 'P002', 'P003'], n_registros),
    'fc': np.random.normal(75, 10, n_registros),  # Frecuencia cardíaca
    'presion_sistolica': np.random.normal(120, 15, n_registros),
    'presion_diastolica': np.random.normal(80, 10, n_registros),
    'spo2': np.random.normal(97, 2, n_registros),  # Saturación de oxígeno
    'temperatura': np.random.normal(37, 0.5, n_registros)
}

df_uci = pd.DataFrame(datos_uci)

# Análisis por paciente
analisis_paciente = df_uci.groupby('paciente_id').agg({
    'fc': ['mean', 'min', 'max', 'std'],
    'presion_sistolica': ['mean', 'std'],
    'temperatura': ['mean', 'max']
})

print("Resumen por paciente:")
print(analisis_paciente)

# Detectar alertas (valores anormales)
df_uci['alerta_taquicardia'] = df_uci['fc'] > 100
df_uci['alerta_hipertension'] = df_uci['presion_sistolica'] > 140
df_uci['alerta_hipoxia'] = df_uci['spo2'] < 92
df_uci['alerta_fiebre'] = df_uci['temperatura'] > 38

# Contar alertas por paciente
alertas = df_uci.groupby('paciente_id')[
    ['alerta_taquicardia', 'alerta_hipertension', 'alerta_hipoxia', 'alerta_fiebre']
].sum()

print("\nAlertas por paciente:")
print(alertas)

# Calcular tendencia temporal de signos vitales
tendencia = df_uci.set_index('timestamp').groupby('paciente_id').resample('6H').mean()
print("\nTendencia cada 6 horas:")
print(tendencia.head(10))
