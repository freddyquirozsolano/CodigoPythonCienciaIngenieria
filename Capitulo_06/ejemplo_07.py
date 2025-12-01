# Ordenar y buscar
temperaturas = [37.5, 36.8, 38.2, 36.5, 37.0]

# Ordenar ascendente
temperaturas.sort()
print(temperaturas)  # [36.5, 36.8, 37.0, 37.5, 38.2]

# Ordenar descendente
temperaturas.sort(reverse=True)
print(temperaturas)  # [38.2, 37.5, 37.0, 36.8, 36.5]

# Contar apariciones
lecturas = [1, 2, 2, 3, 2, 4, 2, 5]
veces = lecturas.count(2)
print(f"El 2 aparece {veces} veces")  # El 2 aparece 4 veces
