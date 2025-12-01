# Buscar un elemento y detener cuando lo encuentres
numeros = [3, 7, 2, 9, 5, 1, 8, 4]
objetivo = 9

print("Buscando el número", objetivo)

for i, numero in enumerate(numeros):
    print(f"Revisando posición {i}: {numero}")
    
    if numero == objetivo:
        print(f"¡Encontrado en posición {i}!")
        break  # Salir del bucle inmediatamente
else:
    # Este bloque se ejecuta si el bucle NO fue interrumpido por break
    print(f"Número {objetivo} no encontrado")

# Ejemplo: Validación con límite de intentos
intentos = 0
max_intentos = 5

while True:  # Bucle infinito
    intentos += 1
    password = input(f"Intento {intentos}: Ingrese contraseña: ")
    
    if password == "correcta":
        print("✓ Acceso concedido")
        break  # Salir del bucle
    
    if intentos >= max_intentos:
        print("✗ Máximo de intentos alcanzado")
        break  # Salir del bucle
    
    print("Contraseña incorrecta, intente nuevamente")