# Leer todo el contenido
with open("datos.txt", "r") as archivo:  # "r" = read (leer)
    contenido = archivo.read()
    print(contenido)

# Leer línea por línea
with open("datos.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())  # strip() elimina el \n al final

# Leer todas las líneas en una lista
with open("datos.txt", "r") as archivo:
    lineas = archivo.readlines()
    print(lineas)  # Lista con todas las líneas

# Leer una cantidad específica de líneas
with open("datos.txt", "r") as archivo:
    primera_linea = archivo.readline()
    segunda_linea = archivo.readline()
    print(primera_linea)
    print(segunda_linea)