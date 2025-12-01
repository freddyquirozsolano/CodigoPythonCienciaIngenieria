# archivo: test_sistema_usuarios.py
import unittest
from sistema_usuarios import Usuario, SistemaAutenticacion

class TestUsuario(unittest.TestCase):
    """Pruebas para la clase Usuario"""
    
    def test_crear_usuario_valido(self):
        """Crear usuario con datos válidos"""
        usuario = Usuario("juan@ejemplo.com", "Juan Pérez")
        self.assertEqual(usuario.email, "juan@ejemplo.com")
        self.assertEqual(usuario.nombre, "Juan Pérez")
        self.assertIsNotNone(usuario.id)
    
    def test_email_invalido(self):
        """Email sin formato correcto debe fallar"""
        with self.assertRaises(ValueError):
            Usuario("email_invalido", "Juan Pérez")
    
    def test_password_debil(self):
        """Contraseña débil debe ser rechazada"""
        usuario = Usuario("juan@ejemplo.com", "Juan")
        with self.assertRaises(ValueError):
            usuario.establecer_password("123")

class TestSistemaAutenticacion(unittest.TestCase):
    """Pruebas para sistema de autenticación"""
    
    def setUp(self):
        """Preparar sistema para cada prueba"""
        self.sistema = SistemaAutenticacion()
        self.usuario_test = self.sistema.registrar(
            "test@ejemplo.com",
            "Test User",
            "Password123!"
        )
    
    def test_login_exitoso(self):
        """Login con credenciales correctas"""
        resultado = self.sistema.login("test@ejemplo.com", "Password123!")
        self.assertTrue(resultado['exito'])
        self.assertIsNotNone(resultado['token'])
    
    def test_login_password_incorrecta(self):
        """Login con contraseña incorrecta debe fallar"""
        resultado = self.sistema.login("test@ejemplo.com", "password_mala")
        self.assertFalse(resultado['exito'])
        self.assertIn('error', resultado)
    
    def test_login_usuario_no_existe(self):
        """Login con usuario inexistente debe fallar"""
        resultado = self.sistema.login("noexiste@ejemplo.com", "123456")
        self.assertFalse(resultado['exito'])
    
    def test_registro_duplicado(self):
        """No se puede registrar dos veces el mismo email"""
        with self.assertRaises(ValueError):
            self.sistema.registrar(
                "test@ejemplo.com",
                "Otro Usuario",
                "Password456!"
            )
    
    def tearDown(self):
        """Limpiar después de cada prueba"""
        self.sistema.limpiar()

if __name__ == '__main__':
    # Ejecutar pruebas con reporte detallado
    unittest.main(verbosity=2)