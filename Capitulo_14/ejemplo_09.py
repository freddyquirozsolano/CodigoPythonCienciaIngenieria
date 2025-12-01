import json

# Diccionario de configuración
config_robot = {
    'id': 'ROBOT-001',
    'modelo': 'AutoNav-X',
    'sensores': {
        'ultrasonico': {'rango': 400, 'activo': True},
        'camara': {'resolucion': '1080p', 'fps': 30}
    },
    'motores': {
        'izquierdo': {'velocidad': 0},
        'derecho': {'velocidad': 0}
    },
    'bateria': 100
}

# Guardar en archivo JSON con formato legible
with open('robot_config.json', 'w', encoding='utf-8') as archivo:
    json.dump(config_robot, archivo, 
              indent=4,           # Identación de 4 espacios
              ensure_ascii=False) # Permite caracteres UTF-8
