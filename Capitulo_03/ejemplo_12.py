# Datos del análisis
proyecto = "Puente Peatonal 2025"
material = "Acero A36"
longitud_viga = 12.5  # metros
carga_aplicada = 50000  # N
area_seccion = 0.0156  # m²
modulo_young = 200e9  # Pa
esfuerzo_calculado = carga_aplicada / area_seccion  # Pa
esfuerzo_mpa = esfuerzo_calculado / 1e6
limite_elastico = 250  # MPa
factor_seguridad = limite_elastico / esfuerzo_mpa

# Reporte de ingeniería
print("═" * 70)
print(f"{'REPORTE DE ANÁLISIS ESTRUCTURAL':^70}")
print("═" * 70)
print()
print(f"Proyecto:        {proyecto}")
print(f"Material:        {material}")
print(f"Longitud:        {longitud_viga:>8.2f} m")
print()
print("-" * 70)
print(f"{'CARGAS Y ESFUERZOS':^70}")
print("-" * 70)
print(f"Carga aplicada:           {carga_aplicada:>12,.0f} N ({carga_aplicada/1000:>8.2f} kN)")
print(f"Área de sección:          {area_seccion:>12.4f} m²")
print(f"Esfuerzo calculado:       {esfuerzo_mpa:>12.2f} MPa")
print(f"Límite elástico material: {limite_elastico:>12.2f} MPa")
print()
print("-" * 70)
print(f"{'ANÁLISIS DE SEGURIDAD':^70}")
print("-" * 70)
print(f"Factor de seguridad:      {factor_seguridad:>12.2f}")
print()

if factor_seguridad >= 2.0:
    print(f"{'✓ ESTRUCTURA SEGURA':^70}")
elif factor_seguridad >= 1.5:
    print(f"{'⚠️ REVISAR DISEÑO':^70}")
else:
    print(f"{'✗ ESTRUCTURA INSEGURA':^70}")
print()
print("═" * 70)