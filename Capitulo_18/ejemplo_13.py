# Consumir APIs con requests
import requests
import json

# Ejemplo 1: API pública de clima
print("=== Consultando API de Clima ===")
ciudad = "London"
api_key = "tu_api_key_aqui"  # Obtener en openweathermap.org
url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}"

response = requests.get(url)
if response.status_code == 200:
    datos = response.json()
    temp_kelvin = datos['main']['temp']
    temp_celsius = temp_kelvin - 273.15
    print(f"Temperatura en {ciudad}: {temp_celsius:.1f}°C")
    print(f"Descripción: {datos['weather'][0]['description']}")
else:
    print(f"Error: {response.status_code}")

# Ejemplo 2: POST a nuestra API Flask
print("\n=== Actualizando Sensor via API ===")
url_api = "http://localhost:5000/actualizar"
datos_sensor = {
    "id": 1,
    "valor": 26.8
}

response = requests.post(url_api, json=datos_sensor)
print(f"Status: {response.status_code}")
print(f"Respuesta: {response.json()}")

# Ejemplo 3: Descargar archivo
print("\n=== Descargando Archivo ===")
url_archivo = "https://ejemplo.com/datos.csv"
response = requests.get(url_archivo)
if response.status_code == 200:
    with open('datos_descargados.csv', 'wb') as f:
        f.write(response.content)
    print("Archivo descargado exitosamente")