import logging
logging.basicConfig(level=logging.DEBUG)
def dividir(a, b):
    try:
        resultado = a / b
        logging.info(f'División exitosa: {a}/{b} = {resultado}')
        return resultado
    except ZeroDivisionError:
        logging.error('Intento de división entre cero', exc_info=True)
        return None

if __name__ == '__main__':
    numeros = [(10, 2), (5, 0), (8, 4)]
    for a, b in numeros:
        dividir(a, b)