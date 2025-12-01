# Programa: Cálculo de esfuerzo en viga
print("=== CALCULADORA DE ESFUERZO EN VIGAS ===")
print()

# Obtener parámetros de la viga
longitud = float(input("Longitud de la viga (m): "))
ancho = float(input("Ancho de la sección (cm): "))
alto = float(input("Alto de la sección (cm): "))
carga = float(input("Carga aplicada (kN): "))

# Convertir unidades (cm a m, kN a N)
ancho_m = ancho / 100
alto_m = alto / 100
carga_n = carga * 1000

# Calcular área y momento de inercia
area = ancho_m * alto_m
momento_inercia = (ancho_m * alto_m ** 3) / 12

# Calcular momento máximo (carga concentrada al centro)
momento_maximo = (carga_n * longitud) / 4

# Calcular esfuerzo máximo
distancia_eje = alto_m / 2
esfuerzo_maximo = (momento_maximo * distancia_eje) / momento_inercia

# Convertir a MPa
esfuerzo_mpa = esfuerzo_maximo / 1e6

# Mostrar resultados
print("\n=== RESULTADOS DEL ANÁLISIS ===")
print(f"Dimensiones: {ancho} cm × {alto} cm × {longitud} m")
print(f"Área de sección: {area:.6f} m²")
print(f"Momento de inercia: {momento_inercia:.8f} m⁴")
print(f"Momento máximo: {momento_maximo:.2f} N·m")
print(f"Esfuerzo máximo: {esfuerzo_mpa:.2f} MPa")

# Verificar límites (acero típico: 250 MPa)
limite_elastico = 250
factor_seguridad = limite_elastico / esfuerzo_mpa

if factor_seguridad < 1.5:
    print(f"\n⚠️ ADVERTENCIA: Factor de seguridad bajo ({factor_seguridad:.2f})")
else:
    print(f"\n✓ Factor de seguridad adecuado ({factor_seguridad:.2f})")