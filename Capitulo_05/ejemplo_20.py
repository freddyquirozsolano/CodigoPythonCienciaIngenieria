# Análisis de distribución de esfuerzos en una estructura
print("=== ANÁLISIS DE DISTRIBUCIÓN DE ESFUERZOS ===\n")

# Tensor de esfuerzos en diferentes puntos (MPa)
esfuerzos = [
    [120, 135, 142, 138, 125],
    [115, 150, 165, 155, 130],
    [110, 145, 180, 160, 135],
    [118, 155, 175, 165, 140],
    [125, 140, 150, 145, 135]
]

limite_elastico = 250  # MPa
esfuerzo_critico = 200  # MPa

filas = len(esfuerzos)
columnas = len(esfuerzos[0])

print(f"Análisis de {filas}x{columnas} puntos de medición")
print(f"Límite elástico: {limite_elastico} MPa")
print(f"Esfuerzo crítico: {esfuerzo_critico} MPa\n")

esfuerzo_maximo = 0
posicion_maxima = (0, 0)
puntos_criticos = 0
suma_esfuerzos = 0

print("DISTRIBUCIÓN DE ESFUERZOS (MPa):")
print("    ", end="")
for j in range(columnas):
    print(f"Col{j}  ", end="")
print()

for i in range(filas):
    print(f"F{i}  ", end="")
    for j in range(columnas):
        esfuerzo = esfuerzos[i][j]
        print(f"{esfuerzo:4}  ", end="")
        
        suma_esfuerzos += esfuerzo
        
        if esfuerzo > esfuerzo_maximo:
            esfuerzo_maximo = esfuerzo
            posicion_maxima = (i, j)
        
        if esfuerzo > esfuerzo_critico:
            puntos_criticos += 1
    print()

esfuerzo_promedio = suma_esfuerzos / (filas * columnas)
factor_seguridad_minimo = limite_elastico / esfuerzo_maximo

print(f"\nRESULTADOS DEL ANÁLISIS:")
print(f"Esfuerzo máximo: {esfuerzo_maximo} MPa en posición {posicion_maxima}")
print(f"Esfuerzo promedio: {esfuerzo_promedio:.1f} MPa")
print(f"Puntos críticos (>{esfuerzo_critico} MPa): {puntos_criticos}")
print(f"Factor de seguridad mínimo: {factor_seguridad_minimo:.2f}")

if puntos_criticos > 0:
    print(f"\n⚠️ ADVERTENCIA: {puntos_criticos} puntos con esfuerzo crítico")
    print("   Considerar reforzamiento en zonas críticas")
    
    print("\nPUNTOS CRÍTICOS DETECTADOS:")
    for i in range(filas):
        for j in range(columnas):
            if esfuerzos[i][j] > esfuerzo_critico:
                print(f"  Posición ({i},{j}): {esfuerzos[i][j]} MPa")

if factor_seguridad_minimo < 1.5:
    print("\n🚨 CRÍTICO: Factor de seguridad insuficiente")
    print("   Se requiere rediseño")
elif factor_seguridad_minimo < 2.0:
    print("\n⚠️ PRECAUCIÓN: Factor de seguridad bajo")
    print("   Se recomienda revisión del diseño")
else:
    print("\n✓ Estructura dentro de parámetros seguros")