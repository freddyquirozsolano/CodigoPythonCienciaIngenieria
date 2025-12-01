# biomedicas.py - Biblioteca de funciones biomédicas

def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal.
    
    Args:
        peso (float): Peso en kilogramos
        altura (float): Altura en metros
    
    Returns:
        float: IMC calculado
    """
    return peso / (altura ** 2)

def clasificar_imc(imc):
    """
    Clasifica el IMC según estándares OMS.
    
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

def calcular_frecuencia_cardiaca_maxima(edad):
    """
    Calcula la frecuencia cardíaca máxima teórica.
    
    Args:
        edad (int): Edad en años
    
    Returns:
        int: Frecuencia cardíaca máxima en bpm
    """
    return 220 - edad

def calcular_zona_entrenamiento(fcm, intensidad=0.7):
    """
    Calcula la zona de entrenamiento cardíaco.
    
    Args:
        fcm (int): Frecuencia cardíaca máxima
        intensidad (float): Porcentaje de intensidad (0.6-0.9)
    
    Returns:
        tuple: (fc_minima, fc_maxima) para la zona
    """
    fc_min = int(fcm * (intensidad - 0.1))
    fc_max = int(fcm * intensidad)
    return fc_min, fc_max

def convertir_presion_arterial(sistolica, diastolica, a_kpa=False):
    """
    Convierte presión arterial entre mmHg y kPa.
    
    Args:
        sistolica (float): Presión sistólica en mmHg
        diastolica (float): Presión diastólica en mmHg
        a_kpa (bool): Si True, convierte a kPa
    
    Returns:
        tuple: (sistolica, diastolica) en la unidad especificada
    """
    if a_kpa:
        return sistolica * 0.133322, diastolica * 0.133322
    return sistolica, diastolica

# Ejemplo de uso
if __name__ == "__main__":
    peso, altura = 70, 1.75
    imc = calcular_imc(peso, altura)
    clasificacion = clasificar_imc(imc)
    print(f"IMC: {imc:.2f} - {clasificacion}")
    
    edad = 30
    fcm = calcular_frecuencia_cardiaca_maxima(edad)
    zona = calcular_zona_entrenamiento(fcm, 0.7)
    print(f"Zona de entrenamiento: {zona[0]}-{zona[1]} bpm")