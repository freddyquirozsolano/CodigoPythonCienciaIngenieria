# Análisis de logs de aplicación web
import pandas as pd
import numpy as np

# Simular logs de servidor
np.random.seed(42)
n_logs = 1000

tipos_request = ['GET', 'POST', 'PUT', 'DELETE']
endpoints = ['/api/users', '/api/products', '/api/orders', '/api/auth']
status_codes = [200, 201, 400, 401, 404, 500, 503]

logs = {
    'timestamp': pd.date_range('2025-01-01', periods=n_logs, freq='1min'),
    'ip': ['192.168.1.' + str(np.random.randint(1, 255)) for _ in range(n_logs)],
    'method': np.random.choice(tipos_request, n_logs, p=[0.6, 0.25, 0.1, 0.05]),
    'endpoint': np.random.choice(endpoints, n_logs),
    'status_code': np.random.choice(status_codes, n_logs, p=[0.7, 0.1, 0.05, 0.02, 0.05, 0.05, 0.03]),
    'response_time': np.random.exponential(200, n_logs),  # milisegundos
    'bytes_sent': np.random.randint(500, 50000, n_logs)
}

df_logs = pd.DataFrame(logs)

# Análisis de tráfico por hora
df_logs['hora'] = df_logs['timestamp'].dt.hour
trafico_hora = df_logs.groupby('hora').size()
print("Requests por hora:")
print(trafico_hora)

# Análisis de códigos de estado
status_analisis = df_logs.groupby('status_code').agg({
    'timestamp': 'count',
    'response_time': 'mean'
}).rename(columns={'timestamp': 'count', 'response_time': 'avg_response_time'})

print("\nAnálisis por código de estado:")
print(status_analisis)

# Endpoints más lentos
endpoints_lentos = df_logs.groupby('endpoint')['response_time'].agg(['mean', 'median', 'max']).sort_values('mean', ascending=False)
print("\nEndpoints más lentos:")
print(endpoints_lentos)

# Detectar IPs sospechosas (alto volumen de errores)
df_logs['es_error'] = df_logs['status_code'] >= 400
ips_problematicas = df_logs[df_logs['es_error']].groupby('ip').size().sort_values(ascending=False).head(10)
print("\nIPs con más errores:")
print(ips_problematicas)

# Análisis temporal de rendimiento
df_logs['fecha'] = df_logs['timestamp'].dt.date
rendimiento_diario = df_logs.groupby('fecha').agg({
    'response_time': ['mean', 'median', 'max'],
    'timestamp': 'count'
}).round(2)

print("\nRendimiento diario:")
print(rendimiento_diario)

# Tasa de errores
tasa_errores = (df_logs['es_error'].sum() / len(df_logs)) * 100
print(f"\nTasa de errores: {tasa_errores:.2f}%")
