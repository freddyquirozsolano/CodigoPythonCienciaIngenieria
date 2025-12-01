def procesar_datos(datos, indice, divisor):
    try:
        valor = datos[indice]
        resultado = valor / divisor
        return resultado
    except IndexError:
        print('Error: Índice fuera de rango')
        return None
    except ZeroDivisionError:
        print('Error: No se puede dividir entre cero')
        return None
    except TypeError:
        print('Error: Tipo de dato inválido')
        return None

# Ejemplo de uso
datos = [10, 20, 30, 40, 50]
print(procesar_datos(datos, 2, 5))    # Salida: 6.0
print(procesar_datos(datos, 10, 5))   # Salida: Error: Índice fuera de rango
print(procesar_datos(datos, 2, 0))    # Salida: Error: No se puede dividir entre cero
print(procesar_datos(datos, 2, 'a'))  # Salida: Error: Tipo de dato inválido