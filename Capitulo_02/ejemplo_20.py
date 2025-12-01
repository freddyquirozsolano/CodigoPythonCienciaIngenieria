# Parámetros del material (de un archivo o base de datos)
modulo_young_str = "200000"  # MPa
area_str = "0.025"           # m²
longitud_str = "5.5"         # m

# Convertir a números
modulo_young = float(modulo_young_str)
area = float(area_str)
longitud = float(longitud_str)

# Calcular rigidez axial
rigidez = (modulo_young * area) / longitud
print(f"Rigidez axial: {rigidez:.2f} MN")

# Crear reporte
reporte_rigidez = f"Rigidez: {rigidez:.2f} MN"