# Cambio de mayúsculas/minúsculas
texto = "Python para Ingeniería"
print(texto.upper())       # PYTHON PARA INGENIERÍA
print(texto.lower())       # python para ingeniería
print(texto.title())       # Python Para Ingeniería
print(texto.capitalize())  # Python para ingeniería

# Búsqueda y verificación
print("Python" in texto)        # True
print(texto.startswith("Py"))   # True
print(texto.endswith("ría"))    # True
print(texto.find("para"))       # 7 (índice donde empieza)
print(texto.count("a"))         # 3 (número de veces que aparece)

# Reemplazo
nuevo = texto.replace("Ingeniería", "Ciencias")
print(nuevo)  # Python para Ciencias

# Eliminar espacios
datos = "  12.5  "
print(datos.strip())   # "12.5" (elimina espacios al inicio y final)
print(datos.lstrip())  # "12.5  " (elimina espacios a la izquierda)
print(datos.rstrip())  # "  12.5" (elimina espacios a la derecha)