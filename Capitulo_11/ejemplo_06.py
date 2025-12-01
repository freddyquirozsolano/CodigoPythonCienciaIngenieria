class Paciente:
    '''Clase para gestionar información de pacientes'''
    
    # Atributo de clase
    hospital = 'Hospital General'
    total_pacientes = 0
    
    def __init__(self, nombre, edad, id_paciente):
        self.nombre = nombre
        self.edad = edad
        self.id_paciente = id_paciente
        self.historial_medico = []
        self.signos_vitales = {}
        Paciente.total_pacientes += 1
    
    def registrar_signos_vitales(self, presion, temperatura, frecuencia):
        '''Registrar signos vitales del paciente'''
        self.signos_vitales = {
            'presion': presion,
            'temperatura': temperatura,
            'frecuencia_cardiaca': frecuencia
        }
        return f'Signos vitales registrados para {self.nombre}'
    
    def agregar_diagnostico(self, diagnostico):
        '''Agregar diagnóstico al historial médico'''
        self.historial_medico.append(diagnostico)
        return f'Diagnóstico agregado al expediente de {self.nombre}'
    
    def calcular_imc(self, peso, altura):
        '''Calcular Índice de Masa Corporal'''
        imc = peso / (altura ** 2)
        if imc < 18.5:
            clasificacion = 'Bajo peso'
        elif imc < 25:
            clasificacion = 'Peso normal'
        elif imc < 30:
            clasificacion = 'Sobrepeso'
        else:
            clasificacion = 'Obesidad'
        return f'{self.nombre}: IMC = {imc:.2f} ({clasificacion})'
    
    def __str__(self):
        return f'Paciente: {self.nombre} | ID: {self.id_paciente} | Edad: {self.edad} años'

# Uso de la clase
paciente1 = Paciente('María López', 45, 'P001')
print(paciente1)
print(paciente1.registrar_signos_vitales('120/80', 36.5, 72))
print(paciente1.calcular_imc(70, 1.65))
print(f'Total de pacientes registrados: {Paciente.total_pacientes}')
