# Control de calidad de materiales
resistencia_medida = float(input("Resistencia medida (MPa): "))
resistencia_minima = 400  # MPa

print(f"\n=== CONTROL DE CALIDAD ===")
print(f"Resistencia medida: {resistencia_medida} MPa")
print(f"Resistencia mínima: {resistencia_minima} MPa")

if resistencia_medida >= resistencia_minima:
    print("\n✓ MATERIAL ACEPTADO")
    print("El material cumple con las especificaciones")
    print("Autorizado para uso en construcción")
else:
    diferencia = resistencia_minima - resistencia_medida
    print("\n✗ MATERIAL RECHAZADO")
    print(f"Déficit: {diferencia:.1f} MPa")
    print("El material no cumple especificaciones")
    print("Acción: Devolver al proveedor")