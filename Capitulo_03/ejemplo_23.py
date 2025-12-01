import json
from datetime import datetime

# Función para registrar telemetría
def registrar_telemetria(datos_robot):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Agregar al archivo CSV
    with open("telemetria_robot.csv", "a") as archivo:
        linea = f"{timestamp},{datos_robot['velocidad']},{datos_robot['bateria']},"
        linea += f"{datos_robot['temperatura']},{datos_robot['distancia']}\n"
        archivo.write(linea)
    
    # También guardar en JSON para análisis detallado
    datos_completos = {
        "timestamp": timestamp,
        **datos_robot
    }
    
    with open("telemetria_robot.json", "a") as archivo:
        json.dump(datos_completos, archivo)
        archivo.write("\n")

# Registrar datos
datos = {
    "velocidad": 2.5,
    "bateria": 11.8,
    "temperatura": 42.3,
    "distancia": 156.7
}

registrar_telemetria(datos)

# Leer y analizar telemetría
print("=== ANÁLISIS DE TELEMETRÍA ===\n")

velocidades = []
with open("telemetria_robot.csv", "r") as archivo:
    for linea in archivo:
        campos = linea.strip().split(",")
        vel = float(campos[1])
        velocidades.append(vel)

velocidad_promedio = sum(velocidades) / len(velocidades)
velocidad_maxima = max(velocidades)
velocidad_minima = min(velocidades)

print(f"Lecturas totales: {len(velocidades)}")
print(f"Velocidad promedio: {velocidad_promedio:.2f} m/s")
print(f"Velocidad máxima: {velocidad_maxima:.2f} m/s")
print(f"Velocidad mínima: {velocidad_minima:.2f} m/s")