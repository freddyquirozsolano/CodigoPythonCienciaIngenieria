# Estadísticas del sistema
usuario = "jperez"
tiempo_sesion = 3.75  # horas
archivos_procesados = 1247
datos_transferidos = 3.456e9  # bytes
cpu_promedio = 45.8  # porcentaje
memoria_usada = 6.2  # GB
memoria_total = 16.0  # GB

# Conversiones
datos_gb = datos_transferidos / (1024**3)
memoria_porcentaje = (memoria_usada / memoria_total) * 100
archivos_por_hora = archivos_procesados / tiempo_sesion

# Reporte del sistema
print("+" + "-" * 58 + "+")
print(f"|{'REPORTE DE ACTIVIDAD DEL SISTEMA':^58}|")
print("+" + "-" * 58 + "+")
print(f"| Usuario: {usuario:<48}|")
print(f"| Tiempo de sesión: {tiempo_sesion:>5.2f} horas                       |")
print("+" + "-" * 58 + "+")
print(f"| {'PROCESAMIENTO':^58} |")
print(f"|   Archivos procesados:  {archivos_procesados:>10,}                 |")
print(f"|   Tasa de procesamiento: {archivos_por_hora:>8.1f} archivos/hora  |")
print(f"|   Datos transferidos:    {datos_gb:>9.2f} GB               |")
print("+" + "-" * 58 + "+")
print(f"| {'RECURSOS':^58} |")
print(f"|   CPU promedio:          {cpu_promedio:>6.1f}%                   |")
print(f"|   Memoria utilizada:     {memoria_usada:>6.2f} GB de {memoria_total:>5.1f} GB |")
print(f"|   Memoria porcentaje:    {memoria_porcentaje:>6.1f}%                   |")
print("+" + "-" * 58 + "+")