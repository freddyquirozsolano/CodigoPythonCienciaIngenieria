# Estado del robot
import math

nombre_robot = "RoboCar-01"
velocidad_actual = 2.345  # m/s
angulo_direccion = 45.7   # grados
voltaje_bateria = 11.87   # V
corriente = 3.45          # A
temperatura_motor = 42.3  # °C
distancia_recorrida = 15678.9  # metros
rpm_motor = 1234

# Cálculos
potencia = voltaje_bateria * corriente
porcentaje_bateria = (voltaje_bateria / 12.6) * 100
angulo_rad = math.radians(angulo_direccion)

# Dashboard formateado
print("╔" + "═" * 58 + "╗")
print(f"║{'DASHBOARD DEL ROBOT':^58}║")
print("╠" + "═" * 58 + "╣")
print(f"║ Robot: {nombre_robot:<47}║")
print("╠" + "═" * 58 + "╣")
print(f"║ {'MOVIMIENTO':^58} ║")
print(f"║   Velocidad:      {velocidad_actual:>7.2f} m/s   ({rpm_motor:>5} RPM)  ║")
print(f"║   Dirección:      {angulo_direccion:>7.1f}° ({angulo_rad:>7.4f} rad)  ║")
print(f"║   Distancia:      {distancia_recorrida:>10,.1f} m                ║")
print("╠" + "═" * 58 + "╣")
print(f"║ {'ENERGÍA':^58} ║")
print(f"║   Batería:        {voltaje_bateria:>6.2f} V ({porcentaje_bateria:>5.1f}%)      ║")
print(f"║   Corriente:      {corriente:>6.2f} A                       ║")
print(f"║   Potencia:       {potencia:>6.2f} W                       ║")
print("╠" + "═" * 58 + "╣")
print(f"║ {'TEMPERATURA':^58} ║")
print(f"║   Motor:          {temperatura_motor:>6.1f}°C                      ║")
print("╚" + "═" * 58 + "╝")