# Forma tradicional (concatenación)
nombre = "Ana"
edad = 25
mensaje = "Hola, me llamo " + nombre + " y tengo " + str(edad) + " años"

# Con f-strings (moderno y legible)
mensaje = f"Hola, me llamo {nombre} y tengo {edad} años"

# Puedes incluir expresiones dentro de las llaves
resultado = f"El doble de {edad} es {edad * 2}"

# Llamar funciones
texto = "python"
print(f"Mayúsculas: {texto.upper()}")  # PYTHON