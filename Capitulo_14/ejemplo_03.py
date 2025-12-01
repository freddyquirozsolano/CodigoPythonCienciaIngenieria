import csv
# Supongamos que pacientes.csv contiene:
# nombre,edad,presion
# María López,45,120/80
# Juan Pérez,32,118/75
# Ana García,28,115/72

with open('pacientes.csv', 'r', encoding='utf-8') as archivo:
    lector = csv.reader(archivo)
    
    # Saltar encabezado si existe
    encabezados = next(lector)  # Primera línea
    print(f'Columnas: {encabezados}')
    # Salida: Columnas: ['nombre', 'edad', 'presion']
    
    # Leer datos
    for fila in lector:
        nombre, edad, presion = fila  # Desempaquetar lista
        print(f'{nombre}: {edad} años, PA: {presion}')
        # Salida: María López: 45 años, PA: 120/80
