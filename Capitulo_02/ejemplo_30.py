# Conversión de unidades de almacenamiento
gb = 16
mb = gb * 1024
kb = mb * 1024
bytes_total = kb * 1024
print(f"{gb} GB = {bytes_total:,} bytes")

# Cálculo de tiempo de transferencia
tamaño_mb = 500
velocidad_mbps = 50
tiempo_segundos = (tamaño_mb * 8) / velocidad_mbps
tiempo_minutos = tiempo_segundos / 60
print(f"Tiempo de descarga: {tiempo_minutos:.2f} minutos")

# Cálculo de direcciones IP disponibles
mascara = 24
hosts_disponibles = (2 ** (32 - mascara)) - 2
print(f"Direcciones IP disponibles: {hosts_disponibles}")