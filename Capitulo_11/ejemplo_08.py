import hashlib
from datetime import datetime

class Usuario:
    '''Clase para gestionar usuarios del sistema'''
    
    usuarios_registrados = 0
    
    def __init__(self, username, email, rol='usuario'):
        self.username = username
        self.email = email
        self.rol = rol
        self.password_hash = None
        self.fecha_creacion = datetime.now()
        self.ultimo_login = None
        self.activo = True
        self.intentos_fallidos = 0
        Usuario.usuarios_registrados += 1
    
    def establecer_password(self, password):
        '''Establecer contraseña (guardada como hash)'''
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()
        return 'Contraseña establecida exitosamente'
    
    def verificar_password(self, password):
        '''Verificar si la contraseña es correcta'''
        password_ingresado = hashlib.sha256(password.encode()).hexdigest()
        return password_ingresado == self.password_hash
    
    def login(self, password):
        '''Intentar iniciar sesión'''
        if not self.activo:
            return 'Cuenta desactivada. Contacta al administrador'
        
        if self.intentos_fallidos >= 3:
            self.activo = False
            return 'Cuenta bloqueada por múltiples intentos fallidos'
        
        if self.verificar_password(password):
            self.ultimo_login = datetime.now()
            self.intentos_fallidos = 0
            return f'Bienvenido, {self.username}!'
        else:
            self.intentos_fallidos += 1
            return f'Contraseña incorrecta. Intentos restantes: {3 - self.intentos_fallidos}'
    
    def cambiar_rol(self, nuevo_rol):
        '''Cambiar rol del usuario'''
        roles_validos = ['usuario', 'moderador', 'admin']
        if nuevo_rol in roles_validos:
            self.rol = nuevo_rol
            return f'Rol actualizado a: {nuevo_rol}'
        return 'Rol no válido'
    
    def desactivar_cuenta(self):
        '''Desactivar la cuenta del usuario'''
        self.activo = False
        return f'Cuenta de {self.username} desactivada'
    
    def __str__(self):
        estado = 'Activa' if self.activo else 'Inactiva'
        return f'Usuario: {self.username} | Email: {self.email} | Rol: {self.rol} | Estado: {estado}'

# Uso de la clase
usuario1 = Usuario('juan_dev', 'juan@ejemplo.com', 'admin')
print(usuario1.establecer_password('MiPassword123'))
print(usuario1.login('MiPassword123'))
print(usuario1)
print(f'Total usuarios registrados: {Usuario.usuarios_registrados}')
