# Sistema de logs con módulos estándar
import datetime
import json
import os

def registrar_evento(tipo, mensaje, archivo='sistema.log'):
    """Registra eventos del sistema en archivo JSON"""
    evento = {
        'timestamp': datetime.datetime.now().isoformat(),
        'tipo': tipo,
        'mensaje': mensaje
    }
    
    # Leer eventos existentes
    eventos = []
    if os.path.exists(archivo):
        with open(archivo, 'r') as f:
            try:
                eventos = json.load(f)
            except:
                eventos = []
    
    # Agregar nuevo evento
    eventos.append(evento)
    
    # Guardar
    with open(archivo, 'w') as f:
        json.dump(eventos, f, indent=2)
    
    print(f"[{tipo}] {mensaje}")

# Uso del sistema de logs
registrar_evento('INFO', 'Sistema iniciado')
registrar_evento('WARNING', 'Memoria al 85%')
registrar_evento('ERROR', 'Conexión a DB falló')
registrar_evento('INFO', 'Sistema detenido')