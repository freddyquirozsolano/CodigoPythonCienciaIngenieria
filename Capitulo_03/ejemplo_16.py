# Simulación de línea de log
log_line = "2025-11-03 14:23:45 [ERROR] Database connection failed - timeout after 30s"

# Parsear la línea de log
partes = log_line.split(None, 3)  # Dividir en máximo 4 partes
fecha = partes[0]
hora = partes[1]
nivel = partes[2].strip("[]")
mensaje = partes[3]

# Extraer información específica
if "timeout" in mensaje.lower():
    # Buscar el número de segundos
    pos_after = mensaje.find("after")
    if pos_after != -1:
        resto = mensaje[pos_after:].split()[1]  # "30s"
        segundos = resto.rstrip("s")
        print(f"Timeout detectado: {segundos} segundos")

# Crear resumen
resumen = f"[{nivel}] {fecha} {hora}: {mensaje[:50]}..."
print(resumen)

# Contar errores por tipo
errores_db = log_line.lower().count("database")
errores_conexion = log_line.lower().count("connection")
print(f"Errores de base de datos: {errores_db}")
print(f"Errores de conexión: {errores_conexion}")