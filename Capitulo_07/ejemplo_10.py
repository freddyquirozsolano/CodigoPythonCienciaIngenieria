# Configuración de robot autónomo
robot_config = {
    'id': 'ROBOT-001',
    'modelo': 'AutoNav-X',
    'sensores': {
        'ultrasonico': {'rango': 400, 'activo': True},
        'infrarrojo': {'rango': 100, 'activo': True},
        'camara': {'resolucion': '1080p', 'fps': 30, 'activo': True}
    },
    'motores': {
        'izquierdo': {'velocidad': 0, 'direccion': 'adelante'},
        'derecho': {'velocidad': 0, 'direccion': 'adelante'}
    },
    'posicion': {'x': 0, 'y': 0, 'theta': 0},
    'bateria': 100
}

# Actualizar velocidad de motores
robot_config['motores']['izquierdo']['velocidad'] = 150
robot_config['motores']['derecho']['velocidad'] = 150

# Verificar sensores activos
sensores_activos = {s for s, config in robot_config['sensores'].items() 
                    if config['activo']}
print(f"Sensores activos: {sensores_activos}")
