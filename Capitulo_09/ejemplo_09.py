def suma_mala(a, b):
    print(a + b)  # Solo imprime, no retorna nada
resultado = suma_mala(5, 3)  # resultado es None
print(f"Resultado de la suma: {resultado}")
nuevo = resultado * 2  # ERROR: no puedes usar None