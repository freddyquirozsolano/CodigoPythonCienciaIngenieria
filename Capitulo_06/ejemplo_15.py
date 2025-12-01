# analizador_signos_vitales.py
# Sistema profesional de análisis de signos vitales

def mostrar_menu():
    print("\n" + "="*60)
    print("🏥 ANALIZADOR DE SIGNOS VITALES")
    print("="*60)
    print("1. Agregar lectura")
    print("2. Ver todas las lecturas")
    print("3. Calcular estadísticas")
    print("4. Detectar valores anormales")
    print("5. Generar reporte completo")
    print("6. Salir")

def agregar_lectura(lecturas):
    # Solicitar datos al usuario
    hora = input("Hora (HH:MM): ")
    fc = float(input("Frecuencia cardíaca (bpm): "))
    ps = float(input("Presión sistólica (mmHg): "))
    pd = float(input("Presión diastólica (mmHg): "))
    temp = float(input("Temperatura (°C): "))
    spo2 = float(input("SpO2 (%): "))
    
    # Crear tupla y agregar a la lista
    lectura = (hora, fc, ps, pd, temp, spo2)
    lecturas.append(lectura)
    print("✓ Lectura agregada exitosamente")

def calcular_estadisticas(lecturas):
    # Extraer datos usando list comprehensions
    fc_datos = [l[1] for l in lecturas]
    ps_datos = [l[2] for l in lecturas]
    temp_datos = [l[4] for l in lecturas]
    
    # Calcular estadísticas
    print(f"FC Promedio: {sum(fc_datos)/len(fc_datos):.1f} bpm")
    print(f"FC Máxima: {max(fc_datos):.0f} bpm")
    print(f"PA Promedio: {sum(ps_datos)/len(ps_datos):.0f} mmHg")

def detectar_anomalias(lecturas):
    # Filtrar usando list comprehensions
    taquicardia = [(h, fc) for h, fc, _, _, _, _ in lecturas if fc > 100]
    hipertension = [(h, ps) for h, _, ps, _, _, _ in lecturas if ps > 140]
    fiebre = [(h, t) for h, _, _, _, t, _ in lecturas if t > 37.5]
    
    if taquicardia:
        print(f"🔴 TAQUICARDIA: {len(taquicardia)} lecturas")
    if hipertension:
        print(f"🔴 HIPERTENSIÓN: {len(hipertension)} lecturas")

# Ejemplo de uso
lecturas = []
lecturas.append(("08:00", 72, 120, 80, 36.5, 98))
lecturas.append(("12:00", 105, 145, 92, 37.8, 96))
calcular_estadisticas(lecturas)
detectar_anomalias(lecturas)
