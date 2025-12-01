# Escribir datos en formato CSV
datos_pacientes = [
    ["Nombre", "Edad", "Tipo Sangre", "Peso"],
    ["Ana García", 45, "O+", 68.5],
    ["Juan Pérez", 32, "A+", 75.0],
    ["María López", 28, "B-", 62.5]
]

with open("pacientes.csv", "w") as archivo:
    for fila in datos_pacientes:
        linea = ",".join(str(campo) for campo in fila)
        archivo.write(linea + "\n")

# Leer datos CSV
with open("pacientes.csv", "r") as archivo:
    lineas = archivo.readlines()
    encabezados = lineas[0].strip().split(",")
    
    print(f"Columnas: {encabezados}")
    print()
    
    for linea in lineas[1:]:  # Saltar encabezados
        campos = linea.strip().split(",")
        nombre = campos[0]
        edad = int(campos[1])
        tipo_sangre = campos[2]
        peso = float(campos[3])
        
        print(f"{nombre}: {edad} años, {tipo_sangre}, {peso} kg")