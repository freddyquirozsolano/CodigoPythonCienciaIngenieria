# Registro de paciente con validación completa
print("=== REGISTRO DE NUEVO PACIENTE ===\n")

# Nombre (no puede estar vacío)
while True:
    nombre = input("Nombre completo: ").strip()
    if nombre:
        break
    print("⚠️ El nombre no puede estar vacío")

# Edad con validación
while True:
    try:
        edad = int(input("Edad (0-120): "))
        if 0 <= edad <= 120:
            break
        print("⚠️ Edad fuera de rango")
    except ValueError:
        print("⚠️ Debe ingresar un número entero")

# Tipo de sangre
tipos_validos = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
while True:
    tipo_sangre = input("Tipo de sangre (A+, A-, B+, B-, AB+, AB-, O+, O-): ").upper()
    if tipo_sangre in tipos_validos:
        break
    print(f"⚠️ Tipo de sangre no válido. Opciones: {', '.join(tipos_validos)}")

# Peso con validación
while True:
    try:
        peso = float(input("Peso (kg): "))
        if 2 <= peso <= 300:  # Rango razonable
            break
        print("⚠️ Peso fuera de rango razonable")
    except ValueError:
        print("⚠️ Debe ingresar un número válido")

print("\n✓ Paciente registrado exitosamente")
print(f"Paciente: {nombre}, {edad} años, {tipo_sangre}, {peso} kg")