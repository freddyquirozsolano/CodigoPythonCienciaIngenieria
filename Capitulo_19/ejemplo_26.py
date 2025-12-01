# tests/test_paciente.py
import unittest
from src.modelos.paciente import Paciente

class TestPaciente(unittest.TestCase):
    """Pruebas para la clase Paciente"""
    
    def setUp(self):
        """Preparar paciente de prueba antes de cada test"""
        self.paciente = Paciente("P001", "Juan Pérez", 45, "O+")
    
    def test_crear_paciente_valido(self):
        """Crear paciente con datos válidos"""
        self.assertEqual(self.paciente.id, "P001")
        self.assertEqual(self.paciente.nombre, "Juan Pérez")
        self.assertEqual(self.paciente.edad, 45)
        self.assertEqual(self.paciente.tipo_sangre, "O+")
    
    def test_nombre_invalido(self):
        """Nombre vacío debe generar error"""
        with self.assertRaises(ValueError):
            Paciente("P002", "", 30, "A+")
    
    def test_edad_invalida(self):
        """Edad fuera de rango debe generar error"""
        with self.assertRaises(ValueError):
            Paciente("P002", "María", -5, "A+")
        
        with self.assertRaises(ValueError):
            Paciente("P002", "María", 200, "A+")
    
    def test_tipo_sangre_invalido(self):
        """Tipo de sangre inválido debe generar error"""
        with self.assertRaises(ValueError):
            Paciente("P002", "María", 30, "X+")
    
    def test_agregar_alergia(self):
        """Agregar alergia al paciente"""
        self.paciente.agregar_alergia("Penicilina")
        self.assertIn("penicilina", self.paciente.alergias)
    
    def test_registrar_signo_vital(self):
        """Registrar signo vital"""
        self.paciente.registrar_signo_vital("fc", 75, "bpm")
        self.assertEqual(len(self.paciente.historial), 1)
        self.assertEqual(self.paciente.historial[0]['tipo'], "fc")
        self.assertEqual(self.paciente.historial[0]['valor'], 75)
    
    def test_obtener_ultimos_signos(self):
        """Obtener últimos registros de signos vitales"""
        # Registrar varios signos
        for i in range(10):
            self.paciente.registrar_signo_vital("fc", 70 + i, "bpm")
        
        # Obtener últimos 5
        ultimos = self.paciente.obtener_ultimos_signos(5)
        self.assertEqual(len(ultimos), 5)
        self.assertEqual(ultimos[-1]['valor'], 79)

if __name__ == '__main__':
    unittest.main(verbosity=2)