# robotica/cinematica.py
"""Módulo de cinemática"""
import math

def cinematica_directa(l1, l2, theta1, theta2):
    """Cinemática directa de brazo 2R"""
    t1 = math.radians(theta1)
    t2 = math.radians(theta2)
    
    x = l1 * math.cos(t1) + l2 * math.cos(t1 + t2)
    y = l1 * math.sin(t1) + l2 * math.sin(t1 + t2)
    
    return x, y

def calcular_velocidad(rpm, diametro_rueda):
    """Calcula velocidad lineal del robot"""
    # Convertir RPM a rad/s
    omega = (rpm * 2 * math.pi) / 60
    # Velocidad lineal
    radio = diametro_rueda / 2
    return omega * radio

# robotica/control.py
"""Módulo de control"""

class ControladorPID:
    """Controlador PID"""
    
    def __init__(self, kp=1.0, ki=0.0, kd=0.0):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.integral = 0
        self.error_prev = 0
    
    def calcular(self, error, dt=0.1):
        """Calcula señal de control"""
        # Proporcional
        p = self.kp * error
        
        # Integral
        self.integral += error * dt
        i = self.ki * self.integral
        
        # Derivativo
        derivada = (error - self.error_prev) / dt
        d = self.kd * derivada
        
        self.error_prev = error
        
        return p + i + d

# robotica/sensores.py
"""Módulo de manejo de sensores"""
import random

def leer_sensor_distancia(distancia_real=50, ruido=2):
    """Simula sensor ultrasónico"""
    return distancia_real + random.uniform(-ruido, ruido)

def leer_encoder(posicion_actual, incremento):
    """Simula encoder de motor"""
    return posicion_actual + incremento

# main.py
"""Programa principal del robot"""
from robotica import cinematica, control, sensores
import time

def main():
    print("=== Sistema de Control de Robot ===\n")
    
    # Configuración del robot
    l1, l2 = 1.0, 1.0  # Longitudes de eslabones
    
    # Posición actual y objetivo
    theta1_actual, theta2_actual = 30, 45
    theta1_objetivo, theta2_objetivo = 45, 60
    
    # Calcular posiciones
    x_actual, y_actual = cinematica.cinematica_directa(
        l1, l2, theta1_actual, theta2_actual
    )
    x_objetivo, y_objetivo = cinematica.cinematica_directa(
        l1, l2, theta1_objetivo, theta2_objetivo
    )
    
    print(f"Posición actual: ({x_actual:.2f}, {y_actual:.2f})")
    print(f"Posición objetivo: ({x_objetivo:.2f}, {y_objetivo:.2f})")
    
    # Control PID
    pid = control.ControladorPID(kp=0.5, ki=0.1, kd=0.05)
    
    # Simular control
    print("\nIniciando control...")
    posicion = 0
    objetivo = 100
    
    for i in range(10):
        error = objetivo - posicion
        control_signal = pid.calcular(error)
        posicion += control_signal * 0.1
        
        # Leer sensor
        distancia = sensores.leer_sensor_distancia()
        
        print(f"Iteración {i+1}: Pos={posicion:.2f}, "
              f"Error={error:.2f}, Sensor={distancia:.2f}cm")
        
        time.sleep(0.1)
    
    print("\n✓ Control completado")

if __name__ == "__main__":
    main()