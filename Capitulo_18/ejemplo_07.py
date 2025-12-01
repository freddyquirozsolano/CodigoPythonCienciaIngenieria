# Comunicación con Arduino usando pySerial
import serial
import time

# Configurar puerto serial (ajustar COM# o /dev/tty...)
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)
time.sleep(2)  # Esperar inicialización

def enviar_comando(comando):
    """Enviar comando al Arduino"""
    arduino.write(comando.encode())
    print(f"Comando enviado: {comando}")
    
def leer_sensor():
    """Leer datos del sensor"""
    if arduino.in_waiting > 0:
        linea = arduino.readline().decode('utf-8').strip()
        return linea
    return None

# Control de LED
print("Control de LED Arduino")
enviar_comando("LED_ON\n")
time.sleep(2)
enviar_comando("LED_OFF\n")

# Leer sensor de distancia ultrasónico
print("\nLeyendo sensor ultrasónico...")
enviar_comando("READ_DISTANCE\n")
time.sleep(0.5)

distancia = leer_sensor()
if distancia:
    print(f"Distancia medida: {distancia} cm")

# Control de servo motor
angulo = 90
enviar_comando(f"SERVO:{angulo}\n")
print(f"Servo movido a {angulo}°")

# Cerrar conexión
arduino.close()