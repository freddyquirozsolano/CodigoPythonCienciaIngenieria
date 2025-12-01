class Perro:
    # Atributo de clase (compartido por todos)
    especie = 'Canis familiaris'
    contador_perros = 0
    
    def __init__(self, nombre, raza):
        self.nombre = nombre  # Atributo de instancia
        self.raza = raza
        Perro.contador_perros += 1  # Incrementar contador

perro1 = Perro('Max', 'Labrador')
perro2 = Perro('Luna', 'Husky')

print(Perro.especie)  # Canis familiaris
print(Perro.contador_perros)  # 2
