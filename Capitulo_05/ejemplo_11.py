# Análisis de fuerzas en vigas de una estructura
print("=== ANÁLISIS DE CARGAS EN ESTRUCTURA ===\n")

# Cargas aplicadas en diferentes puntos (en kN)
cargas = [10, 15, 20, 18, 12, 25, 30, 22]
distancias = [0, 1.5, 3, 4.5, 6, 7.5, 9, 10.5]  # metros desde apoyo

print(f"Número de cargas: {len(cargas)}")
print(f"Longitud total: {distancias[-1]} metros\n")

carga_total = 0
momento_total = 0
carga_maxima = 0
posicion_maxima = 0

print("ANÁLISIS DE CARGAS:")
print("-" * 50)

for i in range(len(cargas)):
    carga = cargas[i]
    distancia = distancias[i]
    momento = carga * distancia
    
    print(f"Punto {i+1}:")
    print(f"  Posición: {distancia:.1f} m")
    print(f"  Carga: {carga} kN")
    print(f"  Momento: {momento:.1f} kN·m")
    
    carga_total += carga
    momento_total += momento
    
    if carga > carga_maxima:
        carga_maxima = carga
        posicion_maxima = distancia
    
    print()

# Calcular reacciones
longitud_viga = distancias[-1]
reaccion_A = momento_total / longitud_viga
reaccion_B = carga_total - reaccion_A

print("=" * 50)
print("RESULTADOS DEL ANÁLISIS:")
print("=" * 50)
print(f"Carga total: {carga_total} kN")
print(f"Momento total: {momento_total:.1f} kN·m")
print(f"Carga máxima: {carga_maxima} kN en posición {posicion_maxima} m")
print(f"\nReacciones en apoyos:")
print(f"  Reacción A (x=0): {reaccion_A:.2f} kN")
print(f"  Reacción B (x={longitud_viga}): {reaccion_B:.2f} kN")
print(f"\nVerificación: {reaccion_A + reaccion_B:.2f} kN (debe ser {carga_total} kN)")