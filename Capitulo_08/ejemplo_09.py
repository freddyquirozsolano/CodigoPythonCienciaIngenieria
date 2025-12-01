# Sistema de comandos para robot
import re

def parsear_comando(comando):
    comando = comando.strip().upper()
    
    # MOVE(x, y, velocidad)
    if comando.startswith('MOVE'):
        match = re.search(r'MOVE\(([\d\.]+),\s*([\d\.]+),\s*([\d\.]+)\)', comando)
        if match:
            x, y, vel = match.groups()
            return {'accion': 'mover', 'x': float(x), 'y': float(y), 'velocidad': float(vel)}
    
    # ROTATE(angulo)
    elif comando.startswith('ROTATE'):
        match = re.search(r'ROTATE\(([\d\.]+)\)', comando)
        if match:
            angulo = match.group(1)
            return {'accion': 'rotar', 'angulo': float(angulo)}
    
    # STOP
    elif comando == 'STOP':
        return {'accion': 'detener'}
    
    return {'accion': 'desconocido', 'comando': comando}

# Probar comandos
comandos = [
    "MOVE(10.5, 20.3, 1.5)",
    "ROTATE(90)",
    "STOP"
]

for cmd in comandos:
    resultado = parsear_comando(cmd)
    print(f"Comando: {cmd} -> {resultado}")
