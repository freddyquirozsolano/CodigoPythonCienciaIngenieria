import csv
with open('pacientes.csv', 'r', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo)  # Lee encabezados automáticamente
    
    for fila in lector:
        # Acceder por nombre de columna (más claro y seguro)
        print(f"Nombre: {fila['nombre']}")
        print(f"Edad: {fila['edad']}")
        print(f"Presión: {fila['presion']}")
        print('-' * 40)
