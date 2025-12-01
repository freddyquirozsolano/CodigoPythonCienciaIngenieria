# Sistema de evaluación de diseño estructural
print("=== EVALUADOR DE DISEÑO ESTRUCTURAL ===\n")

esfuerzo = float(input("Esfuerzo calculado (MPa): "))
limite_elastico = float(input("Límite elástico del material (MPa): "))

factor_seguridad = limite_elastico / esfuerzo

print(f"\nFactor de seguridad calculado: {factor_seguridad:.2f}")
print("=" * 60)

if factor_seguridad < 1.0:
    evaluacion = "FALLO ESTRUCTURAL"
    color = "🔴"
    estado = "RECHAZADO"
    descripcion = "El diseño fallará bajo la carga especificada"
    accion = "REDISEÑO COMPLETO REQUERIDO"
    urgencia = "CRÍTICO"
elif factor_seguridad < 1.5:
    evaluacion = "INSUFICIENTE"
    color = "🟠"
    estado = "RECHAZADO"
    descripcion = "Factor de seguridad por debajo del mínimo aceptable"
    accion = "Aumentar sección transversal o cambiar material"
    urgencia = "ALTO"
elif factor_seguridad < 2.0:
    evaluacion = "MARGINAL"
    color = "🟡"
    estado = "REVISAR"
    descripcion = "Cumple requisitos mínimos pero sin margen"
    accion = "Recomendar optimización del diseño"
    urgencia = "MEDIO"
elif factor_seguridad < 3.0:
    evaluacion = "ACEPTABLE"
    color = "🟢"
    estado = "APROBADO"
    descripcion = "Diseño seguro con margen adecuado"
    accion = "Proceder con fabricación"
    urgencia = "NINGUNO"
elif factor_seguridad < 5.0:
    evaluacion = "BUENO"
    color = "🟢"
    estado = "APROBADO"
    descripcion = "Diseño muy seguro con buen margen"
    accion = "Diseño óptimo, proceder"
    urgencia = "NINGUNO"
else:
    evaluacion = "SOBREDIMENSIONADO"
    color = "🔵"
    estado = "OPTIMIZAR"
    descripcion = "Diseño excesivamente conservador"
    accion = "Considerar reducir dimensiones para optimizar costos"
    urgencia = "BAJO"

print(f"{color} Evaluación: {evaluacion}")
print(f"Estado: {estado}")
print(f"Urgencia: {urgencia}")
print()
print(f"Descripción: {descripcion}")
print(f"Acción recomendada: {accion}")
print()
print(f"Esfuerzo aplicado: {esfuerzo:.2f} MPa")
print(f"Límite elástico: {limite_elastico:.2f} MPa")
print(f"Margen de seguridad: {(factor_seguridad - 1) * 100:.1f}%")
print("=" * 60)