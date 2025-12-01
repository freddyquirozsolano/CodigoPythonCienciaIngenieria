import csv
# Datos como lista de diccionarios (más claro)
pacientes = [
    {'nombre': 'María López', 'edad': 45, 'tipo_sangre': 'O+'},
    {'nombre': 'Juan Pérez', 'edad': 32, 'tipo_sangre': 'A+'},
    {'nombre': 'Ana García', 'edad': 28, 'tipo_sangre': 'B+'}
]
with open('pacientes.csv', 'w', newline='', encoding='utf-8') as archivo:
    # Especificar los nombres de las columnas
    campos = ['nombre', 'edad', 'tipo_sangre']
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    
    escritor.writeheader()      # Escribir encabezados
    escritor.writerows(pacientes)  # Escribir todas las filas
