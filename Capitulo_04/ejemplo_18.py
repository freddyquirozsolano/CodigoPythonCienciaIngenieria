# Operador NOT - Invierte el valor
sistema_activo = False

if not sistema_activo:
    print("Sistema apagado")
    print("Iniciando secuencia de arranque...")

# Ejemplo práctico
tiene_permiso = False

if not tiene_permiso:
    print("Acceso denegado")
    print("Solicite permisos al administrador")

# Combinando NOT con otras condiciones
motor_encendido = True
sensor_funcional = False

if motor_encendido and not sensor_funcional:
    print("⚠️ Advertencia: Motor activo sin sensor")
    print("Detener motor para evitar daños")