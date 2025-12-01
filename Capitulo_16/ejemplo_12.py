# Análisis de datos de telemetría de robot móvil
import pandas as pd
import numpy as np

# Crear dataset de telemetría
np.random.seed(42)
n_muestras = 500

telemetria = {
    'timestamp': pd.date_range('2025-01-01', periods=n_muestras, freq='100ms'),
    'pos_x': np.cumsum(np.random.randn(n_muestras) * 0.1),
    'pos_y': np.cumsum(np.random.randn(n_muestras) * 0.1),
    'velocidad': np.abs(np.random.normal(1.5, 0.3, n_muestras)),
    'bateria': 100 - np.linspace(0, 30, n_muestras) + np.random.randn(n_muestras) * 2,
    'temp_motor_izq': np.random.normal(45, 5, n_muestras),
    'temp_motor_der': np.random.normal(47, 5, n_muestras),
    'corriente_total': np.random.normal(2.5, 0.5, n_muestras)
}

df_telemetria = pd.DataFrame(telemetria)

# Calcular distancia recorrida
df_telemetria['distancia_incremental'] = np.sqrt(
    df_telemetria['pos_x'].diff()**2 + df_telemetria['pos_y'].diff()**2
)
distancia_total = df_telemetria['distancia_incremental'].sum()

print(f"Distancia total recorrida: {distancia_total:.2f} metros")

# Estadísticas de rendimiento
rendimiento = df_telemetria[['velocidad', 'corriente_total', 'bateria']].describe()
print("\nEstadísticas de rendimiento:")
print(rendimiento)

# Detectar problemas
df_telemetria['sobrecalentamiento'] = (
    (df_telemetria['temp_motor_izq'] > 55) | 
    (df_telemetria['temp_motor_der'] > 55)
)

df_telemetria['bateria_baja'] = df_telemetria['bateria'] < 20

# Resumen de eventos
eventos = {
    'Sobrecalentamientos': df_telemetria['sobrecalentamiento'].sum(),
    'Alertas batería baja': df_telemetria['bateria_baja'].sum(),
    'Tiempo de operación (s)': len(df_telemetria) * 0.1,
    'Velocidad promedio (m/s)': df_telemetria['velocidad'].mean(),
    'Consumo promedio (A)': df_telemetria['corriente_total'].mean()
}

df_eventos = pd.Series(eventos)
print("\nResumen de misión:")
print(df_eventos)

# Análisis por intervalos de batería
df_telemetria['nivel_bateria'] = pd.cut(
    df_telemetria['bateria'],
    bins=[0, 20, 40, 60, 80, 100],
    labels=['Crítico', 'Bajo', 'Medio', 'Alto', 'Máximo']
)

analisis_bateria = df_telemetria.groupby('nivel_bateria').agg({
    'velocidad': 'mean',
    'corriente_total': 'mean',
    'temp_motor_izq': 'mean'
})

print("\nRendimiento por nivel de batería:")
print(analisis_bateria)
