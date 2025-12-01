class Perro:
    def __init__(self, nombre, raza, edad):
        # Atributos de instancia
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

# Crear objetos con diferentes atributos
mi_perro = Perro('WallE', 'Labrador', 3)
tu_perro = Perro('Luna', 'Husky', 5)

# Acceder a los atributos
print(f'{mi_perro.nombre} es un {mi_perro.raza}')
# Max es un Labrador
