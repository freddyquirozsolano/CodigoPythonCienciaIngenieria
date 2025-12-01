# Patrón: Obtener y convertir en una línea
edad = int(input("Ingresa tu edad: "))
peso = float(input("Ingresa tu peso (kg): "))
nombre = input("Ingresa tu nombre: ")  # Ya es string, no necesita conversión

# Usar los datos
print(f"{nombre}, tienes {edad} años y pesas {peso} kg")