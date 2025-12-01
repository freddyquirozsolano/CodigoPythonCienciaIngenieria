# simulador_tratamiento_medico.py
# Simulador de tratamiento con dosificación progresiva

import random

def simular_tratamiento():
    print("=" * 70)
    print("🏥 SIMULADOR DE TRATAMIENTO MÉDICO")
    print("=" * 70)
    print()
    
    # Parámetros del paciente
    nombre = input("Nombre del paciente: ")
    peso = float(input("Peso (kg): "))
    severidad_inicial = int(input("Severidad de la condición (1-10): "))
    
    # Parámetros del tratamiento
    dosis_por_kg = 5  # mg/kg
    dosis_diaria = peso * dosis_por_kg
    duracion_tratamiento = 10  # días
    
    print(f"\n{'='*70}")
    print("PLAN DE TRATAMIENTO")
    print(f"{'='*70}")
    print(f"Paciente: {nombre}")
    print(f"Peso: {peso} kg")
    print(f"Severidad inicial: {severidad_inicial}/10")
    print(f"Dosis diaria: {dosis_diaria:.1f} mg")
    print(f"Duración: {duracion_tratamiento} días")
    print(f"{'='*70}\n")
    
    # Simulación día por día
    severidad_actual = severidad_inicial
    dosis_acumulada = 0
    dias_completados = 0
    
    print("PROGRESO DEL TRATAMIENTO:\n")
    
    for dia in range(1, duracion_tratamiento + 1):
        print(f"DÍA {dia}:")
        print(f"{'─'*70}")
        
        # Administrar dosis
        print(f"  Administrando dosis: {dosis_diaria:.1f} mg")
        dosis_acumulada += dosis_diaria
        
        # Simular respuesta al tratamiento (con variabilidad aleatoria)
        mejora_base = 0.8  # Mejora esperada por día
        variabilidad = random.uniform(-0.2, 0.3)
        mejora_total = mejora_base + variabilidad
        
        severidad_anterior = severidad_actual
        severidad_actual = max(0, severidad_actual - mejora_total)
        
        # Reportar estado
        print(f"  Severidad: {severidad_anterior:.1f} → {severidad_actual:.1f}")
        
        # Calcular porcentaje de mejora
        mejora_porcentaje = ((severidad_inicial - severidad_actual) / severidad_inicial) * 100
        print(f"  Mejora acumulada: {mejora_porcentaje:.1f}%")
        print(f"  Dosis acumulada: {dosis_acumulada:.1f} mg")
        
        # Evaluación diaria
        if severidad_actual <= 0:
            print(f"  ✓ RECUPERACIÓN COMPLETA")
            dias_completados = dia
            print(f"\n{'='*70}")
            print("🎉 TRATAMIENTO EXITOSO - ALTA MÉDICA")
            print(f"{'='*70}")
            print(f"Recuperación en {dias_completados} días")
            print(f"Dosis total administrada: {dosis_acumulada:.1f} mg")
            break
        elif severidad_actual < 3:
            print(f"  ✓ Mejora significativa")
        elif severidad_actual < 6:
            print(f"  ⚠️ Mejora moderada")
        else:
            print(f"  ⚠️ Mejora lenta - monitoreo cercano")
        
        # Simular efectos secundarios aleatorios
        if random.random() < 0.1:  # 10% de probabilidad
            print(f"  ⚠️ Efecto secundario leve detectado")
        
        print()
        dias_completados = dia
    
    else:
        # Si completamos todos los días sin recuperación total
        print(f"{'='*70}")
        print("TRATAMIENTO COMPLETADO")
        print(f"{'='*70}")
        print(f"Severidad final: {severidad_actual:.1f}/10")
        print(f"Mejora total: {((severidad_inicial - severidad_actual) / severidad_inicial) * 100:.1f}%")
        
        if severidad_actual < 2:
            print("✓ Tratamiento exitoso - Seguimiento ambulatorio")
        else:
            print("⚠️ Se requiere tratamiento adicional o ajuste de dosis")
    
    # Resumen final
    print(f"\nDosis total administrada: {dosis_acumulada:.1f} mg")
    print(f"Días de tratamiento: {dias_completados}")
    
    # Generar reporte
    print(f"\n{'='*70}")
    print("GENERAR REPORTE DETALLADO")
    print(f"{'='*70}")
    
    generar = input("¿Generar reporte para archivo? (s/n): ").lower()
    
    if generar == 's':
        nombre_archivo = f"reporte_{nombre.replace(' ', '_')}.txt"
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(f"REPORTE DE TRATAMIENTO MÉDICO\n")
            archivo.write(f"{'='*70}\n\n")
            archivo.write(f"Paciente: {nombre}\n")
            archivo.write(f"Peso: {peso} kg\n")
            archivo.write(f"Severidad inicial: {severidad_inicial}/10\n")
            archivo.write(f"Severidad final: {severidad_actual:.1f}/10\n")
            archivo.write(f"Días de tratamiento: {dias_completados}\n")
            archivo.write(f"Dosis total: {dosis_acumulada:.1f} mg\n")
            archivo.write(f"Mejora: {((severidad_inicial - severidad_actual) / severidad_inicial) * 100:.1f}%\n")
        
        print(f"✓ Reporte guardado en: {nombre_archivo}")

# Ejecutar el simulador
if __name__ == "__main__":
    simular_tratamiento()