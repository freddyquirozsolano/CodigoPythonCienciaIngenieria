class Perro:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
    
    def __str__(self):
        return f'{self.nombre} ({self.raza}, {self.edad} años)'

mi_perro = Perro('Max', 'Labrador', 3)
print(mi_perro)  # Max (Labrador, 3 años)
