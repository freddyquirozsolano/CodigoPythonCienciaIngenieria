# Archivo: mecatronica.py
"""
Módulo de funciones para mecatrónica y robótica.
Incluye conversiones, cinemática y control.
"""

import math

# Constantes
PI = math.pi
GRAVEDAD = 9.81  # m/s²

def grados_a_radianes(grados):
    """Convierte ángulos de grados a radianes."""
    return grados * PI / 180

def radianes_a_grados(radianes):
    """Convierte ángulos de radianes a grados."""
    return radianes * 180 / PI

def rpm_a_rad_s(rpm):
    """Convierte RPM a rad/s."""
    return (rpm * 2 * PI) / 60

def rad_s_a_rpm(rad_s):
    """Convierte rad/s a RPM."""
    return (rad_s * 60) / (2 * PI)

def calcular_torque(fuerza, distancia):
    """Calcula torque: T = F × d"""
    return fuerza * distancia

def calcular_potencia(torque, velocidad_angular):
    """Calcula potencia: P = T × ω"""
    return torque * velocidad_angular

def cinematica_directa_2r(l1, l2, theta1, theta2):
    """
    Cinemática directa de robot de 2 eslabones.
    
    Args:
        l1, l2: Longitudes de eslabones
        theta1, theta2: Ángulos en grados
    
    Returns:
        tuple: Coordenadas (x, y) del efector final
    """
    t1_rad = grados_a_radianes(theta1)
    t2_rad = grados_a_radianes(theta2)
    
    x = l1 * math.cos(t1_rad) + l2 * math.cos(t1_rad + t2_rad)
    y = l1 * math.sin(t1_rad) + l2 * math.sin(t1_rad + t2_rad)
    
    return x, y

def pid_controller(error, kp=1.0, ki=0.0, kd=0.0, 
                   error_prev=0, integral=0, dt=0.1):
    """
    Controlador PID básico.
    
    Returns:
        tuple: (salida, nueva_integral, error_actual)
    """
    # Proporcional
    p = kp * error
    
    # Integral
    integral += error * dt
    i = ki * integral
    
    # Derivativo
    derivada = (error - error_prev) / dt
    d = kd * derivada
    
    salida = p + i + d
    
    return salida, integral, error

__version__ = "1.0.0"
__author__ = "Tu Nombre"

if __name__ == "__main__":
    print("=== Pruebas del módulo mecatronica ===\n")
    
    # Conversiones
    angulo = 90
    print(f"{angulo}° = {grados_a_radianes(angulo):.4f} rad")
    
    # Cinemática
    x, y = cinematica_directa_2r(1, 1, 45, 45)
    print(f"Posición: ({x:.2f}, {y:.2f})")
    
    # Control PID
    error = 10
    salida, _, _ = pid_controller(error, kp=0.5, ki=0.1, kd=0.01)
    print(f"Señal de control: {salida:.2f}")