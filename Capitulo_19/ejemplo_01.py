# ❌ Mal diseño - hace demasiadas cosas
class Paciente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def calcular_imc(self, peso, altura):
        return peso / (altura ** 2)
    
    def guardar_en_bd(self):
        # Código para guardar en base de datos
        pass
    
    def enviar_email(self):
        # Código para enviar email
        pass

# ✅ Buen diseño - responsabilidades separadas
class Paciente:
    def __init__(self, nombre, edad, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.altura = altura
    
    def calcular_imc(self):
        return self.peso / (self.altura ** 2)

class RepositorioPacientes:
    def guardar(self, paciente):
        # Código para guardar en base de datos
        pass

class ServicioNotificaciones:
    def enviar_email(self, destinatario, mensaje):
        # Código para enviar email
        pass