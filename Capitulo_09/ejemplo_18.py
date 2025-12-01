# mecatronica.py - Biblioteca de funciones de mecatrónica

import math

def grados_a_radianes(grados):
    """Convierte ángulos de grados a radianes."""
    return grados * math.pi / 180

def radianes_a_grados(radianes):
    """Convierte ángulos de radianes a grados."""
    return radianes * 180 / math.pi

def rpm_a_rad_por_seg(rpm):
    """
    Convierte velocidad de RPM a rad/s.
    
    Args:
        rpm (float): Revoluciones por minuto
    
    Returns:
        float: Velocidad angular en rad/s
    """
    return (rpm * 2 * math.pi) / 60

def calcular_torque(fuerza, distancia):
    """
    Calcula el torque aplicado.
    
    Args:
        fuerza (float): Fuerza en Newtons
        distancia (float): Distancia al centro en metros
    
    Returns:
        float: Torque en N·m
    """
    return fuerza * distancia

def calcular_distancia_recorrida(velocidad, tiempo, aceleracion=0):
    """
    Calcula distancia recorrida con aceleración constante.
    
    Args:
        velocidad (float): Velocidad inicial en m/s
        tiempo (float): Tiempo en segundos
        aceleracion (float): Aceleración en m/s²
    
    Returns:
        float: Distancia recorrida en metros
    """
    return velocidad * tiempo + 0.5 * aceleracion * (tiempo ** 2)

def pid_basico(error, kp=1.0, ki=0.0, kd=0.0):
    """
    Implementación básica de controlador PID.
    
    Args:
        error (float): Error actual (setpoint - medición)
        kp (float): Ganancia proporcional
        ki (float): Ganancia integral
        kd (float): Ganancia derivativa
    
    Returns:
        float: Señal de control PID
    """
    return kp * error + ki * error + kd * error

# Ejemplo de uso
if __name__ == "__main__":
    angulo_grados = 90
    angulo_rad = grados_a_radianes(angulo_grados)
    print(f"{angulo_grados}° = {angulo_rad:.4f} rad")
    
    control = pid_basico(20, kp=0.5)
    print(f"Señal de control: {control:.2f}")