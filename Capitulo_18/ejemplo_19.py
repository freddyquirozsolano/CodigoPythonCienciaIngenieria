"""
Sistema de Control de Robot Autónomo con Visión Artificial
Integra: pySerial, OpenCV, numpy
"""

import cv2
import serial
import numpy as np
import time

class RobotVision:
    def __init__(self, puerto_serial='COM3'):
        # Configurar comunicación con Arduino
        self.arduino = serial.Serial(puerto_serial, 9600, timeout=1)
        time.sleep(2)
        
        # Configurar cámara
        self.cap = cv2.VideoCapture(0)
        
        # Parámetros de detección de color (HSV)
        # Rojo para seguir objeto rojo
        self.lower_red = np.array([0, 100, 100])
        self.upper_red = np.array([10, 255, 255])
        
        print("Sistema de visión del robot inicializado")
    
    def detectar_objeto(self, frame):
        """Detectar objeto de color específico"""
        # Convertir a HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Crear máscara
        mask = cv2.inRange(hsv, self.lower_red, self.upper_red)
        
        # Encontrar contornos
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, 
                                       cv2.CHAIN_APPROX_SIMPLE)
        
        if contours:
            # Encontrar el contorno más grande
            c = max(contours, key=cv2.contourArea)
            
            # Obtener centro del objeto
            M = cv2.moments(c)
            if M["m00"] > 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                return (cx, cy), cv2.contourArea(c)
        
        return None, 0
    
    def controlar_robot(self, posicion_objeto, area):
        """Enviar comandos al robot según posición del objeto"""
        if posicion_objeto is None:
            # No hay objeto: buscar girando
            self.enviar_comando("SEARCH")
            return "Buscando objeto..."
        
        cx, cy = posicion_objeto
        frame_width = 640
        centro = frame_width // 2
        
        # Definir zona muerta
        tolerancia = 50
        
        if area < 1000:
            # Objeto lejos: avanzar
            self.enviar_comando("FORWARD")
            return "Avanzando hacia objeto"
        elif area > 5000:
            # Objeto muy cerca: retroceder
            self.enviar_comando("BACKWARD")
            return "Retrocediendo"
        elif cx < centro - tolerancia:
            # Objeto a la izquierda: girar izquierda
            self.enviar_comando("LEFT")
            return "Girando izquierda"
        elif cx > centro + tolerancia:
            # Objeto a la derecha: girar derecha
            self.enviar_comando("RIGHT")
            return "Girando derecha"
        else:
            # Objeto centrado y a buena distancia: detener
            self.enviar_comando("STOP")
            return "Objeto alcanzado"
    
    def enviar_comando(self, comando):
        """Enviar comando al Arduino"""
        self.arduino.write(f"{comando}\n".encode())
    
    def ejecutar(self):
        """Loop principal del sistema"""
        print("Sistema activo. Presiona 'q' para salir.")
        
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            
            # Detectar objeto
            posicion, area = self.detectar_objeto(frame)
            
            # Controlar robot
            estado = self.controlar_robot(posicion, area)
            
            # Visualización
            if posicion:
                cv2.circle(frame, posicion, 10, (0, 255, 0), -1)
                cv2.putText(frame, f"Area: {area:.0f}", (10, 30),
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            cv2.putText(frame, estado, (10, 70),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
            
            cv2.imshow('Robot Vision', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        self.cleanup()
    
    def cleanup(self):
        """Liberar recursos"""
        self.enviar_comando("STOP")
        self.cap.release()
        self.arduino.close()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    robot = RobotVision()
    robot.ejecutar()
"""