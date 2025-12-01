# Simulación de procesamiento de archivos
print("=== PROCESAMIENTO BATCH DE ARCHIVOS ===\n")

archivos = [
    "reporte_2025_01.txt",
    "reporte_2025_02.txt",
    "datos_2025_03.csv",
    "reporte_2025_04.txt",
    "imagen_2025_05.png",
    "reporte_2025_06.txt"
]

print(f"Total de archivos a procesar: {len(archivos)}\n")

archivos_procesados = 0
archivos_txt = 0
archivos_csv = 0
archivos_otros = 0

for i, archivo in enumerate(archivos, 1):
    print(f"[{i}/{len(archivos)}] Procesando: {archivo}")
    
    # Determinar tipo de archivo
    if archivo.endswith('.txt'):
        archivos_txt += 1
        print("  → Tipo: Archivo de texto")
        print("  → Acción: Analizar contenido")
    elif archivo.endswith('.csv'):
        archivos_csv += 1
        print("  → Tipo: Archivo CSV")
        print("  → Acción: Importar a base de datos")
    else:
        archivos_otros += 1
        print("  → Tipo: Otro formato")
        print("  → Acción: Omitir")
    
    archivos_procesados += 1
    progreso = (archivos_procesados / len(archivos)) * 100
    print(f"  → Progreso: {progreso:.1f}%")
    print()

print("=" * 50)
print("RESUMEN DEL PROCESAMIENTO")
print("=" * 50)
print(f"Archivos procesados: {archivos_procesados}")
print(f"Archivos .txt: {archivos_txt}")
print(f"Archivos .csv: {archivos_csv}")
print(f"Otros archivos: {archivos_otros}")
print("✓ Procesamiento completado")