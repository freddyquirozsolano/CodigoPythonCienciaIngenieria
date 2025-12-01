# Instalar paquetes de mecatrónica
pip install numpy scipy
pip install pyserial  # Comunicación serial (Arduino)
pip install opencv-python  # Visión artificial
pip install matplotlib  # Gráficos

# Ejemplo: Comunicación con Arduino
import serial
import time

# Conectar a Arduino
arduino = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)  # Esperar inicialización

# Enviar comando
comando = "MOTOR:150
"
arduino.write(comando.encode())

# Leer respuesta
respuesta = arduino.readline().decode().strip()
print(f"Arduino responde: {respuesta}")

arduino.close()