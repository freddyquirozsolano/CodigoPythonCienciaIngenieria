# División de strings (split)
datos = "Juan,25,O+,70.5"
partes = datos.split(",")
print(partes)  # ['Juan', '25', 'O+', '70.5']

nombre = partes[0]
edad = int(partes[1])
tipo_sangre = partes[2]
peso = float(partes[3])

# División con espacios
frase = "Python es genial"
palabras = frase.split()  # split() sin argumentos divide por espacios
print(palabras)  # ['Python', 'es', 'genial']

# Unión de strings (join)
elementos = ["Juan", "María", "Pedro"]
resultado = ", ".join(elementos)
print(resultado)  # "Juan, María, Pedro"

# Unir con saltos de línea
lineas = ["Línea 1", "Línea 2", "Línea 3"]
texto = "\n".join(lineas)
print(texto)
# Línea 1
# Línea 2
# Línea 3