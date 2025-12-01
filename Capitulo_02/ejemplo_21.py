# Sintaxis básica de input()
nombre = input("¿Cuál es tu nombre? ")
print(f"Hola, {nombre}!")

# ⚠️ IMPORTANTE: input() SIEMPRE devuelve un string
edad_texto = input("¿Cuál es tu edad? ")
# Si el usuario escribe "25", edad_texto será el string "25", no el número 25

# Para usar como número, debemos convertir
edad = int(edad_texto)
año_nacimiento = 2025 - edad
print(f"Naciste aproximadamente en {año_nacimiento}")