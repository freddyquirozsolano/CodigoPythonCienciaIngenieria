texto = "Sensor de temperatura: 25.5°C"

# find() - buscar substring (retorna índice o -1)
posicion = texto.find('temperatura')  # 10

# index() - buscar substring (genera error si no existe)
posicion = texto.index('temperatura')  # 10

# count() - contar apariciones
veces = texto.count('a')  # 4

# startswith() y endswith()
if texto.startswith('Sensor'):
    print('Es un sensor')

if texto.endswith('°C'):
    print('Temperatura en Celsius')
