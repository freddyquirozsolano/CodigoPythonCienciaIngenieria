# Control de robot con módulos estándar
import math
import random
import time

def calcular_trayectoria(x_actual, y_actual, x_objetivo, y_objetivo):
    """Calcula distancia y ángulo para navegación"""
    dx = x_objetivo - x_actual
    dy = y_objetivo - y_actual
    
    distancia = math.sqrt(dx**2 + dy**2)
    angulo_rad = math.atan2(dy, dx)
    angulo_grados = math.degrees(angulo_rad)
    
    return distancia, angulo_grados

# Simular sensor con ruido aleatorio
def leer_sensor_distancia():
    """Simula lectura de sensor ultrasónico"""
    distancia_real = 50  # cm
    ruido = random.uniform(-2, 2)  # ±2 cm de error
    return distancia_real + ruido

# Navegación
posicion_actual = (0, 0)
objetivo = (10, 5)

distancia, angulo = calcular_trayectoria(*posicion_actual, *objetivo)
print(f"Mover {distancia:.2f}m a {angulo:.1f}°")

# Simular lecturas de sensor
print("\nLecturas de sensor:")
for i in range(5):
    lectura = leer_sensor_distancia()
    print(f"  Lectura {i+1}: {lectura:.2f} cm")
    time.sleep(0.5)  # Esperar 0.5 segundos