import json

# Datos estructurados
configuracion_robot = {
    "nombre": "RoboCar-01",
    "velocidad_maxima": 5.0,
    "sensores": ["ultrasonido", "infrarrojo", "camara"],
    "motores": {
        "izquierdo": {"rpm_max": 200, "voltaje": 12},
        "derecho": {"rpm_max": 200, "voltaje": 12}
    },
    "activo": True
}

# Guardar en JSON
with open("config_robot.json", "w") as archivo:
    json.dump(configuracion_robot, archivo, indent=4)

# Leer desde JSON
with open("config_robot.json", "r") as archivo:
    config = json.load(archivo)
    
print(f"Robot: {config['nombre']}")
print(f"Velocidad máxima: {config['velocidad_maxima']} m/s")
print(f"Sensores: {', '.join(config['sensores'])}")
print(f"RPM motor izquierdo: {config['motores']['izquierdo']['rpm_max']}")