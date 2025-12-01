# 🏥 Ejemplo Biomédico: Sistema de Alertas
class SujetoObservable:
    def __init__(self):
        self._observadores = []
    
    def agregar_observador(self, observador):
        self._observadores.append(observador)
    
    def notificar_observadores(self, datos):
        for observador in self._observadores:
            observador.actualizar(datos)

class MonitorSignosVitales(SujetoObservable):
    def __init__(self):
        super().__init__()
        self.frecuencia_cardiaca = 70
    
    def establecer_frecuencia(self, fc):
        self.frecuencia_cardiaca = fc
        if fc > 100 or fc < 60:
            self.notificar_observadores({
                'tipo': 'alerta',
                'fc': fc,
                'mensaje': 'FC fuera de rango normal'
            })

class PantallaMonitor:
    def actualizar(self, datos):
        print(f"🖥️  ALERTA EN PANTALLA: {datos['mensaje']}")

class SistemaAlarma:
    def actualizar(self, datos):
        print(f"🔔 ALARMA SONORA: FC={datos['fc']} bpm")

class RegistroEventos:
    def actualizar(self, datos):
        print(f"📝 Registrado en log: {datos}")

# Uso
monitor = MonitorSignosVitales()
monitor.agregar_observador(PantallaMonitor())
monitor.agregar_observador(SistemaAlarma())
monitor.agregar_observador(RegistroEventos())

monitor.establecer_frecuencia(115)  # Dispara notificaciones