# Clase base (padre o superclase)
class DispositivoMedico:
    def __init__(self, id_dispositivo, fabricante):
        self.id = id_dispositivo
        self.fabricante = fabricante
        self.estado = "apagado"
        self.bateria = 100
    
    def encender(self):
        self.estado = "encendido"
        print(f"Dispositivo {self.id} encendido")
    
    def apagar(self):
        self.estado = "apagado"
        print(f"Dispositivo {self.id} apagado")
    
    def verificar_bateria(self):
        return f"Batería: {self.bateria}%"

# Clase derivada (hija o subclase)
class Oximetro(DispositivoMedico):
    def __init__(self, id_dispositivo, fabricante):
        super().__init__(id_dispositivo, fabricante)
        self.saturacion_o2 = 0
        self.frecuencia_cardiaca = 0
    
    def medir(self):
        if self.estado == "encendido":
            # Simulación de medición
            self.saturacion_o2 = 98
            self.frecuencia_cardiaca = 72
            return f"SpO2: {self.saturacion_o2}%, FC: {self.frecuencia_cardiaca} bpm"
        else:
            return "Dispositivo apagado"

# Uso
oximetro = Oximetro("OX-001", "MedTech")
oximetro.encender()  # Método heredado
print(oximetro.medir())  # Método específico
print(oximetro.verificar_bateria())  # Método heredado