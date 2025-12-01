# Validación básica con try-except
while True:
    try:
        edad = int(input("Ingrese su edad: "))
        if edad < 0 or edad > 120:
            print("⚠️ Error: La edad debe estar entre 0 y 120 años")
            continue
        break  # Salir del bucle si la edad es válida
    except ValueError:
        print("⚠️ Error: Debe ingresar un número entero")

print(f"Edad registrada: {edad} años")

# Validación de opciones limitadas
while True:
    opcion = input("Seleccione (S/N): ").upper()
    if opcion in ["S", "N"]:
        break
    print("⚠️ Error: Debe ingresar S o N")

# Validación de rango numérico
while True:
    try:
        temperatura = float(input("Temperatura corporal (35-42°C): "))
        if 35 <= temperatura <= 42:
            break
        print("⚠️ Temperatura fuera del rango normal")
    except ValueError:
        print("⚠️ Debe ingresar un número válido")