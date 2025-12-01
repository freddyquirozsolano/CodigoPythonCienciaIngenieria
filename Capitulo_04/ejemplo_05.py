# Sistema de control de calidad
esfuerzo_calculado = 235  # MPa
limite_elastico = 250  # MPa
factor_seguridad = limite_elastico / esfuerzo_calculado
deformacion = 0.0045  # porcentaje

print("=== SISTEMA DE CONTROL DE CALIDAD ===\n")

if factor_seguridad < 1.5:
    print("🚨 CRÍTICO: Factor de seguridad insuficiente")
    print(f"   Factor de seguridad: {factor_seguridad:.2f}")
    print("   Acción: Rediseño requerido")

if esfuerzo_calculado > limite_elastico * 0.9:
    print("⚠️ ADVERTENCIA: Esfuerzo cerca del límite")
    print(f"   Esfuerzo: {esfuerzo_calculado} MPa")
    print(f"   Límite: {limite_elastico} MPa")

if deformacion > 0.004:
    print("⚠️ ADVERTENCIA: Deformación excesiva")
    print(f"   Deformación: {deformacion*100:.2f}%")
    print("   Acción: Verificar especificaciones")