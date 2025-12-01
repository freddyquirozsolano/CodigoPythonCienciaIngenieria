# Usuario ingresa su edad
entrada_usuario = input("Ingresa tu edad: ")  # Siempre retorna string

# Convertir y validar
try:
    edad = int(entrada_usuario)
    es_mayor = edad >= 18
    
    if es_mayor:
        acceso = "Concedido"
    else:
        acceso = "Denegado"
    
    print(f"Edad: {edad} años")
    print(f"Acceso: {acceso}")
except ValueError:
    print("Error: Debes ingresar un número válido")