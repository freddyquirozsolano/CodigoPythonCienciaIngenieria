# Variable global (definida fuera de funciones)
temperatura_ambiente = 25

def medir_temperatura():
    # Variable local (solo existe dentro de la función)
    temperatura_paciente = 37.5
    print(f"Temperatura del paciente: {temperatura_paciente}°C")
    print(f"Temperatura ambiente: {temperatura_ambiente}°C")  # Puede leer globales

medir_temperatura()
# Salida:
# Temperatura del paciente: 37.5°C
# Temperatura ambiente: 25°C

print(temperatura_ambiente)  # Funciona: 25
# print(temperatura_paciente)  # ERROR: temperatura_paciente no existe aquí