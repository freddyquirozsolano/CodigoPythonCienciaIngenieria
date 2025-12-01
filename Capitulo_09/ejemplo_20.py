# ingenieria.py - Biblioteca de funciones de ingeniería

import math

def calcular_fuerza(masa, aceleracion=9.8):
    """
    Calcula fuerza según F = m × a.
    
    Args:
        masa (float): Masa en kilogramos
        aceleracion (float): Aceleración en m/s² (default: gravedad)
    
    Returns:
        float: Fuerza en Newtons
    """
    return masa * aceleracion

def calcular_presion(fuerza, area):
    """
    Calcula presión según P = F / A.
    
    Args:
        fuerza (float): Fuerza en Newtons
        area (float): Área en m²
    
    Returns:
        float: Presión en Pascales
    """
    return fuerza / area

def convertir_presion(presion_pa, unidad='psi'):
    """
    Convierte presión de Pascales a otras unidades.
    
    Args:
        presion_pa (float): Presión en Pascales
        unidad (str): Unidad destino ('psi', 'bar', 'atm')
    
    Returns:
        float: Presión en la unidad especificada
    """
    conversiones = {
        'psi': 0.000145038,
        'bar': 0.00001,
        'atm': 0.00000986923
    }
    return presion_pa * conversiones.get(unidad, 1)

def calcular_volumen_cilindro(radio, altura):
    """
    Calcula volumen de un cilindro.
    
    Args:
        radio (float): Radio de la base en metros
        altura (float): Altura del cilindro en metros
    
    Returns:
        float: Volumen en m³
    """
    return math.pi * (radio ** 2) * altura

def calcular_densidad(masa, volumen):
    """
    Calcula densidad según ρ = m / V.
    
    Args:
        masa (float): Masa en kilogramos
        volumen (float): Volumen en m³
    
    Returns:
        float: Densidad en kg/m³
    """
    return masa / volumen

# Ejemplo de uso
if __name__ == "__main__":
    masa = 50
    fuerza = calcular_fuerza(masa)
    print(f"Peso de {masa}kg: {fuerza:.2f} N")
    
    radio, altura = 0.5, 2.0
    volumen = calcular_volumen_cilindro(radio, altura)
    print(f"Volumen del cilindro: {volumen:.4f} m³")