import math
from abc import ABC, abstractmethod

class Robot(ABC):
    """Clase abstracta base para robots"""
    
    def __init__(self, id_robot, modelo):
        self.id = id_robot
        self.modelo = modelo
        self.posicion = {'x': 0, 'y': 0, 'theta': 0}
        self.estado = "detenido"
        self._bateria = 100
    
    @property
    def bateria(self):
        return self._bateria
    
    @bateria.setter
    def bateria(self, valor):
        if 0 <= valor <= 100:
            self._bateria = valor
            if valor < 20:
                print(f"⚠️ Batería baja en {self.id}: {valor}%")
        else:
            raise ValueError("Batería debe estar entre 0 y 100")
    
    @abstractmethod
    def moverse(self, distancia):
        """Método abstracto - debe implementarse en subclases"""
        pass
    
    def actualizar_posicion(self, dx, dy):
        """Actualizar posición del robot"""
        self.posicion['x'] += dx
        self.posicion['y'] += dy
    
    def rotar(self, angulo):
        """Rotar el robot (en grados)"""
        self.posicion['theta'] = (self.posicion['theta'] + angulo) % 360
        self.bateria -= 0.5  # Consumo de batería
    
    def __str__(self):
        return f"{self.modelo} (ID: {self.id}) - Batería: {self.bateria}%"
    
    def __repr__(self):
        return f"Robot('{self.id}', '{self.modelo}')"

class RobotMovil(Robot):
    """Robot móvil terrestre"""
    
    def __init__(self, id_robot, modelo, vel_max):
        super().__init__(id_robot, modelo)
        self.velocidad_maxima = vel_max
        self.velocidad_actual = 0
    
    def moverse(self, distancia):
        """Implementación de movimiento terrestre"""
        if self.bateria > 0:
            self.estado = "moviendo"
            
            # Calcular desplazamiento basado en orientación
            theta_rad = math.radians(self.posicion['theta'])
            dx = distancia * math.cos(theta_rad)
            dy = distancia * math.sin(theta_rad)
            
            self.actualizar_posicion(dx, dy)
            
            # Consumo de batería proporcional a distancia
            self.bateria -= distancia * 0.1
            
            self.estado = "detenido"
            return True
        else:
            print(f"❌ {self.id}: Batería agotada")
            return False
    
    def acelerar(self, incremento):
        """Acelerar el robot"""
        nueva_vel = min(self.velocidad_actual + incremento, 
                       self.velocidad_maxima)
        self.velocidad_actual = nueva_vel
    
    def frenar(self):
        """Detener el robot"""
        self.velocidad_actual = 0

class BrazoRobotico(Robot):
    """Brazo robótico con articulaciones"""
    
    def __init__(self, id_robot, modelo, num_articulaciones):
        super().__init__(id_robot, modelo)
        self.num_articulaciones = num_articulaciones
        self.angulos = [0] * num_articulaciones
        self.objeto_sujetado = None
    
    def moverse(self, distancia):
        """Movimiento del efector final"""
        # Simplificación: mover en dirección actual
        if self.bateria > 0:
            self.actualizar_posicion(distancia, 0)
            self.bateria -= distancia * 0.2
            return True
        return False
    
    def mover_articulacion(self, num_articulacion, angulo):
        """Mover una articulación específica"""
        if 0 <= num_articulacion < self.num_articulaciones:
            self.angulos[num_articulacion] = angulo
            self.bateria -= 0.3
        else:
            raise ValueError(f"Articulación {num_articulacion} no existe")
    
    def sujetar(self, objeto):
        """Sujetar un objeto"""
        if self.objeto_sujetado is None:
            self.objeto_sujetado = objeto
            print(f"✓ {self.id} sujetó: {objeto}")
        else:
            print(f"❌ {self.id} ya tiene un objeto")
    
    def soltar(self):
        """Soltar objeto"""
        if self.objeto_sujetado:
            obj = self.objeto_sujetado
            self.objeto_sujetado = None
            print(f"✓ {self.id} soltó: {obj}")

class SistemaControl:
    """Sistema de control para múltiples robots"""
    
    def __init__(self):
        self.robots = {}
    
    def agregar_robot(self, robot):
        """Agregar robot al sistema"""
        self.robots[robot.id] = robot
        print(f"✓ Robot {robot.id} agregado al sistema")
    
    def comando_global(self, comando, *args):
        """Enviar comando a todos los robots"""
        for robot in self.robots.values():
            if hasattr(robot, comando):
                metodo = getattr(robot, comando)
                metodo(*args)
    
    def estado_sistema(self):
        """Mostrar estado de todos los robots"""
        print(f"\n{'='*60}")
        print("ESTADO DEL SISTEMA")
        print(f"{'='*60}")
        for robot in self.robots.values():
            print(f"{robot}")
            pos = robot.posicion
            print(f"  Posición: ({pos['x']:.2f}, {pos['y']:.2f}), "
                  f"Orientación: {pos['theta']:.1f}°")
        print(f"{'='*60}\n")

# Uso del sistema
sistema = SistemaControl()

# Crear robots
robot1 = RobotMovil("R001", "Explorer-X", vel_max=3.0)
robot2 = RobotMovil("R002", "Scout-Y", vel_max=2.5)
brazo = BrazoRobotico("B001", "Arm-6DOF", num_articulaciones=6)

# Agregar al sistema
sistema.agregar_robot(robot1)
sistema.agregar_robot(robot2)
sistema.agregar_robot(brazo)

# Comandos individuales
robot1.moverse(5)
robot1.rotar(45)
robot1.moverse(3)

brazo.mover_articulacion(0, 90)
brazo.mover_articulacion(1, 45)
brazo.sujetar("Objeto A")

# Comando global
sistema.comando_global('rotar', 180)

# Estado del sistema
sistema.estado_sistema()