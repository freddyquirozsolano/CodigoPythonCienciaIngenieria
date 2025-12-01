# Sistema de validación de usuario
intentos_fallidos = 3
tiempo_sesion = 125  # minutos
uso_cpu = 95  # porcentaje

print("=== SISTEMA DE SEGURIDAD ===\n")

if intentos_fallidos >= 3:
    print("🔒 ALERTA DE SEGURIDAD: Cuenta bloqueada")
    print(f"   Intentos fallidos: {intentos_fallidos}")
    print("   Acción: Cuenta bloqueada temporalmente")

if tiempo_sesion > 120:
    print("⏰ AVISO: Sesión extendida")
    print(f"   Tiempo de sesión: {tiempo_sesion} minutos")
    print("   Acción: Solicitar reautenticación")

if uso_cpu > 90:
    print("💻 ALERTA: Uso excesivo de CPU")
    print(f"   CPU: {uso_cpu}%")
    print("   Acción: Revisar procesos activos")