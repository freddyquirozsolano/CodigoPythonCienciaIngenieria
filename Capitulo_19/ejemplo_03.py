# 🤖 Ejemplo Mecatrónica: Factory de Sensores
class Sensor:
    def leer(self):
        raise NotImplementedError

class SensorTemperatura(Sensor):
    def leer(self):
        return f"Temperatura: {random.uniform(20, 30):.1f}°C"

class SensorPresion(Sensor):
    def leer(self):
        return f"Presión: {random.uniform(1000, 1020):.1f} hPa"

class SensorHumedad(Sensor):
    def leer(self):
        return f"Humedad: {random.uniform(40, 70):.1f}%"

class FabricaSensores:
    @staticmethod
    def crear_sensor(tipo):
        if tipo == 'temperatura':
            return SensorTemperatura()
        elif tipo == 'presion':
            return SensorPresion()
        elif tipo == 'humedad':
            return SensorHumedad()
        else:
            raise ValueError(f"Tipo de sensor desconocido: {tipo}")

# Uso
sensor = FabricaSensores.crear_sensor('temperatura')
print(sensor.leer())