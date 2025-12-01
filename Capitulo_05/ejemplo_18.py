# Simulación de procesamiento de imagen médica simplificada
print("=== ANÁLISIS DE IMAGEN MÉDICA ===\n")

# Matriz de intensidades de píxeles (simulada, valores 0-255)
imagen = [
    [120, 125, 130, 128, 122],
    [118, 240, 245, 242, 120],
    [122, 238, 250, 240, 125],
    [120, 242, 248, 238, 122],
    [125, 128, 130, 126, 124]
]

filas = len(imagen)
columnas = len(imagen[0])

print(f"Dimensiones de imagen: {filas}x{columnas} píxeles")
print("Umbral de detección: 200\n")

# Detectar áreas de alta intensidad (posibles anomalías)
anomalias_detectadas = 0
coordenadas_anomalias = []

print("PROCESANDO IMAGEN:")
for i in range(filas):
    for j in range(columnas):
        intensidad = imagen[i][j]
        
        if intensidad > 200:  # Umbral de detección
            anomalias_detectadas += 1
            coordenadas_anomalias.append((i, j))
            print(f"⚠️ Anomalía detectada en ({i},{j}): intensidad = {intensidad}")

print(f"\nRESULTADO DEL ANÁLISIS:")
print(f"Píxeles totales: {filas * columnas}")
print(f"Anomalías detectadas: {anomalias_detectadas}")
print(f"Porcentaje de área anómala: {(anomalias_detectadas/(filas*columnas))*100:.1f}%")

if anomalias_detectadas > 0:
    print(f"\nCoordenadas de anomalías: {coordenadas_anomalias}")
    print("\n⚠️ RECOMENDACIÓN: Realizar análisis adicional")
else:
    print("\n✓ No se detectaron anomalías significativas")