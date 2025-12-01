# Solo números pares
pares = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Temperaturas normales (36-37.5°C)
todas_temps = [36.2, 37.8, 36.5, 38.5, 37.0, 35.9]
normales = [t for t in todas_temps if 36 <= t <= 37.5]
# [36.2, 36.5, 37.0]
print("Números pares:", pares)