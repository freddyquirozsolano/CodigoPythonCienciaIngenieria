# Control de decimales con :.Nf (N = número de decimales)
pi = 3.14159265359

print(f"Pi con 2 decimales: {pi:.2f}")      # 3.14
print(f"Pi con 4 decimales: {pi:.4f}")      # 3.1416
print(f"Pi sin decimales: {pi:.0f}")        # 3

# Ejemplos prácticos
temperatura = 36.789
print(f"Temperatura: {temperatura:.1f}°C")  # 36.8°C

imc = 23.456789
print(f"IMC: {imc:.2f}")                    # 23.46

# Notación científica
distancia = 149597870700  # Distancia Tierra-Sol en metros
print(f"Distancia: {distancia:.2e} m")      # 1.50e+11 m