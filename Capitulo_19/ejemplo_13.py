# archivo: test_calculadora_medica.py
import unittest
from calculadora_medica import calcular_dosis, calcular_imc

class TestCalculadoraMedica(unittest.TestCase):
    """Pruebas para funciones de calculadora médica"""
    
    def setUp(self):
        """Se ejecuta antes de cada prueba"""
        print("Preparando prueba...")
    
    def tearDown(self):
        """Se ejecuta después de cada prueba"""
        print("Limpiando después de prueba...")
    
    def test_calcular_imc_normal(self):
        """Prueba cálculo de IMC con valores normales"""
        resultado = calcular_imc(70, 1.75)
        self.assertAlmostEqual(resultado, 22.86, places=2)
    
    def test_calcular_imc_bajo_peso(self):
        """Prueba clasificación de bajo peso"""
        imc = calcular_imc(50, 1.75)
        self.assertLess(imc, 18.5)
    
    def test_calcular_dosis_correcta(self):
        """Prueba cálculo de dosis de medicamento"""
        resultado = calcular_dosis(70, 10, 5)
        self.assertEqual(resultado['dosis_total'], 350.0)
        self.assertEqual(resultado['volumen'], 35.0)
    
    def test_calcular_dosis_valores_invalidos(self):
        """Prueba manejo de errores con valores inválidos"""
        with self.assertRaises(ValueError):
            calcular_dosis(-70, 10, 5)
        
        with self.assertRaises(ValueError):
            calcular_dosis(70, 0, 5)
    
    def test_calcular_dosis_tipos_datos(self):
        """Prueba con diferentes tipos de datos"""
        # Debe funcionar con enteros
        resultado1 = calcular_dosis(70, 10, 5)
        self.assertIsInstance(resultado1, dict)
        
        # Debe funcionar con flotantes
        resultado2 = calcular_dosis(70.5, 10.2, 5.5)
        self.assertIsInstance(resultado2, dict)

# Ejecutar pruebas
if __name__ == '__main__':
    unittest.main(verbosity=2)