# Sistema de login
usuario_ingresado = input("Usuario: ")
contraseña_ingresada = input("Contraseña: ")

# Credenciales correctas (en aplicación real, nunca hardcodear)
usuario_correcto = "admin"
contraseña_correcta = "segura123"

if usuario_ingresado == usuario_correcto and contraseña_ingresada == contraseña_correcta:
    print("\n✓ Acceso concedido")
    print("Bienvenido al sistema")
    print("Cargando panel de administración...")
else:
    print("\n✗ Acceso denegado")
    print("Usuario o contraseña incorrectos")
    print("Intente nuevamente")