import csv
# Datos como lista de listas
datos = [
    ['Nombre', 'Edad', 'Ciudad'],  # Encabezados
    ['María', '32', 'Lima'],
    ['Juan', '45', 'Bogotá'],
    ['Ana', '28', 'Ciudad de México']
]

with open('personas.csv', 'w', newline='', encoding='utf-8') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(datos)  # Escribir todas las filas de una vez
