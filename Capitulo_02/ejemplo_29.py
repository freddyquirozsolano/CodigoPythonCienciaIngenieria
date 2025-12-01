# Conversión de pulsos a grados
pulsos_encoder = 1440
pulsos_por_revolucion = 360
revoluciones = pulsos_encoder / pulsos_por_revolucion
grados = revoluciones * 360
print(f"Ángulo: {grados}°")

# Cálculo de velocidad angular
rpm = 120  # revoluciones por minuto
import math
velocidad_angular = (rpm * 2 * math.pi) / 60  # rad/s
print(f"Velocidad angular: {velocidad_angular:.2f} rad/s")

# Cálculo de torque
fuerza = 50  # N
distancia = 0.2  # m
torque = fuerza * distancia
print(f"Torque: {torque} N·m")