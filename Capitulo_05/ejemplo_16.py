# Bucle for anidado básico
for i in range(3):  # Bucle externo
    for j in range(4):  # Bucle interno
        print(f"i={i}, j={j}")

# Crear una tabla de multiplicar
print("TABLA DE MULTIPLICAR (1-5)\n")

for i in range(1, 6):
    for j in range(1, 6):
        resultado = i * j
        print(f"{resultado:3}", end=" ")
    print()  # Nueva línea después de cada fila

# Salida:
#   1   2   3   4   5 
#   2   4   6   8  10 
#   3   6   9  12  15 
#   4   8  12  16  20 
#   5  10  15  20  25