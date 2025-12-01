# Sistema de login con límite de intentos
print("=== SISTEMA DE AUTENTICACIÓN ===\n")

password_correcto = "segura123"
intentos_maximos = 3
intentos = 0
autenticado = False

while intentos < intentos_maximos and not autenticado:
    intentos += 1
    print(f"Intento {intentos} de {intentos_maximos}")
    password = input("Ingrese contraseña: ")
    
    if password == password_correcto:
        autenticado = True
        print("\n✓ Acceso concedido")
        print("Bienvenido al sistema")
    else:
        intentos_restantes = intentos_maximos - intentos
        if intentos_restantes > 0:
            print(f"✗ Contraseña incorrecta")
            print(f"Intentos restantes: {intentos_restantes}\n")
        else:
            print("\n🔒 Cuenta bloqueada")
            print("Demasiados intentos fallidos")