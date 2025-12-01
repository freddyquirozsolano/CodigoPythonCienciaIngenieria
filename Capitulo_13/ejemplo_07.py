try:
    numero = int(input('Ingresa un número: '))
    resultado = 100 / numero
except ValueError:
    print('Debes ingresar un número')
except ZeroDivisionError:
    print('No puedes dividir entre cero')
else:
    print(f'Resultado exitoso: {resultado}')
finally:
    print('Operación completada')
