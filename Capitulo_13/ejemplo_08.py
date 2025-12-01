# Ejemplo 08: Uso de prints de depuración para rastrear valores intermedios
def calcular_promedio(numeros):
    print(f'DEBUG: numeros = {numeros}')  # Ver qué recibe
    total = sum(numeros)
    print(f'DEBUG: total = {total}')
    cantidad = len(numeros)
    print(f'DEBUG: cantidad = {cantidad}')
    promedio = total / cantidad
    print(f'DEBUG: promedio = {promedio}')
    return promedio
