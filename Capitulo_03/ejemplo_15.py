# Datos de paciente en formato CSV (simulando lectura de archivo)
linea_datos = "García,Ana,45,O+,68.5,1.65,120/80,37.2"

# Procesar datos
campos = linea_datos.split(",")
apellido = campos[0].strip()
nombre = campos[1].strip()
edad = int(campos[2])
tipo_sangre = campos[3].strip()
peso = float(campos[4])
altura = float(campos[5])
presion = campos[6].strip()
temperatura = float(campos[7])

# Extraer presión arterial
presion_partes = presion.split("/")
sistolica = int(presion_partes[0])
diastolica = int(presion_partes[1])

# Normalizar nombre (título)
nombre_completo = f"{nombre} {apellido}".title()

# Crear código de paciente
iniciales = nombre[0] + apellido[0]
codigo_paciente = f"{iniciales.upper()}-{edad:03d}-{tipo_sangre.replace('+', 'P').replace('-', 'N')}"

print(f"Código: {codigo_paciente}")
print(f"Nombre: {nombre_completo}")
print(f"Presión: {sistolica}/{diastolica} mmHg")