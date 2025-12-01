# Archivo: biomedicas.py - Versión completa
"""
Módulo de funciones para ingeniería biomédica.
Incluye cálculos de signos vitales, dosificación y análisis clínico.
"""

import math

# Constantes
IMC_BAJO = 18.5
IMC_NORMAL = 25
IMC_SOBREPESO = 30

def calcular_imc(peso, altura):
    """Calcula el Índice de Masa Corporal."""
    if peso <= 0 or altura <= 0:
        raise ValueError("Peso y altura deben ser positivos")
    return peso / (altura ** 2)

def clasificar_imc(imc):
    """Clasifica el IMC según OMS."""
    if imc < IMC_BAJO:
        return "Bajo peso"
    elif imc < IMC_NORMAL:
        return "Peso normal"
    elif imc < IMC_SOBREPESO:
        return "Sobrepeso"
    else:
        return "Obesidad"

def calcular_fcm(edad):
    """Calcula frecuencia cardíaca máxima teórica."""
    if edad <= 0 or edad > 120:
        raise ValueError("Edad debe estar entre 1 y 120")
    return 220 - edad

def calcular_zona_entrenamiento(fcm, intensidad=0.7):
    """
    Calcula zona de entrenamiento cardíaco.
    
    Args:
        fcm: Frecuencia cardíaca máxima
        intensidad: Nivel de intensidad (0.6-0.9)
    
    Returns:
        tuple: (fc_minima, fc_maxima)
    """
    if not 0.6 <= intensidad <= 0.9:
        raise ValueError("Intensidad debe estar entre 0.6 y 0.9")
    
    fc_min = int(fcm * (intensidad - 0.1))
    fc_max = int(fcm * intensidad)
    return fc_min, fc_max

def calcular_dosis(peso, mg_por_kg):
    """Calcula dosis de medicamento según peso."""
    if peso <= 0:
        raise ValueError("Peso debe ser positivo")
    if mg_por_kg <= 0:
        raise ValueError("Dosis debe ser positiva")
    return peso * mg_por_kg

def calcular_superficie_corporal(peso, altura):
    """
    Calcula superficie corporal usando fórmula de Mosteller.
    BSA = sqrt((altura_cm * peso_kg) / 3600)
    """
    altura_cm = altura * 100
    return math.sqrt((altura_cm * peso) / 3600)

def clasificar_presion(sistolica, diastolica):
    """Clasifica presión arterial según AHA."""
    if sistolica < 120 and diastolica < 80:
        return "Normal"
    elif sistolica < 130 and diastolica < 80:
        return "Elevada"
    elif sistolica < 140 or diastolica < 90:
        return "Hipertensión Etapa 1"
    elif sistolica >= 140 or diastolica >= 90:
        return "Hipertensión Etapa 2"
    elif sistolica >= 180 or diastolica >= 120:
        return "Crisis Hipertensiva"
    return "Revisar valores"

# Información del módulo
__version__ = "1.0.0"
__author__ = "Tu Nombre"
__all__ = ['calcular_imc', 'clasificar_imc', 'calcular_fcm',
           'calcular_zona_entrenamiento', 'calcular_dosis',
           'calcular_superficie_corporal', 'clasificar_presion']

if __name__ == "__main__":
    # Pruebas del módulo
    print("=== Pruebas del módulo biomedicas ===\n")
    
    # Prueba IMC
    peso, altura = 70, 1.75
    imc = calcular_imc(peso, altura)
    print(f"IMC: {imc:.2f} - {clasificar_imc(imc)}")
    
    # Prueba FCM
    edad = 30
    fcm = calcular_fcm(edad)
    zona = calcular_zona_entrenamiento(fcm)
    print(f"FCM: {fcm} bpm, Zona: {zona[0]}-{zona[1]} bpm")
    
    # Prueba presión
    clasificacion = clasificar_presion(125, 82)
    print(f"Presión 125/82: {clasificacion}")
    
    print(f"\nMódulo versión {__version__}")