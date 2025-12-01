# Si realmente necesitas modificar una variable global
contador = 0

def incrementar_contador():
    global contador  # Declarar que usarás la global
    contador += 1
    print(f"Contador: {contador}")

incrementar_contador()  # Contador: 1
incrementar_contador()  # Contador: 2
incrementar_contador()  # Contador: 3