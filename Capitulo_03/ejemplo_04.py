# Configuración de robot con validación
print("=== CONFIGURACIÓN DE ROBOT MÓVIL ===\n")

# Velocidad máxima
while True:
    try:
        vel_max = float(input("Velocidad máxima (m/s, 0.1-5.0): "))
        if 0.1 <= vel_max <= 5.0:
            break
        print("⚠️ Velocidad fuera del rango seguro")
    except ValueError:
        print("⚠️ Ingrese un número válido")

# Modo de operación
modos = ["manual", "automatico", "teleoperado"]
while True:
    modo = input(f"Modo de operación ({'/'.join(modos)}): ").lower()
    if modo in modos:
        break
    print(f"⚠️ Modo no válido. Opciones: {', '.join(modos)}")

# Confirmación
confirmacion = input("\n¿Confirmar configuración? (S/N): ").upper()
if confirmacion == "S":
    print("\n✓ Robot configurado correctamente")
    print(f"Velocidad máxima: {vel_max} m/s")
    print(f"Modo: {modo.capitalize()}")
else:
    print("\n✗ Configuración cancelada")