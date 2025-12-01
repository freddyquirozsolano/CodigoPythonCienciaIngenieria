import json
# Leer JSON desde archivo
with open('configuracion.json', 'r', encoding='utf-8') as archivo:
    config = json.load(archivo)  # Convierte JSON a diccionario Python

# Ahora config es un diccionario normal de Python
print(config['servidor'])    # Acceder a valores
print(config['puerto'])
print(config['debug'])
