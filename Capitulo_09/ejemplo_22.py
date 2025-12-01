# control_robot.py
import math

def calcular_trayectoria(x_actual, y_actual, x_objetivo, y_objetivo):
    """Calcula distancia y ángulo para llegar al objetivo"""
    distancia = math.sqrt((x_objetivo - x_actual)**2 + 
                         (y_objetivo - y_actual)**2)
    angulo_rad = math.atan2(y_objetivo - y_actual, 
                            x_objetivo - x_actual)
    angulo_grados = angulo_rad * 180 / math.pi
    return distancia, angulo_grados

def ajustar_velocidad(velocidad_actual, velocidad_objetivo):
    """Ajusta velocidad gradualmente"""
    diferencia = velocidad_objetivo - velocidad_actual
    if abs(diferencia) < 0.1:
        return velocidad_objetivo
    return velocidad_actual + (diferencia * 0.1)

# Uso
distancia, angulo = calcular_trayectoria(0, 0, 10, 5)
print(f"Mover {distancia:.2f}m a ángulo {angulo:.1f}°")

velocidad = ajustar_velocidad(0, 2.5)
print(f"Velocidad ajustada: {velocidad:.2f} m/s")