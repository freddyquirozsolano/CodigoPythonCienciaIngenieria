"""
Sistema de Monitoreo de Signos Vitales
Integra: pySerial, Flask, numpy, matplotlib
"""

import serial
import numpy as np
from flask import Flask, jsonify, render_template
from datetime import datetime
import threading
import time

app = Flask(__name__)

# Datos del sistema
datos_vitales = {
    'frecuencia_cardiaca': [],
    'temperatura': [],
    'saturacion_o2': [],
    'timestamps': []
}

# Límites normales
LIMITES = {
    'fc_min': 60, 'fc_max': 100,
    'temp_min': 36.0, 'temp_max': 37.5,
    'o2_min': 95
}

def leer_arduino():
    """Thread para leer datos del Arduino"""
    arduino = serial.Serial('COM3', 9600, timeout=1)
    time.sleep(2)
    
    while True:
        if arduino.in_waiting:
            linea = arduino.readline().decode().strip()
            # Formato: "FC:75,TEMP:36.8,O2:98"
            try:
                datos = dict(item.split(':') for item in linea.split(','))
                agregar_lectura(
                    float(datos['FC']),
                    float(datos['TEMP']),
                    int(datos['O2'])
                )
            except:
                pass
        time.sleep(1)

def agregar_lectura(fc, temp, o2):
    """Agregar nueva lectura al historial"""
    datos_vitales['frecuencia_cardiaca'].append(fc)
    datos_vitales['temperatura'].append(temp)
    datos_vitales['saturacion_o2'].append(o2)
    datos_vitales['timestamps'].append(datetime.now())
    
    # Mantener solo últimas 100 lecturas
    for key in ['frecuencia_cardiaca', 'temperatura', 'saturacion_o2', 'timestamps']:
        if len(datos_vitales[key]) > 100:
            datos_vitales[key].pop(0)
    
    # Verificar alertas
    verificar_alertas(fc, temp, o2)

def verificar_alertas(fc, temp, o2):
    """Detectar valores anormales"""
    alertas = []
    
    if fc < LIMITES['fc_min'] or fc > LIMITES['fc_max']:
        alertas.append(f"⚠️ FC anormal: {fc} bpm")
    
    if temp < LIMITES['temp_min'] or temp > LIMITES['temp_max']:
        alertas.append(f"⚠️ Temperatura anormal: {temp}°C")
    
    if o2 < LIMITES['o2_min']:
        alertas.append(f"⚠️ Saturación O2 baja: {o2}%")
    
    if alertas:
        for alerta in alertas:
            print(f"{datetime.now()}: {alerta}")

@app.route('/')
def index():
    return "Sistema de Monitoreo - API activa"

@app.route('/vitales')
def obtener_vitales():
    """Endpoint para obtener datos actuales"""
    if not datos_vitales['frecuencia_cardiaca']:
        return jsonify({"error": "No hay datos disponibles"})
    
    return jsonify({
        'actual': {
            'fc': datos_vitales['frecuencia_cardiaca'][-1],
            'temp': datos_vitales['temperatura'][-1],
            'o2': datos_vitales['saturacion_o2'][-1]
        },
        'promedios': {
            'fc': np.mean(datos_vitales['frecuencia_cardiaca']),
            'temp': np.mean(datos_vitales['temperatura']),
            'o2': np.mean(datos_vitales['saturacion_o2'])
        },
        'total_lecturas': len(datos_vitales['frecuencia_cardiaca'])
    })

if __name__ == '__main__':
    # Iniciar thread de lectura Arduino
    thread_arduino = threading.Thread(target=leer_arduino, daemon=True)
    thread_arduino.start()
    
    print("Sistema de Monitoreo iniciado")
    app.run(debug=True, port=5000)
"""