# biomedica/signos_vitales.py
"""Módulo de signos vitales"""

def calcular_imc(peso, altura):
    """Calcula IMC"""
    return peso / (altura ** 2)

def clasificar_imc(imc):
    """Clasifica IMC según OMS"""
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    return "Obesidad"

def calcular_fcm(edad):
    """Frecuencia cardíaca máxima"""
    return 220 - edad

# biomedica/analisis.py
"""Módulo de análisis estadístico"""
import statistics

def analizar_temperaturas(temperaturas):
    """Analiza serie de temperaturas"""
    return {
        'promedio': statistics.mean(temperaturas),
        'minima': min(temperaturas),
        'maxima': max(temperaturas),
        'desviacion': statistics.stdev(temperaturas)
    }

def detectar_anomalias(valores, umbral_std=2):
    """Detecta valores anómalos"""
    media = statistics.mean(valores)
    std = statistics.stdev(valores)
    anomalias = []
    
    for i, valor in enumerate(valores):
        if abs(valor - media) > umbral_std * std:
            anomalias.append((i, valor))
    
    return anomalias

# biomedica/reportes.py
"""Módulo de generación de reportes"""
from datetime import datetime

def generar_reporte_paciente(nombre, datos_vitales):
    """Genera reporte de paciente"""
    reporte = []
    reporte.append("=" * 60)
    reporte.append(f"REPORTE MÉDICO - {nombre}")
    reporte.append(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    reporte.append("=" * 60)
    reporte.append("")
    
    for clave, valor in datos_vitales.items():
        reporte.append(f"{clave}: {valor}")
    
    reporte.append("=" * 60)
    return "\n".join(reporte)

# main.py
"""Programa principal"""
from biomedica import signos_vitales, analisis, reportes

def main():
    # Datos del paciente
    paciente = {
        'nombre': 'María López',
        'edad': 45,
        'peso': 70,
        'altura': 1.65
    }
    
    # Análisis
    imc = signos_vitales.calcular_imc(paciente['peso'], paciente['altura'])
    clasificacion = signos_vitales.clasificar_imc(imc)
    fcm = signos_vitales.calcular_fcm(paciente['edad'])
    
    # Temperaturas del día
    temps = [36.5, 37.2, 36.8, 37.0, 36.9, 37.5, 36.7]
    analisis_temps = analisis.analizar_temperaturas(temps)
    
    # Generar reporte
    datos_vitales = {
        'IMC': f"{imc:.2f} ({clasificacion})",
        'FCM teórica': f"{fcm} bpm",
        'Temp. promedio': f"{analisis_temps['promedio']:.2f}°C",
        'Temp. mínima': f"{analisis_temps['minima']}°C",
        'Temp. máxima': f"{analisis_temps['maxima']}°C"
    }
    
    reporte = reportes.generar_reporte_paciente(
        paciente['nombre'], 
        datos_vitales
    )
    
    print(reporte)

if __name__ == "__main__":
    main()