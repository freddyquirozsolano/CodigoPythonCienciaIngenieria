# math - Funciones matemáticas
import math
print(math.sqrt(144))  # Raíz cuadrada: 12.0
print(math.sin(math.pi/2))  # Seno: 1.0
print(math.factorial(5))  # Factorial: 120

# random - Números aleatorios
import random
print(random.randint(1, 100))  # Entero aleatorio entre 1 y 100
print(random.choice(['rojo', 'verde', 'azul']))  # Elemento aleatorio
print(random.random())  # Float entre 0 y 1

# datetime - Manejo de fechas y horas
from datetime import datetime, timedelta
ahora = datetime.now()
print(ahora)  # 2025-11-03 10:30:45.123456
mañana = ahora + timedelta(days=1)
print(mañana)

# os - Interacción con el sistema operativo
import os
print(os.getcwd())  # Directorio actual
print(os.listdir('.'))  # Archivos en directorio
# os.mkdir('nueva_carpeta')  # Crear directorio

# sys - Información del sistema Python
import sys
print(sys.version)  # Versión de Python
print(sys.platform)  # Sistema operativo

# json - Trabajar con JSON
import json
datos = {'nombre': 'María', 'edad': 30}
json_string = json.dumps(datos)
print(json_string)  # '{"nombre": "María", "edad": 30}'

# re - Expresiones regulares
import re
patron = r'\d{3}-\d{4}'
if re.match(patron, '555-1234'):
    print('Formato de teléfono válido')