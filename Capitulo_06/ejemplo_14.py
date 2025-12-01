# Sistema de análisis de logs
logs = [
    "2025-01-15 10:23:45 INFO Usuario login exitoso",
    "2025-01-15 10:24:12 ERROR Conexión a DB falló",
    "2025-01-15 10:25:33 WARNING Memoria al 85%",
    "2025-01-15 10:26:01 ERROR Timeout en API",
    "2025-01-15 10:27:15 INFO Backup completado"
]

# Filtrar solo errores
errores = [log for log in logs if 'ERROR' in log]

# Extraer niveles de log
niveles = [log.split()[2] for log in logs]

# Contar errores
num_errores = niveles.count('ERROR')

print(f"Total de logs: {len(logs)}")
print(f"Errores encontrados: {num_errores}")
