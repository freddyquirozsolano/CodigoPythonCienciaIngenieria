# Programa: Calculadora de espacio en disco
print("=== CALCULADORA DE ALMACENAMIENTO ===")
print()

# Obtener información
capacidad_gb = float(input("Capacidad total del disco (GB): "))
usado_gb = float(input("Espacio usado (GB): "))

# Cálculos
disponible_gb = capacidad_gb - usado_gb
porcentaje_usado = (usado_gb / capacidad_gb) * 100
porcentaje_libre = 100 - porcentaje_usado

# Convertir a otras unidades
disponible_mb = disponible_gb * 1024
disponible_tb = disponible_gb / 1024

# Estado del disco
espacio_critico = porcentaje_usado > 90

# Mostrar resultados
print("\n=== ANÁLISIS DE ALMACENAMIENTO ===")
print(f"Capacidad total: {capacidad_gb:.2f} GB")
print(f"Espacio usado: {usado_gb:.2f} GB ({porcentaje_usado:.1f}%)")
print(f"Espacio disponible: {disponible_gb:.2f} GB ({porcentaje_libre:.1f}%)")
print(f"Espacio disponible: {disponible_mb:.0f} MB")
print(f"Espacio disponible: {disponible_tb:.4f} TB")

if espacio_critico:
    print("\n⚠️ ADVERTENCIA: Espacio en disco crítico!")
else:
    print("\n✓ Espacio en disco saludable")