# API REST con Flask
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Base de datos simulada
sensores = [
    {"id": 1, "nombre": "Temperatura", "valor": 25.5, "unidad": "°C"},
    {"id": 2, "nombre": "Humedad", "valor": 60, "unidad": "%"},
    {"id": 3, "nombre": "Presión", "valor": 1013, "unidad": "hPa"}
]

@app.route('/')
def home():
    """Endpoint principal"""
    return jsonify({
        "mensaje": "API de Sensores IoT",
        "version": "1.0",
        "endpoints": ["/sensores", "/sensor/<id>", "/actualizar"]
    })

@app.route('/sensores', methods=['GET'])
def obtener_sensores():
    """Obtener todos los sensores"""
    return jsonify(sensores)

@app.route('/sensor/<int:sensor_id>', methods=['GET'])
def obtener_sensor(sensor_id):
    """Obtener un sensor específico"""
    sensor = next((s for s in sensores if s['id'] == sensor_id), None)
    if sensor:
        return jsonify(sensor)
    return jsonify({"error": "Sensor no encontrado"}), 404

@app.route('/actualizar', methods=['POST'])
def actualizar_sensor():
    """Actualizar valor de sensor"""
    data = request.json
    sensor_id = data.get('id')
    nuevo_valor = data.get('valor')
    
    sensor = next((s for s in sensores if s['id'] == sensor_id), None)
    if sensor:
        sensor['valor'] = nuevo_valor
        sensor['timestamp'] = datetime.now().isoformat()
        return jsonify({"mensaje": "Sensor actualizado", "sensor": sensor})
    
    return jsonify({"error": "Sensor no encontrado"}), 404

if __name__ == '__main__':
    print("Servidor Flask iniciado en http://localhost:5000")
    app.run(debug=True, port=5000)