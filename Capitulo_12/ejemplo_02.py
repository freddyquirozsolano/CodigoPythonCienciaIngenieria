class Robot:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def moverse(self):
        return f"{self.nombre} se está moviendo"
    
    def realizar_tarea(self):
        return "Realizando tarea genérica"

class RobotTerrestre(Robot):
    def __init__(self, nombre, velocidad_ruedas):
        super().__init__(nombre)
        self.velocidad_ruedas = velocidad_ruedas
    
    def moverse(self):  # Sobrescritura
        return f"{self.nombre} rodando a {self.velocidad_ruedas} m/s"
    
    def realizar_tarea(self):
        return f"{self.nombre} navegando por terreno"

class RobotAereo(Robot):
    def __init__(self, nombre, altitud_max):
        super().__init__(nombre)
        self.altitud_max = altitud_max
    
    def moverse(self):  # Sobrescritura
        return f"{self.nombre} volando hasta {self.altitud_max}m"
    
    def realizar_tarea(self):
        return f"{self.nombre} realizando reconocimiento aéreo"

class RobotAcuatico(Robot):
    def __init__(self, nombre, profundidad_max):
        super().__init__(nombre)
        self.profundidad_max = profundidad_max
    
    def moverse(self):  # Sobrescritura
        return f"{self.nombre} nadando hasta {self.profundidad_max}m"
    
    def realizar_tarea(self):
        return f"{self.nombre} explorando entorno submarino"

# Polimorfismo en acción
robots = [
    RobotTerrestre("Explorer-1", 2.5),
    RobotAereo("Drone-X", 100),
    RobotAcuatico("SubBot", 50)
]

# Misma interfaz, comportamiento diferente
for robot in robots:
    print(robot.moverse())
    print(robot.realizar_tarea())
    print()