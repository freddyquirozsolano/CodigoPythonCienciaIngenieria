try:
    resultado = 10 / 0
except ZeroDivisionError as error:
    print(f'Se produjo un error: {error}')
    # Salida: Se produjo un error: division by zero
