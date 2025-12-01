# Procesar solo números pares
for i in range(1, 11):
    if i % 2 != 0:  # Si es impar
        continue  # Saltar al siguiente número
    
    print(f"{i} es par")

# Salida:
# 2 es par
# 4 es par
# 6 es par
# 8 es par
# 10 es par

# Ejemplo: Filtrar datos inválidos
temperaturas = [36.5, -999, 37.2, 38.1, -999, 36.8, 39.5]

print("Procesando temperaturas válidas:")
suma = 0
contador = 0

for temp in temperaturas:
    if temp < 0:  # Dato inválido
        print(f"  Omitiendo dato inválido: {temp}")
        continue  # Saltar al siguiente
    
    print(f"  Temperatura válida: {temp}°C")
    suma += temp
    contador += 1

if contador > 0:
    promedio = suma / contador
    print(f"\nTemperatura promedio: {promedio:.2f}°C")