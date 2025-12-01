import re

# Búsqueda simple
texto = "Paciente: Juan Pérez, ID: 12345"

# Buscar patrón
resultado = re.search(r'\d+', texto)  # \d+ busca uno o más dígitos
if resultado:
    print(resultado.group())  # '12345'

# Encontrar todas las coincidencias
numeros = re.findall(r'\d+', texto)
print(numeros)  # ['12345']
