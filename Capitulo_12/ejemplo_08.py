from datetime import datetime
from abc import ABC, abstractmethod

class Usuario:
    """Clase para representar usuarios"""
    
    contador_usuarios = 0  # Atributo de clase
    
    def __init__(self, username, email, password):
        Usuario.contador_usuarios += 1
        self.id = Usuario.contador_usuarios
        self.username = username
        self.email = email
        self._password_hash = self._hash_password(password)
        self.fecha_creacion = datetime.now()
        self.ultimo_login = None
        self.activo = True
    
    def _hash_password(self, password):
        """Simulación de hash (usar bcrypt en producción)"""
        return f"HASH_{password}_SALT"
    
    def verificar_password(self, password):
        """Verificar contraseña"""
        return self._hash_password(password) == self._password_hash
    
    def login(self):
        """Registrar login"""
        self.ultimo_login = datetime.now()
        print(f"✓ Usuario {self.username} inició sesión")
    
    def __str__(self):
        return f"Usuario: {self.username} ({self.email})"
    
    def __repr__(self):
        return f"Usuario({self.username!r}, {self.email!r})"

class UsuarioAdmin(Usuario):
    """Usuario con privilegios de administrador"""
    
    def __init__(self, username, email, password, nivel_acceso=1):
        super().__init__(username, email, password)
        self.nivel_acceso = nivel_acceso
        self.acciones_admin = []
    
    def registrar_accion(self, accion):
        """Registrar acción administrativa"""
        self.acciones_admin.append({
            'accion': accion,
            'timestamp': datetime.now()
        })
    
    def eliminar_usuario(self, usuario):
        """Eliminar usuario (admin only)"""
        usuario.activo = False
        self.registrar_accion(f"Eliminó usuario {usuario.username}")
        print(f"✓ Admin {self.username} eliminó a {usuario.username}")

class Permiso:
    """Clase para representar permisos"""
    
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
    
    def __str__(self):
        return self.nombre
    
    def __eq__(self, otro):
        return self.nombre == otro.nombre
    
    def __hash__(self):
        return hash(self.nombre)

class Rol:
    """Clase para agrupar permisos"""
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.permisos = set()
    
    def agregar_permiso(self, permiso):
        self.permisos.add(permiso)
    
    def tiene_permiso(self, permiso_nombre):
        return any(p.nombre == permiso_nombre for p in self.permisos)
    
    def __str__(self):
        return f"Rol: {self.nombre} ({len(self.permisos)} permisos)"

class UsuarioConRol(Usuario):
    """Usuario con sistema de roles y permisos"""
    
    def __init__(self, username, email, password):
        super().__init__(username, email, password)
        self.roles = []
    
    def asignar_rol(self, rol):
        if rol not in self.roles:
            self.roles.append(rol)
            print(f"✓ Rol '{rol.nombre}' asignado a {self.username}")
    
    def tiene_permiso(self, permiso_nombre):
        """Verificar si tiene un permiso específico"""
        for rol in self.roles:
            if rol.tiene_permiso(permiso_nombre):
                return True
        return False
    
    def listar_permisos(self):
        """Obtener todos los permisos del usuario"""
        todos_permisos = set()
        for rol in self.roles:
            todos_permisos.update(rol.permisos)
        return todos_permisos

class SistemaAutenticacion:
    """Sistema de autenticación y autorización"""
    
    def __init__(self):
        self.usuarios = {}
        self.sesiones_activas = {}
    
    def registrar_usuario(self, usuario):
        """Registrar nuevo usuario"""
        if usuario.username in self.usuarios:
            raise ValueError(f"Usuario {usuario.username} ya existe")
        self.usuarios[usuario.username] = usuario
        print(f"✓ Usuario {usuario.username} registrado")
    
    def autenticar(self, username, password):
        """Autenticar usuario"""
        if username not in self.usuarios:
            return False, "Usuario no existe"
        
        usuario = self.usuarios[username]
        
        if not usuario.activo:
            return False, "Usuario desactivado"
        
        if usuario.verificar_password(password):
            usuario.login()
            # Crear sesión
            import uuid
            token = str(uuid.uuid4())
            self.sesiones_activas[token] = usuario
            return True, token
        
        return False, "Contraseña incorrecta"
    
    def verificar_permiso(self, token, permiso_nombre):
        """Verificar si la sesión tiene un permiso"""
        if token not in self.sesiones_activas:
            return False
        
        usuario = self.sesiones_activas[token]
        
        if isinstance(usuario, UsuarioConRol):
            return usuario.tiene_permiso(permiso_nombre)
        elif isinstance(usuario, UsuarioAdmin):
            return True  # Admin tiene todos los permisos
        
        return False

# Uso del sistema
sistema = SistemaAutenticacion()

# Crear permisos
perm_leer = Permiso("leer", "Leer contenido")
perm_escribir = Permiso("escribir", "Crear/modificar contenido")
perm_eliminar = Permiso("eliminar", "Eliminar contenido")

# Crear roles
rol_editor = Rol("Editor")
rol_editor.agregar_permiso(perm_leer)
rol_editor.agregar_permiso(perm_escribir)

rol_moderador = Rol("Moderador")
rol_moderador.agregar_permiso(perm_leer)
rol_moderador.agregar_permiso(perm_escribir)
rol_moderador.agregar_permiso(perm_eliminar)

# Crear usuarios
admin = UsuarioAdmin("admin", "admin@ejemplo.com", "admin123")
usuario1 = UsuarioConRol("juan", "juan@ejemplo.com", "pass123")
usuario2 = UsuarioConRol("maria", "maria@ejemplo.com", "pass456")

# Asignar roles
usuario1.asignar_rol(rol_editor)
usuario2.asignar_rol(rol_moderador)

# Registrar en sistema
sistema.registrar_usuario(admin)
sistema.registrar_usuario(usuario1)
sistema.registrar_usuario(usuario2)

# Autenticación
exito, token = sistema.autenticar("juan", "pass123")
if exito:
    print(f"Token de sesión: {token[:20]}...")
    
    # Verificar permisos
    puede_escribir = sistema.verificar_permiso(token, "escribir")
    puede_eliminar = sistema.verificar_permiso(token, "eliminar")
    
    print(f"Puede escribir: {puede_escribir}")
    print(f"Puede eliminar: {puede_eliminar}")

# Acciones administrativas
admin.eliminar_usuario(usuario2)

print(f"\nTotal usuarios creados: {Usuario.contador_usuarios}")