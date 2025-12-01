# calculadora_sistemas.py
# Calculadora para Ingeniería en Sistemas

print("=" * 60)
print("💻 CALCULADORA DE SISTEMAS")
print("=" * 60)
print()

print("Selecciona una operación:")
print("1. Conversión de unidades de almacenamiento")
print("2. Tiempo de transferencia de archivos")
print("3. Conversión de sistemas numéricos")
print("4. Cálculo de direcciones IP disponibles")
print()

opcion = input("Ingresa el número de opción: ")

if opcion == "1":
    print("\n--- Conversión de Almacenamiento ---")
    gb = float(input("Cantidad en GB: "))
    mb = gb * 1024
    kb = mb * 1024
    bytes_total = kb * 1024
    print(f"{gb} GB = {mb:.0f} MB = {kb:.0f} KB = {bytes_total:.0f} Bytes")

elif opcion == "2":
    print("\n--- Tiempo de Transferencia ---")
    tamaño_mb = float(input("Tamaño del archivo (MB): "))
    velocidad_mbps = float(input("Velocidad de conexión (Mbps): "))
    tiempo_segundos = (tamaño_mb * 8) / velocidad_mbps
    print(f"Tiempo estimado: {tiempo_segundos:.2f} segundos")

elif opcion == "3":
    print("\n--- Conversión Numérica ---")
    decimal = int(input("Número decimal: "))
    print(f"Binario: {bin(decimal)}")
    print(f"Octal: {oct(decimal)}")
    print(f"Hexadecimal: {hex(decimal)}")

elif opcion == "4":
    print("\n--- Direcciones IP Disponibles ---")
    mascara = int(input("Máscara de subred (ej. 24 para /24): "))
    hosts = (2 ** (32 - mascara)) - 2
    print(f"Direcciones IP disponibles: {hosts}")

else:
    print("Opción no válida")

print("\n¡Gracias por usar la calculadora de sistemas!")