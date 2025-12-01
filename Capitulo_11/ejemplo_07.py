import math

class Robot:
    '''Clase para controlar un robot móvil'''
    
    def __init__(self, id_robot, modelo):
        self.id_robot = id_robot
        self.modelo = modelo
        self.posicion_x = 0.0
        self.posicion_y = 0.0
        self.orientacion = 0.0  # ángulo en grados
        self.bateria = 100.0
        self.velocidad_max = 2.0  # m/s
        self.activo = False
    
    def encender(self):
        '''Encender el robot'''
        if self.bateria > 10:
            self.activo = True
            return f'{self.id_robot} encendido. Batería: {self.bateria}%'
        else:
            return f'{self.id_robot}: Batería insuficiente'
    
    def apagar(self):
        '''Apagar el robot'''
        self.activo = False
        return f'{self.id_robot} apagado'
    
    def mover(self, distancia):
        '''Mover el robot en la dirección actual'''
        if not self.activo:
            return f'{self.id_robot} está apagado'
        
        if self.bateria < 5:
            return f'{self.id_robot}: Batería muy baja para moverse'
        
        # Calcular nueva posición
        rad = math.radians(self.orientacion)
        self.posicion_x += distancia * math.cos(rad)
        self.posicion_y += distancia * math.sin(rad)
        
        # Consumir batería
        self.bateria -= distancia * 0.5
        
        return f'{self.id_robot} movió {distancia}m. Nueva posición: ({self.posicion_x:.2f}, {self.posicion_y:.2f})'
    
    def rotar(self, angulo):
        '''Rotar el robot (ángulo en grados)'''
        if not self.activo:
            return f'{self.id_robot} está apagado'
        
        self.orientacion = (self.orientacion + angulo) % 360
        self.bateria -= abs(angulo) * 0.01
        return f'{self.id_robot} rotó {angulo}°. Nueva orientación: {self.orientacion:.1f}°'
    
    def cargar_bateria(self, cantidad):
        '''Cargar la batería'''
        self.bateria = min(100, self.bateria + cantidad)
        return f'{self.id_robot}: Batería cargada al {self.bateria:.1f}%'
    
    def obtener_estado(self):
        '''Obtener estado completo del robot'''
        estado = 'ACTIVO' if self.activo else 'APAGADO'
        return f'''
Robot {self.id_robot} ({self.modelo})
Estado: {estado}
Posición: ({self.posicion_x:.2f}, {self.posicion_y:.2f})
Orientación: {self.orientacion:.1f}°
Batería: {self.bateria:.1f}%
'''
    
    def __str__(self):
        return f'Robot {self.id_robot} ({self.modelo}) - Batería: {self.bateria:.1f}%'

# Uso de la clase
robot1 = Robot('R001', 'Navigator-X')
print(robot1.encender())
print(robot1.mover(5))
print(robot1.rotar(90))
print(robot1.mover(3))
print(robot1.obtener_estado())
