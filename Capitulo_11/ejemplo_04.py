class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.energia = 100
    
    def ladrar(self):
        return f'{self.nombre} dice: ¡Guau! ¡Guau!'
    
    def correr(self, distancia):
        if self.energia > 10:
            self.energia -= 10
            return f'{self.nombre} corrió {distancia}m. Energía: {self.energia}%'
        else:
            return f'{self.nombre} está muy cansado para correr'
    
    def cumplir_años(self):
        self.edad += 1
        return f'¡{self.nombre} ahora tiene {self.edad} años!'

# Usar los métodos
mi_perro = Perro('Max', 3)
print(mi_perro.ladrar())  # Max dice: ¡Guau! ¡Guau!
print(mi_perro.correr(50))  # Max corrió 50m. Energía: 90%
print(mi_perro.cumplir_años())  # ¡Max ahora tiene 4 años!
