class Paciente:
    """Clase base para pacientes"""
    
    def __init__(self, id_paciente, nombre, edad):
        self.id = id_paciente
        self.nombre = nombre
        self.edad = edad
        self._historial = []
    
    def agregar_registro(self, registro):
        """Agregar entrada al historial"""
        from datetime import datetime
        self._historial.append({
            'fecha': datetime.now(),
            'registro': registro
        })
    
    def get_historial(self):
        """Obtener historial completo"""
        return self._historial.copy()
    
    def __str__(self):
        return f"Paciente: {self.nombre} (ID: {self.id})"

class PacienteCronico(Paciente):
    """Paciente con enfermedad crónica"""
    
    def __init__(self, id_paciente, nombre, edad, enfermedad):
        super().__init__(id_paciente, nombre, edad)
        self.enfermedad = enfermedad
        self._medicamentos = []
    
    def agregar_medicamento(self, medicamento, dosis):
        self._medicamentos.append({
            'nombre': medicamento,
            'dosis': dosis
        })
    
    def get_medicamentos(self):
        return self._medicamentos.copy()
    
    def __str__(self):
        base = super().__str__()
        return f"{base} - {self.enfermedad}"

class SignoVital:
    """Clase para representar signos vitales"""
    
    def __init__(self, tipo, valor, unidad):
        self.tipo = tipo
        self.valor = valor
        self.unidad = unidad
        from datetime import datetime
        self.timestamp = datetime.now()
    
    def __str__(self):
        return f"{self.tipo}: {self.valor} {self.unidad}"
    
    def __repr__(self):
        return f"SignoVital('{self.tipo}', {self.valor}, '{self.unidad}')"
    
    def es_normal(self):
        """Verificar si el signo vital está en rango normal"""
        rangos = {
            'temperatura': (36.1, 37.2),
            'presion_sistolica': (90, 120),
            'presion_diastolica': (60, 80),
            'frecuencia_cardiaca': (60, 100),
            'saturacion_o2': (95, 100)
        }
        
        if self.tipo in rangos:
            minimo, maximo = rangos[self.tipo]
            return minimo <= self.valor <= maximo
        return True

# Sistema de monitoreo
class MonitorPaciente:
    """Sistema de monitoreo de signos vitales"""
    
    def __init__(self, paciente):
        self.paciente = paciente
        self.signos_vitales = []
    
    def registrar_signo(self, tipo, valor, unidad):
        signo = SignoVital(tipo, valor, unidad)
        self.signos_vitales.append(signo)
        
        # Registrar en historial del paciente
        self.paciente.agregar_registro(str(signo))
        
        # Alertar si está fuera de rango
        if not signo.es_normal():
            self._generar_alerta(signo)
        
        return signo
    
    def _generar_alerta(self, signo):
        print(f"⚠️ ALERTA: {signo} fuera de rango normal")
    
    def resumen(self):
        print(f"\n{'='*50}")
        print(f"Monitor de {self.paciente.nombre}")
        print(f"{'='*50}")
        for signo in self.signos_vitales:
            estado = "✓" if signo.es_normal() else "⚠️"
            print(f"{estado} {signo}")
        print(f"{'='*50}\n")

# Uso del sistema
paciente = PacienteCronico("P001", "María López", 45, "Hipertensión")
paciente.agregar_medicamento("Losartán", "50mg/día")

monitor = MonitorPaciente(paciente)
monitor.registrar_signo('temperatura', 36.5, '°C')
monitor.registrar_signo('presion_sistolica', 135, 'mmHg')
monitor.registrar_signo('frecuencia_cardiaca', 72, 'bpm')
monitor.registrar_signo('saturacion_o2', 98, '%')

monitor.resumen()