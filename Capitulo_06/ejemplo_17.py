# analizador_logs.py

def procesar_log(linea):
    partes = linea.split()
    return {
        'fecha': partes[0],
        'hora': partes[1],
        'nivel': partes[2].strip('[]'),
        'mensaje': ' '.join(partes[3:])
    }

def analizar_logs(logs):
    # Procesar líneas
    entradas = [procesar_log(l) for l in logs]
    
    # Contar por nivel usando list comprehensions
    errores = [e for e in entradas if e['nivel'] == 'ERROR']
    warnings = [e for e in entradas if e['nivel'] == 'WARNING']
    
    print(f"Total de logs: {len(entradas)}")
    print(f"Errores: {len(errores)}")
    print(f"Advertencias: {len(warnings)}")

# Ejemplo
logs = [
    "2025-01-04 10:23:45 [INFO] Sistema iniciado",
    "2025-01-04 10:24:12 [ERROR] Conexión fallida",
    "2025-01-04 10:25:33 [WARNING] Memoria al 85%"
]
analizar_logs(logs)
