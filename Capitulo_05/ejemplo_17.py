# Procesamiento de matriz (lista de listas)
matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print("MATRIZ ORIGINAL:")
for fila in matriz:
    for elemento in fila:
        print(f"{elemento:3}", end=" ")
    print()

# Sumar todos los elementos
suma_total = 0
for fila in matriz:
    for elemento in fila:
        suma_total += elemento

print(f"\nSuma de todos los elementos: {suma_total}")

# Encontrar el valor máximo
maximo = matriz[0][0]
posicion_max = (0, 0)

for i, fila in enumerate(matriz):
    for j, elemento in enumerate(fila):
        if elemento > maximo:
            maximo = elemento
            posicion_max = (i, j)

print(f"Valor máximo: {maximo} en posición {posicion_max}")