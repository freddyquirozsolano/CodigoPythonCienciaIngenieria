# División segura con manejo de excepciones
try:
    numero = int(input('Ingresa un número: '))
    resultado = 100 / numero
    print(f'Resultado: {resultado}')
except:
    print('Error: Por favor ingresa un número válido diferente de cero')
