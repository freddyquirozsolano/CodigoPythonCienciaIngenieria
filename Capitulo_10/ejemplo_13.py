# Archivo: ingenieria/biomedica/signos_vitales.py
"""Módulo de análisis de signos vitales"""

def calcular_imc(peso, altura):
    """Calcula IMC"""
    return peso / (altura ** 2)

def clasificar_imc(imc):
    """Clasifica IMC"""
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

def calcular_fcm(edad):
    """Calcula frecuencia cardíaca máxima"""
    return 220 - edad