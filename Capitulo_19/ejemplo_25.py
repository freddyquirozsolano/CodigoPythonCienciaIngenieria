# src/modelos/paciente.py
from datetime import datetime
import re

class Paciente:
    """
    Representa un paciente en el sistema médico.
    
    Attributes:
        id (str): Identificador único del paciente.
        nombre (str): Nombre completo del paciente.
        edad (int): Edad del paciente en años.
        tipo_sangre (str): Tipo de sangre (A+, O-, etc.).
        alergias (set): Conjunto de alergias conocidas.
        historial (list): Lista de signos vitales registrados.
    """
    
    def __init__(self, id, nombre, edad, tipo_sangre):
        """
        Inicializa un nuevo paciente.
        
        Args:
            id (str): Identificador único.
            nombre (str): Nombre completo.
            edad (int): Edad en años.
            tipo_sangre (str): Tipo sanguíneo.
        
        Raises:
            ValueError: Si los datos son inválidos.
        """
        self.id = id
        self.nombre = self._validar_nombre(nombre)
        self.edad = self._validar_edad(edad)
        self.tipo_sangre = self._validar_tipo_sangre(tipo_sangre)
        self.alergias = set()
        self.historial = []
        self.fecha_registro = datetime.now()
    
    def _validar_nombre(self, nombre):
        """Valida que el nombre sea válido"""
        if not nombre or len(nombre.strip()) < 2:
            raise ValueError("Nombre inválido")
        return nombre.strip()
    
    def _validar_edad(self, edad):
        """Valida que la edad sea válida"""
        if not isinstance(edad, int) or edad < 0 or edad > 150:
            raise ValueError("Edad inválida")
        return edad
    
    def _validar_tipo_sangre(self, tipo):
        """Valida el tipo de sangre"""
        tipos_validos = {'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'}
        if tipo not in tipos_validos:
            raise ValueError(f"Tipo de sangre inválido. Debe ser uno de: {tipos_validos}")
        return tipo
    
    def agregar_alergia(self, alergia):
        """Agrega una alergia al registro del paciente"""
        self.alergias.add(alergia.lower())
    
    def registrar_signo_vital(self, tipo, valor, unidad):
        """
        Registra un signo vital del paciente.
        
        Args:
            tipo (str): Tipo de signo vital ('fc', 'presion', 'temperatura').
            valor: Valor medido.
            unidad (str): Unidad de medida.
        """
        registro = {
            'tipo': tipo,
            'valor': valor,
            'unidad': unidad,
            'timestamp': datetime.now()
        }
        self.historial.append(registro)
    
    def obtener_ultimos_signos(self, n=5):
        """Obtiene los últimos n registros de signos vitales"""
        return self.historial[-n:]
    
    def to_dict(self):
        """Convierte el paciente a diccionario para serialización"""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'edad': self.edad,
            'tipo_sangre': self.tipo_sangre,
            'alergias': list(self.alergias),
            'fecha_registro': self.fecha_registro.isoformat()
        }
    
    def __str__(self):
        return f"Paciente(id={self.id}, nombre={self.nombre}, edad={self.edad})"
    
    def __repr__(self):
        return self.__str__()