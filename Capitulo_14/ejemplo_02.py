from pathlib import Path

# Obtener la ruta del archivo datos.txt relativa al script
ruta_archivo = Path(__file__).parent / 'registro.txt'

# Escribir texto en un archivo (modo 'w' sobrescribe)
datos = 'Temperatura: 36.5°C\nHumedad: 60%\nPresión: 1013 hPa'

with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
    archivo.write(datos)  # Escribir el string completo

# Contenido de registro.txt:
# Temperatura: 36.5°C
# Humedad: 60%
# Presión: 1013 hPa
