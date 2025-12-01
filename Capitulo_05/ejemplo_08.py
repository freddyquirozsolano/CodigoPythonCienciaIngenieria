# Análisis de presión arterial durante el día
print("=== ANÁLISIS DE PRESIÓN ARTERIAL ===\n")

# Mediciones de presión sistólica durante 24 horas
presiones = [120, 118, 125, 130, 128, 135, 140, 138, 
             132, 128, 125, 122, 124, 126, 130, 135,
             140, 145, 142, 138, 132, 128, 124, 120]

print(f"Total de mediciones: {len(presiones)}")
print(f"Mediciones: {presiones[:5]}... (mostrando primeras 5)\n")

# Calcular estadísticas
suma_total = 0
presion_maxima = presiones[0]
presion_minima = presiones[0]
mediciones_elevadas = 0

for i, presion in enumerate(presiones):
    suma_total += presion
    
    if presion > presion_maxima:
        presion_maxima = presion
    
    if presion < presion_minima:
        presion_minima = presion
    
    if presion > 140:
        mediciones_elevadas += 1
        print(f"⚠️ Hora {i:02d}:00 - Presión elevada: {presion} mmHg")

presion_promedio = suma_total / len(presiones)
porcentaje_elevado = (mediciones_elevadas / len(presiones)) * 100

print(f"\nESTADÍSTICAS:")
print(f"Presión promedio: {presion_promedio:.1f} mmHg")
print(f"Presión máxima: {presion_maxima} mmHg")
print(f"Presión mínima: {presion_minima} mmHg")
print(f"Mediciones elevadas: {mediciones_elevadas} ({porcentaje_elevado:.1f}%)")

if porcentaje_elevado > 30:
    print("\n⚠️ ALERTA: Más del 30% de mediciones elevadas")
    print("   Consultar con cardiólogo")