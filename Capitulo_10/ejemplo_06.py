# Cálculos de ingeniería con módulos estándar
import math
import statistics

def calcular_esfuerzo_viga(momento, distancia, inercia):
    """Calcula esfuerzo de flexión en viga"""
    return (momento * distancia) / inercia

def analizar_serie_datos(datos):
    """Análisis estadístico de datos experimentales"""
    return {
        'promedio': statistics.mean(datos),
        'desviacion': statistics.stdev(datos),
        'minimo': min(datos),
        'maximo': max(datos),
        'rango': max(datos) - min(datos)
    }

# Datos de prueba de materiales (esfuerzo en MPa)
esfuerzos = [250, 248, 252, 249, 251, 253, 247]

print("Análisis de Resultados Experimentales")
print("=" * 50)

analisis = analizar_serie_datos(esfuerzos)
for clave, valor in analisis.items():
    print(f"{clave.capitalize()}: {valor:.2f} MPa")

# Verificar si está dentro de especificaciones
especificacion = 250  # MPa
tolerancia = 5  # MPa

if all(abs(e - especificacion) <= tolerancia for e in esfuerzos):
    print("\n✓ Todas las muestras dentro de especificación")
else:
    print("\n✗ Algunas muestras fuera de especificación")