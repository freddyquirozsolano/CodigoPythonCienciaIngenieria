import csv

# Escribir CSV con el módulo csv
datos = [
    ["Experimento", "Temperatura", "Presión", "Resultado"],
    ["Exp-001", 25.5, 101.3, "Exitoso"],
    ["Exp-002", 30.0, 98.7, "Fallido"],
    ["Exp-003", 22.3, 103.1, "Exitoso"]
]

with open("experimentos.csv", "w", newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(datos)

# Leer CSV con el módulo csv
with open("experimentos.csv", "r") as archivo:
    lector = csv.reader(archivo)
    encabezados = next(lector)  # Primera fila
    
    print(f"{'Experimento':<12} {'Temp(°C)':>10} {'Presión(kPa)':>15} {'Resultado':>10}")
    print("-" * 50)
    
    for fila in lector:
        exp = fila[0]
        temp = float(fila[1])
        presion = float(fila[2])
        resultado = fila[3]
        print(f"{exp:<12} {temp:>10.1f} {presion:>15.1f} {resultado:>10}")