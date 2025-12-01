# f-strings (Python 3.6+) - Recomendado
nombre = 'Robot-X'
velocidad = 2.5678
bateria = 85.5

# Formateo con precisión decimal
reporte = f"Robot: {nombre} | Vel: {velocidad:.2f} m/s | Batería: {bateria:.1f}%"
print(reporte)  # 'Robot: Robot-X | Vel: 2.57 m/s | Batería: 85.5%'

# Alineación y padding
print(f"{nombre:>15}")  # Alinear derecha, 15 caracteres
print(f"{nombre:<15}")  # Alinear izquierda
print(f"{nombre:^15}")  # Centrar

# Números con formato
costo = 1234567.89
print(f"${costo:,.2f}")  # '$1,234,567.89'
