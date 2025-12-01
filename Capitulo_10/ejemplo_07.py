# Archivo: biomedicas.py
"""
Módulo de funciones para ingeniería biomédica.

Este módulo proporciona funciones para cálculos médicos comunes
como IMC, frecuencia cardíaca y clasificaciones clínicas.

Autor: Tu Nombre
Fecha: Fecha de creación
Versión: 1.0
"""

def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal.
    
    Args:
        peso (float): Peso en kilogramos
        altura (float): Altura en metros
    
    Returns:
        float: IMC calculado
    
    Example:
        >>> calcular_imc(70, 1.75)
        22.86
    """
    return peso / (altura ** 2)

def clasificar_imc(imc):
    """
    Clasifica el IMC según estándares de la OMS.
    
    Args:
        imc (float): Valor del IMC
    
    Returns:
        str: Clasificación del IMC
    """
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

def calcular_fcm(edad):
    """
    Calcula la frecuencia cardíaca máxima teórica.
    
    Args:
        edad (int): Edad en años
    
    Returns:
        int: Frecuencia cardíaca máxima en bpm
    """
    return 220 - edad

# Constantes del módulo
VERSION = "1.0"
AUTOR = "Tu Nombre"

# Código que se ejecuta solo cuando el módulo se ejecuta directamente
if __name__ == "__main__":
    print("Probando módulo biomedicas...")
    imc = calcular_imc(70, 1.75)
    print(f"IMC: {imc:.2f}")
    print(f"Clasificación: {clasificar_imc(imc)}")