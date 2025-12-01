# Encontrar raíz cuadrada usando método iterativo
print("=== MÉTODO DE NEWTON-RAPHSON ===\n")

numero = 25
tolerancia = 0.0001
x = numero / 2  # Estimación inicial
iteracion = 0

print(f"Calculando √{numero}")
print(f"Tolerancia: {tolerancia}\n")

while True:
    iteracion += 1
    x_anterior = x
    
    # Fórmula de Newton-Raphson para raíz cuadrada
    x = (x + numero / x) / 2
    
    error = abs(x - x_anterior)
    
    print(f"Iteración {iteracion}: x = {x:.6f}, error = {error:.6f}")
    
    if error < tolerancia:
        print(f"\n✓ Convergencia alcanzada")
        break

print(f"\nResultado: √{numero} ≈ {x:.6f}")
print(f"Verificación: {x}² = {x**2:.6f}")
print(f"Iteraciones necesarias: {iteracion}")