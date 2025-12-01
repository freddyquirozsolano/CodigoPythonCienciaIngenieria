# Manejo seguro de archivos
archivo = None
try:
    archivo = open('datos.txt', 'r')
    contenido = archivo.read()
    print(contenido)
except FileNotFoundError:
    print('Error: Archivo no encontrado')
finally:
    if archivo:
        archivo.close()
        print('Archivo cerrado correctamente')
