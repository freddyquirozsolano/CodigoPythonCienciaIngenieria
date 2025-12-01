try:
    numero = int(input('Ingresa un número: '))
    resultado = 100 / numero
    print(f'Resultado: {resultado}')
except ValueError:
    print('Error: Debes ingresar un número')
except ZeroDivisionError:
    print('Error: No puedes dividir entre cero')
