# Sintaxis
condicion1 = False
condicion2 = True
condicion3 = False

if condicion1:
    # Código si condicion1 es True
    print("Primera condición")
elif condicion2:
    # Código si condicion1 es False y condicion2 es True
    print("Segunda condición")
elif condicion3:
    # Código si condiciones anteriores son False y condicion3 es True
    print("Tercera condición")
else:
    # Código si todas las condiciones anteriores son False
    print("Ninguna condición se cumplió")

# Ejemplo: Clasificación de calificación
nota = 85

if nota >= 90:
    calificacion = "A - Excelente"
elif nota >= 80:
    calificacion = "B - Muy bueno"
elif nota >= 70:
    calificacion = "C - Bueno"
elif nota >= 60:
    calificacion = "D - Suficiente"
else:
    calificacion = "F - Insuficiente"

print(f"Nota: {nota} = {calificacion}")