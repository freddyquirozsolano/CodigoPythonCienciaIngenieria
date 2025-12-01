datos = [10, 20, 30, 40, 50]

# remove(): eliminar por valor (primera aparición)
datos.remove(30)
print(datos)  # [10, 20, 40, 50]

# pop(): eliminar por índice y devolver el valor
ultimo = datos.pop()  # Elimina el último
print(ultimo)  # 50
print(datos)  # [10, 20, 40]

segundo = datos.pop(1)  # Elimina el elemento en índice 1
print(segundo)  # 20
print(datos)  # [10, 40]

# del: eliminar por índice o rango
numeros = [1, 2, 3, 4, 5, 6]
del numeros[0]  # Elimina el primero
print(numeros)  # [2, 3, 4, 5, 6]

# clear(): vaciar toda la lista
datos.clear()
print(datos)  # []
