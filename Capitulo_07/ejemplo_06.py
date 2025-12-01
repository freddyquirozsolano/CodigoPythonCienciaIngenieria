# Set vacío - NOTA: usar set(), no {}
vacio = set()  # Correcto
# {} crea un diccionario vacío, no un set

# Set con elementos
numeros = {1, 2, 3, 4, 5}
colores = {'rojo', 'verde', 'azul'}
print(numeros)  # Output: {1, 2, 3, 4, 5}
print(colores)  # Output: {'rojo', 'verde', 'azul'}

# Eliminar duplicados de una lista
lecturas = [10, 20, 10, 30, 20, 40, 10]
valores_unicos = set(lecturas)  # {10, 20, 30, 40}
print(valores_unicos)

# Convertir string a set (caracteres únicos)
letras = set('mississippi')  # {'m', 'i', 's', 'p'}

print(letras)