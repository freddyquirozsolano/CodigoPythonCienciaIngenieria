# Crear y escribir en un archivo
archivo = open("datos.txt", "w")  # "w" = write (escribir)
archivo.write("Primera línea\n")
archivo.write("Segunda línea\n")
archivo.close()

# Forma recomendada: usar 'with' (cierra automáticamente)
with open("datos.txt", "w") as archivo:
    archivo.write("Primera línea\n")
    archivo.write("Segunda línea\n")
    archivo.write("Tercera línea\n")
# El archivo se cierra automáticamente al salir del bloque

# Escribir múltiples líneas
lineas = ["Línea 1\n", "Línea 2\n", "Línea 3\n"]
with open("multiples.txt", "w") as archivo:
    archivo.writelines(lineas)

# Agregar al final de un archivo existente
with open("datos.txt", "a") as archivo:  # "a" = append (agregar)
    archivo.write("Línea adicional\n")