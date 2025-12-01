# calculadora_mecatronica.py
# Calculadora para Mecatrónica y Robótica

import math

print("=" * 60)
print("🤖 CALCULADORA DE MECATRÓNICA")
print("=" * 60)
print()

print("Selecciona una operación:")
print("1. Conversión de ángulos (Grados ↔ Radianes)")
print("2. Velocidad angular a RPM")
print("3. Torque requerido")
print("4. Tiempo de aceleración")
print()

opcion = input("Ingresa el número de opción: ")

if opcion == "1":
    print("\n--- Conversión de Ángulos ---")
    tipo = input("¿Convertir de (G)rados o (R)adianes? ").upper()
    if tipo == "G":
        grados = float(input("Ángulo en grados: "))
        radianes = grados * math.pi / 180
        print(f"{grados}° = {radianes:.4f} radianes")
    else:
        radianes = float(input("Ángulo en radianes: "))
        grados = radianes * 180 / math.pi
        print(f"{radianes} rad = {grados:.4f}°")

elif opcion == "2":
    print("\n--- Velocidad Angular a RPM ---")
    vel_angular = float(input("Velocidad angular (rad/s): "))
    rpm = (vel_angular * 60) / (2 * math.pi)
    print(f"Velocidad: {rpm:.2f} RPM")

elif opcion == "3":
    print("\n--- Cálculo de Torque ---")
    fuerza = float(input("Fuerza aplicada (N): "))
    distancia = float(input("Distancia al centro (m): "))
    torque = fuerza * distancia
    print(f"Torque: {torque:.2f} N·m")

elif opcion == "4":
    print("\n--- Tiempo de Aceleración ---")
    vel_inicial = float(input("Velocidad inicial (m/s): "))
    vel_final = float(input("Velocidad final (m/s): "))
    aceleracion = float(input("Aceleración (m/s²): "))
    tiempo = (vel_final - vel_inicial) / aceleracion
    print(f"Tiempo necesario: {tiempo:.2f} segundos")

else:
    print("Opción no válida")

print("\n¡Gracias por usar la calculadora de mecatrónica!")