# sistema_diagnostico_medico.py
# Sistema experto para diagnóstico preliminar

def sistema_diagnostico():
    print("=" * 70)
    print("🏥 SISTEMA EXPERTO DE DIAGNÓSTICO MÉDICO PRELIMINAR")
    print("=" * 70)
    print()
    print("⚠️ ADVERTENCIA: Este es un sistema educativo para demostración.")
    print("   NO reemplaza la consulta con un profesional médico.")
    print()
    
    # Recolección de síntomas
    print("Por favor, responda las siguientes preguntas:\n")
    
    nombre = input("Nombre del paciente: ")
    edad = int(input("Edad: "))
    
    print("\nSÍNTOMAS (responda s/n):")
    fiebre = input("¿Tiene fiebre (>37.5°C)? ").lower() == 's'
    if fiebre:
        temp = float(input("  Temperatura (°C): "))
    else:
        temp = 36.5
    
    tos = input("¿Tiene tos? ").lower() == 's'
    if tos:
        tipo_tos = input("  ¿Tos seca (s) o con flema (n)? ").lower() == 's'
    else:
        tipo_tos = False
    
    dolor_garganta = input("¿Tiene dolor de garganta? ").lower() == 's'
    dolor_cabeza = input("¿Tiene dolor de cabeza? ").lower() == 's'
    congestion_nasal = input("¿Tiene congestión nasal? ").lower() == 's'
    dificultad_respirar = input("¿Tiene dificultad para respirar? ").lower() == 's'
    dolor_pecho = input("¿Tiene dolor en el pecho? ").lower() == 's'
    nauseas = input("¿Tiene náuseas o vómito? ").lower() == 's'
    dolor_abdominal = input("¿Tiene dolor abdominal? ").lower() == 's'
    diarrea = input("¿Tiene diarrea? ").lower() == 's'
    fatiga = input("¿Tiene fatiga extrema? ").lower() == 's'
    
    dias_sintomas = int(input("\n¿Cuántos días con síntomas? "))
    
    # Análisis de diagnóstico
    print("\n" + "=" * 70)
    print("ANÁLISIS DE SÍNTOMAS")
    print("=" * 70)
    
    diagnostico_posible = []
    recomendacion = []
    urgencia = "BAJA"
    
    # Reglas de diagnóstico
    
    # Regla 1: Emergencia respiratoria
    if dificultad_respirar or dolor_pecho:
        diagnostico_posible.append("EMERGENCIA RESPIRATORIA O CARDÍACA")
        recomendacion.append("🚨 BUSCAR ATENCIÓN MÉDICA INMEDIATA")
        recomendacion.append("   Llamar al 911 o acudir a emergencias")
        urgencia = "CRÍTICA"
    
    # Regla 2: Resfriado común
    elif congestion_nasal and (dolor_garganta or dolor_cabeza) and not fiebre:
        diagnostico_posible.append("Posible RESFRIADO COMÚN")
        recomendacion.append("• Descanso adecuado")
        recomendacion.append("• Hidratación abundante")
        recomendacion.append("• Analgésicos de venta libre si es necesario")
        if dias_sintomas > 7:
            recomendacion.append("• Consultar médico si síntomas persisten")
            urgencia = "MEDIA"
    
    # Regla 3: Gripe
    elif fiebre and (dolor_cabeza or fatiga) and (tos or dolor_garganta):
        if temp > 38.5:
            diagnostico_posible.append("Posible INFLUENZA (GRIPE)")
            urgencia = "ALTA"
        else:
            diagnostico_posible.append("Posible GRIPE LEVE")
            urgencia = "MEDIA"
        
        recomendacion.append("• Reposo en cama")
        recomendacion.append("• Antipiréticos para la fiebre")
        recomendacion.append("• Líquidos abundantes")
        recomendacion.append("• Evitar contacto con otras personas")
        
        if edad > 60 or dias_sintomas > 5:
            recomendacion.append("• CONSULTAR MÉDICO")
            urgencia = "ALTA"
    
    # Regla 4: Infección respiratoria
    elif tos and fiebre and tipo_tos:
        diagnostico_posible.append("Posible INFECCIÓN RESPIRATORIA")
        recomendacion.append("• Consultar médico para evaluación")
        recomendacion.append("• Puede requerir antibióticos")
        recomendacion.append("• Mantener hidratación")
        urgencia = "ALTA"
    
    # Regla 5: Gastroenteritis
    elif (nauseas or diarrea) and dolor_abdominal:
        diagnostico_posible.append("Posible GASTROENTERITIS")
        if fiebre:
            urgencia = "MEDIA"
            recomendacion.append("• Hidratación oral constante")
            recomendacion.append("• Dieta blanda")
            recomendacion.append("• Consultar médico si síntomas empeoran")
        else:
            urgencia = "BAJA"
            recomendacion.append("• Hidratación oral")
            recomendacion.append("• Dieta blanda")
        
        if dias_sintomas > 3:
            recomendacion.append("• Consultar médico")
            urgencia = "MEDIA"
    
    # Regla 6: Síntomas leves inespecíficos
    elif dolor_cabeza or fatiga:
        diagnostico_posible.append("SÍNTOMAS LEVES INESPECÍFICOS")
        recomendacion.append("• Descanso")
        recomendacion.append("• Hidratación")
        recomendacion.append("• Monitorear evolución")
        if dias_sintomas > 5:
            recomendacion.append("• Consultar médico si persiste")
            urgencia = "MEDIA"
    
    # Sin diagnóstico claro
    else:
        diagnostico_posible.append("EVALUACIÓN INCONCLUSA")
        recomendacion.append("• Consultar con médico para evaluación completa")
        urgencia = "MEDIA"
    
    # Generar reporte
    print(f"\nPaciente: {nombre}, {edad} años")
    print(f"Días con síntomas: {dias_sintomas}")
    print()
    
    # Mostrar síntomas activos
    sintomas_activos = []
    if fiebre:
        sintomas_activos.append(f"Fiebre ({temp}°C)")
    if tos:
        sintomas_activos.append("Tos" + (" seca" if tipo_tos else " con flema"))
    if dolor_garganta:
        sintomas_activos.append("Dolor de garganta")
    if dolor_cabeza:
        sintomas_activos.append("Dolor de cabeza")
    if congestion_nasal:
        sintomas_activos.append("Congestión nasal")
    if nauseas:
        sintomas_activos.append("Náuseas/vómito")
    if dolor_abdominal:
        sintomas_activos.append("Dolor abdominal")
    if diarrea:
        sintomas_activos.append("Diarrea")
    if fatiga:
        sintomas_activos.append("Fatiga")
    
    print("Síntomas presentes:")
    for sintoma in sintomas_activos:
        print(f"  • {sintoma}")
    
    print()
    print("-" * 70)
    
    # Nivel de urgencia
    if urgencia == "CRÍTICA":
        print("🔴 NIVEL DE URGENCIA: CRÍTICA")
    elif urgencia == "ALTA":
        print("🟠 NIVEL DE URGENCIA: ALTA")
    elif urgencia == "MEDIA":
        print("🟡 NIVEL DE URGENCIA: MEDIA")
    else:
        print("🟢 NIVEL DE URGENCIA: BAJA")
    
    print()
    print("DIAGNÓSTICO PRELIMINAR:")
    for diag in diagnostico_posible:
        print(f"  {diag}")
    
    print()
    print("RECOMENDACIONES:")
    for rec in recomendacion:
        print(f"  {rec}")
    
    print()
    print("=" * 70)
    print("⚠️ RECORDATORIO: Este diagnóstico es preliminar y educativo.")
    print("   Siempre consulte con un profesional médico calificado.")
    print("=" * 70)

# Ejecutar el sistema
if __name__ == "__main__":
    sistema_diagnostico()