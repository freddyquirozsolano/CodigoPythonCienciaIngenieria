# calculadora_ingenieria.py
# Calculadora para Ingeniería Civil y Mecánica

print("=" * 60)
print("🔧 CALCULADORA DE INGENIERÍA")
print("=" * 60)
print()

print("Selecciona una operación:")
print("1. Cálculo de fuerza (F = m × a)")
print("2. Cálculo de presión (P = F / A)")
print("3. Cálculo de densidad (ρ = m / V)")
print("4. Conversión de unidades de presión")
print()

opcion = input("Ingresa el número de opción: ")

if opcion == "1":
    print("\n--- Cálculo de Fuerza ---")
    masa = float(input("Masa (kg): "))
    aceleracion = float(input("Aceleración (m/s²): "))
    fuerza = masa * aceleracion
    print(f"Fuerza: {fuerza:.2f} N (Newtons)")

elif opcion == "2":
    print("\n--- Cálculo de Presión ---")
    fuerza = float(input("Fuerza (N): "))
    area = float(input("Área (m²): "))
    presion = fuerza / area
    print(f"Presión: {presion:.2f} Pa (Pascales)")
    print(f"Presión: {presion/1000:.2f} kPa (Kilopascales)")

elif opcion == "3":
    print("\n--- Cálculo de Densidad ---")
    masa = float(input("Masa (kg): "))
    volumen = float(input("Volumen (m³): "))
    densidad = masa / volumen
    print(f"Densidad: {densidad:.2f} kg/m³")

elif opcion == "4":
    print("\n--- Conversión de Presión ---")
    pa = float(input("Presión en Pascales (Pa): "))
    psi = pa * 0.000145038
    bar = pa * 0.00001
    atm = pa * 0.00000986923
    print(f"{pa} Pa = {psi:.4f} PSI")
    print(f"{pa} Pa = {bar:.4f} bar")
    print(f"{pa} Pa = {atm:.6f} atm")

else:
    print("Opción no válida")

print("\n¡Gracias por usar la calculadora de ingeniería!")