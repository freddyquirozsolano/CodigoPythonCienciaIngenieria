# generador_reportes.py
# Sistema de generación de reportes profesionales

import json
from datetime import datetime

def crear_encabezado(titulo, ancho=70):
    """Crea un encabezado formateado para el reporte"""
    linea = "=" * ancho
    return f"{linea}\n{titulo:^{ancho}}\n{linea}\n"

def crear_seccion(titulo, ancho=70):
    """Crea una sección del reporte"""
    linea = "-" * ancho
    return f"\n{linea}\n{titulo:^{ancho}}\n{linea}\n"

def guardar_reporte(nombre_archivo, contenido):
    """Guarda el reporte en un archivo"""
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)
    print(f"✓ Reporte guardado: {nombre_archivo}")

# ==================== REPORTE BIOMÉDICO ====================
def generar_reporte_biomedico():
    print("\n=== GENERADOR DE REPORTE BIOMÉDICO ===\n")
    
    # Solicitar datos
    nombre = input("Nombre del paciente: ")
    edad = int(input("Edad: "))
    tipo_sangre = input("Tipo de sangre: ")
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    temperatura = float(input("Temperatura (°C): "))
    presion_s = int(input("Presión sistólica (mmHg): "))
    presion_d = int(input("Presión diastólica (mmHg): "))
    fc = int(input("Frecuencia cardíaca (bpm): "))
    
    # Calcular IMC
    imc = peso / (altura ** 2)
    
    # Determinar clasificaciones
    if imc < 18.5:
        cat_imc = "Bajo peso"
    elif imc < 25:
        cat_imc = "Normal"
    elif imc < 30:
        cat_imc = "Sobrepeso"
    else:
        cat_imc = "Obesidad"
    
    alertas = []
    if temperatura > 37.5:
        alertas.append("⚠️ Temperatura elevada")
    if presion_s > 140 or presion_d > 90:
        alertas.append("⚠️ Presión arterial elevada")
    if fc > 100:
        alertas.append("⚠️ Taquicardia")
    if fc < 60:
        alertas.append("⚠️ Bradicardia")
    
    # Generar reporte
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    reporte = crear_encabezado("REPORTE MÉDICO")
    reporte += f"Fecha: {fecha}\n"
    reporte += f"Generado por: Sistema de Registro Médico\n\n"
    
    reporte += crear_seccion("DATOS DEL PACIENTE")
    reporte += f"Nombre: {nombre}\n"
    reporte += f"Edad: {edad} años\n"
    reporte += f"Tipo de sangre: {tipo_sangre}\n"
    reporte += f"Peso: {peso:.1f} kg\n"
    reporte += f"Altura: {altura:.2f} m\n"
    reporte += f"IMC: {imc:.2f} ({cat_imc})\n"
    
    reporte += crear_seccion("SIGNOS VITALES")
    reporte += f"Temperatura:         {temperatura:>6.1f}°C\n"
    reporte += f"Presión arterial:    {presion_s:>3}/{presion_d:<3} mmHg\n"
    reporte += f"Frecuencia cardíaca: {fc:>6} bpm\n"
    
    if alertas:
        reporte += crear_seccion("ALERTAS")
        for alerta in alertas:
            reporte += f"{alerta}\n"
    else:
        reporte += "\n✓ Todos los signos vitales dentro de rangos normales\n"
    
    reporte += "\n" + "=" * 70 + "\n"
    
    # Guardar reporte
    nombre_archivo = f"reporte_medico_{nombre.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.txt"
    guardar_reporte(nombre_archivo, reporte)
    
    # Mostrar en pantalla
    print("\n" + reporte)
    
    return nombre_archivo

# ==================== REPORTE DE MECATRÓNICA ====================
def generar_reporte_mecatronica():
    print("\n=== GENERADOR DE REPORTE DE ROBOT ===\n")
    
    # Solicitar datos
    nombre_robot = input("Nombre del robot: ")
    tiempo_operacion = float(input("Tiempo de operación (horas): "))
    distancia = float(input("Distancia recorrida (m): "))
    velocidad_prom = float(input("Velocidad promedio (m/s): "))
    velocidad_max = float(input("Velocidad máxima (m/s): "))
    bateria_inicial = float(input("Batería inicial (V): "))
    bateria_final = float(input("Batería final (V): "))
    temp_max = float(input("Temperatura máxima (°C): "))
    colisiones = int(input("Número de colisiones: "))
    
    # Calcular estadísticas
    consumo_bateria = bateria_inicial - bateria_final
    porcentaje_bateria = (bateria_final / bateria_inicial) * 100
    velocidad_promedio_kmh = velocidad_prom * 3.6
    distancia_km = distancia / 1000
    consumo_por_km = (consumo_bateria / distancia_km) if distancia_km > 0 else 0
    
    # Generar reporte
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    reporte = crear_encabezado("REPORTE DE OPERACIÓN - ROBÓTICA")
    reporte += f"Fecha: {fecha}\n"
    reporte += f"Robot: {nombre_robot}\n\n"
    
    reporte += crear_seccion("ESTADÍSTICAS DE MOVIMIENTO")
    reporte += f"Tiempo de operación:    {tiempo_operacion:>8.2f} horas\n"
    reporte += f"Distancia recorrida:    {distancia:>10,.1f} m ({distancia_km:.3f} km)\n"
    reporte += f"Velocidad promedio:     {velocidad_prom:>10.2f} m/s ({velocidad_promedio_kmh:.2f} km/h)\n"
    reporte += f"Velocidad máxima:       {velocidad_max:>10.2f} m/s\n"
    
    reporte += crear_seccion("CONSUMO ENERGÉTICO")
    reporte += f"Batería inicial:        {bateria_inicial:>10.2f} V\n"
    reporte += f"Batería final:          {bateria_final:>10.2f} V ({porcentaje_bateria:.1f}%)\n"
    reporte += f"Consumo total:          {consumo_bateria:>10.2f} V\n"
    reporte += f"Consumo por kilómetro:  {consumo_por_km:>10.3f} V/km\n"
    
    reporte += crear_seccion("CONDICIONES OPERATIVAS")
    reporte += f"Temperatura máxima:     {temp_max:>10.1f}°C\n"
    reporte += f"Colisiones detectadas:  {colisiones:>10}\n"
    
    # Análisis y recomendaciones
    reporte += crear_seccion("ANÁLISIS")
    
    if porcentaje_bateria < 20:
        reporte += "⚠️ Batería baja - Recarga requerida\n"
    
    if temp_max > 60:
        reporte += "⚠️ Temperatura elevada - Revisar sistema de enfriamiento\n"
    
    if colisiones > 5:
        reporte += "⚠️ Múltiples colisiones - Revisar sensores\n"
    
    if porcentaje_bateria >= 20 and temp_max <= 60 and colisiones <= 5:
        reporte += "✓ Operación dentro de parámetros normales\n"
    
    reporte += "\n" + "=" * 70 + "\n"
    
    # Guardar reporte
    nombre_archivo = f"reporte_robot_{nombre_robot.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
    guardar_reporte(nombre_archivo, reporte)
    
    print("\n" + reporte)
    
    return nombre_archivo

# ==================== REPORTE DE SISTEMAS ====================
def generar_reporte_sistemas():
    print("\n=== GENERADOR DE REPORTE DE SISTEMA ===\n")
    
    # Solicitar datos
    nombre_sistema = input("Nombre del sistema: ")
    usuario = input("Usuario: ")
    tiempo_activo = float(input("Tiempo activo (horas): "))
    procesos = int(input("Procesos ejecutados: "))
    datos_procesados = float(input("Datos procesados (GB): "))
    cpu_prom = float(input("CPU promedio (%): "))
    cpu_max = float(input("CPU máximo (%): "))
    memoria_prom = float(input("Memoria promedio (GB): "))
    memoria_max = float(input("Memoria máxima (GB): "))
    errores = int(input("Errores detectados: "))
    
    # Calcular estadísticas
    procesos_por_hora = procesos / tiempo_activo if tiempo_activo > 0 else 0
    datos_por_hora = datos_procesados / tiempo_activo if tiempo_activo > 0 else 0
    
    # Generar reporte
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    reporte = crear_encabezado("REPORTE DE RENDIMIENTO DEL SISTEMA")
    reporte += f"Fecha: {fecha}\n"
    reporte += f"Sistema: {nombre_sistema}\n"
    reporte += f"Usuario: {usuario}\n\n"
    
    reporte += crear_seccion("ACTIVIDAD DEL SISTEMA")
    reporte += f"Tiempo activo:          {tiempo_activo:>10.2f} horas\n"
    reporte += f"Procesos ejecutados:    {procesos:>10,}\n"
    reporte += f"Tasa de procesos:       {procesos_por_hora:>10.1f} procesos/hora\n"
    reporte += f"Datos procesados:       {datos_procesados:>10.2f} GB\n"
    reporte += f"Tasa de datos:          {datos_por_hora:>10.2f} GB/hora\n"
    
    reporte += crear_seccion("UTILIZACIÓN DE RECURSOS")
    reporte += f"CPU promedio:           {cpu_prom:>10.1f}%\n"
    reporte += f"CPU máximo:             {cpu_max:>10.1f}%\n"
    reporte += f"Memoria promedio:       {memoria_prom:>10.2f} GB\n"
    reporte += f"Memoria máxima:         {memoria_max:>10.2f} GB\n"
    
    reporte += crear_seccion("CONFIABILIDAD")
    reporte += f"Errores detectados:     {errores:>10}\n"
    
    if errores == 0:
        tasa_exito = 100.0
    else:
        tasa_exito = ((procesos - errores) / procesos) * 100
    
    reporte += f"Tasa de éxito:          {tasa_exito:>10.1f}%\n"
    
    # Análisis
    reporte += crear_seccion("ANÁLISIS DE RENDIMIENTO")
    
    if cpu_max > 90:
        reporte += "⚠️ CPU sobrecargado - Considerar optimización\n"
    
    if memoria_max > 14:  # Asumiendo 16GB total
        reporte += "⚠️ Uso de memoria alto - Verificar fugas de memoria\n"
    
    if errores > procesos * 0.05:  # Más del 5% de errores
        reporte += "⚠️ Alta tasa de errores - Revisar logs del sistema\n"
    
    if cpu_max <= 90 and memoria_max <= 14 and errores <= procesos * 0.05:
        reporte += "✓ Sistema operando eficientemente\n"
    
    reporte += "\n" + "=" * 70 + "\n"
    
    # Guardar reporte
    nombre_archivo = f"reporte_sistema_{nombre_sistema.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
    guardar_reporte(nombre_archivo, reporte)
    
    print("\n" + reporte)
    
    return nombre_archivo

# ==================== REPORTE DE INGENIERÍA ====================
def generar_reporte_ingenieria():
    print("\n=== GENERADOR DE REPORTE DE INGENIERÍA ===\n")
    
    # Solicitar datos
    proyecto = input("Nombre del proyecto: ")
    material = input("Material utilizado: ")
    longitud = float(input("Longitud del elemento (m): "))
    area = float(input("Área de sección transversal (m²): "))
    carga = float(input("Carga aplicada (kN): "))
    modulo = float(input("Módulo de elasticidad (GPa): "))
    limite_elastico = float(input("Límite elástico del material (MPa): "))
    
    # Convertir unidades
    carga_n = carga * 1000
    modulo_pa = modulo * 1e9
    
    # Calcular esfuerzos
    esfuerzo = carga_n / area
    esfuerzo_mpa = esfuerzo / 1e6
    deformacion = esfuerzo / modulo_pa
    deformacion_porcentaje = deformacion * 100
    elongacion = deformacion * longitud
    factor_seguridad = limite_elastico / esfuerzo_mpa
    
    # Generar reporte
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    reporte = crear_encabezado("REPORTE DE ANÁLISIS ESTRUCTURAL")
    reporte += f"Fecha: {fecha}\n"
    reporte += f"Proyecto: {proyecto}\n"
    reporte += f"Ingeniero: Sistema de Análisis Automatizado\n\n"
    
    reporte += crear_seccion("ESPECIFICACIONES DEL ELEMENTO")
    reporte += f"Material:               {material}\n"
    reporte += f"Longitud:               {longitud:>12.3f} m\n"
    reporte += f"Área de sección:        {area:>12.6f} m²\n"
    reporte += f"Módulo de elasticidad:  {modulo:>12.1f} GPa\n"
    reporte += f"Límite elástico:        {limite_elastico:>12.1f} MPa\n"
    
    reporte += crear_seccion("CARGAS Y ESFUERZOS")
    reporte += f"Carga aplicada:         {carga:>12.2f} kN ({carga_n:>12,.0f} N)\n"
    reporte += f"Esfuerzo normal:        {esfuerzo_mpa:>12.2f} MPa\n"
    reporte += f"Deformación unitaria:   {deformacion:.6f} ({deformacion_porcentaje:.4f}%)\n"
    reporte += f"Elongación total:       {elongacion*1000:>12.3f} mm\n"
    
    reporte += crear_seccion("ANÁLISIS DE SEGURIDAD")
    reporte += f"Factor de seguridad:    {factor_seguridad:>12.2f}\n"
    
    # Evaluación
    if factor_seguridad >= 2.5:
        reporte += "\nEvaluación: ✓ DISEÑO MUY SEGURO\n"
    elif factor_seguridad >= 2.0:
        reporte += "\nEvaluación: ✓ DISEÑO SEGURO\n"
    elif factor_seguridad >= 1.5:
        reporte += "\nEvaluación: ⚠️ DISEÑO ACEPTABLE - Revisar condiciones de carga\n"
    else:
        reporte += "\nEvaluación: ✗ DISEÑO INSEGURO - Redimensionar elemento\n"
    
    # Recomendaciones
    reporte += crear_seccion("RECOMENDACIONES")
    
    if factor_seguridad < 2.0:
        area_requerida = (carga_n * 2.0) / (limite_elastico * 1e6)
        reporte += f"• Se recomienda aumentar el área de sección a {area_requerida:.6f} m²\n"
        reporte += f"  para alcanzar un factor de seguridad de 2.0\n"
    
    if esfuerzo_mpa > limite_elastico * 0.8:
        reporte += f"• El esfuerzo está cerca del límite elástico ({esfuerzo_mpa/limite_elastico*100:.1f}%)\n"
        reporte += f"  Considerar un material con mayor resistencia\n"
    
    if deformacion_porcentaje > 0.5:
        reporte += f"• Deformación significativa ({deformacion_porcentaje:.3f}%)\n"
        reporte += f"  Verificar requisitos de rigidez\n"
    
    reporte += "\n" + "=" * 70 + "\n"
    
    # Guardar reporte
    nombre_archivo = f"reporte_ingenieria_{proyecto.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
    guardar_reporte(nombre_archivo, reporte)
    
    print("\n" + reporte)
    
    return nombre_archivo

# ==================== MENÚ PRINCIPAL ====================
def menu_principal():
    print("=" * 70)
    print("🌟 GENERADOR DE REPORTES PROFESIONALES")
    print("=" * 70)
    print()
    print("Selecciona el tipo de reporte:")
    print("1. 🏥 Reporte Biomédico")
    print("2. 🤖 Reporte de Mecatrónica/Robótica")
    print("3. 💻 Reporte de Sistemas")
    print("4. 🔧 Reporte de Ingeniería")
    print("5. Salir")
    print()
    
    opcion = input("Ingresa tu opción: ")
    
    if opcion == "1":
        generar_reporte_biomedico()
    elif opcion == "2":
        generar_reporte_mecatronica()
    elif opcion == "3":
        generar_reporte_sistemas()
    elif opcion == "4":
        generar_reporte_ingenieria()
    elif opcion == "5":
        print("\n¡Hasta luego!")
        return False
    else:
        print("\n⚠️ Opción no válida")
    
    return True

# Ejecutar el programa
if __name__ == "__main__":
    continuar = True
    while continuar:
        continuar = menu_principal()
        if continuar:
            input("\nPresiona Enter para continuar...")
            print("\n" * 2)