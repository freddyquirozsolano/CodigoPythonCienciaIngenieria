import json
# Si tienes JSON como string (ej. de una API)
json_string = '{"nombre": "Robot-X", "velocidad": 2.5, "activo": true}'

datos = json.loads(json_string)  # loads = load string
print(datos['nombre'])  # 'Robot-X'
print(datos['velocidad'])  # 2.5
print(datos['activo'])  # True (JSON true se convierte a Python True)
