# ✅ RECOMENDADO - Cierra automáticamente
from pathlib import Path

# Obtener la ruta del archivo datos.txt relativa al script
ruta_archivo = Path(__file__).parent / 'datos.txt'

with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
    contenido = archivo.read()   # Leer el contenido
    print(contenido)             # Usar el contenido
# El archivo se cierra automáticamente al salir del bloque 'with'
# Incluso si hubo un error, el archivo se cerró correctamente
