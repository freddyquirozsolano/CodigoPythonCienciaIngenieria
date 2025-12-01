# Función con parámetro predeterminado
def convertir_temperatura(celsius, mostrar_kelvin=False):
    """
    Convierte temperatura de Celsius a Fahrenheit.
    Opcionalmente también muestra en Kelvin.
    """
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit:.2f}°F")
    
    if mostrar_kelvin:
        kelvin = celsius + 273.15
        print(f"{celsius}°C = {kelvin:.2f}K")

# Usar el valor predeterminado (False)
convertir_temperatura(25)
# Salida: 25°C = 77.00°F

# Especificar el parámetro opcional
convertir_temperatura(25, True)
# Salida: 
# 25°C = 77.00°F
# 25°C = 298.15K

# Usar nombre del parámetro (más claro)
convertir_temperatura(0, mostrar_kelvin=True)