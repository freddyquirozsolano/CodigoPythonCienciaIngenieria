# Retornar múltiples valores
def calcular_estadisticas(datos):
    """Calcula promedio, mínimo y máximo de una lista"""
    promedio = sum(datos) / len(datos)
    minimo = min(datos)
    maximo = max(datos)
    return promedio, minimo, maximo  # Retorna tupla

# Desempaquetar los valores
temperaturas = [36.5, 37.2, 36.8, 37.0, 36.9, 37.5, 36.7]
prom, temp_min, temp_max = calcular_estadisticas(temperaturas)

print(f"Promedio: {prom:.2f}°C")
print(f"Mínima: {temp_min}°C")
print(f"Máxima: {temp_max}°C")

# También puedes recibir como tupla
stats = calcular_estadisticas(temperaturas)
print(f"Estadísticas: {stats}")