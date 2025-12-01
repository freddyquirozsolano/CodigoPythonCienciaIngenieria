import pandas as pd
import json

# Leer JSON
# Debes agregar el archivo 'datos.json' en el mismo directorio para que funcione
df = pd.read_json('datos.json')

# Leer JSON con diferentes orientaciones
df = pd.read_json('datos.json', orient='records')   # Lista de objetos
df = pd.read_json('datos.json', orient='columns')   # Objeto de columnas

# Exportar a JSON
df.to_json('resultado.json', orient='records', indent=2)

# Leer y aplanar JSON anidado (estructuras complejas)
with open('datos.json', 'r') as f:
    data = json.load(f)
    df = pd.json_normalize(data)   # Aplanar JSON anidado
