# sistema_conversion_universal.py
# Sistema de Conversión para Ciencias e Ingeniería

import math

print("=" * 70)
print("🌟 SISTEMA DE CONVERSIÓN UNIVERSAL")
print("=" * 70)
print()

# Menú principal
print("Selecciona tu área de especialización:")
print("1. 🏥 Biomédica - Conversiones médicas")
print("2. 🤖 Mecatrónica - Conversiones de robótica")
print("3. 💻 Sistemas - Conversiones de computación")
print("4. 🔧 Ingeniería - Conversiones de ingeniería")
print()

area = input("Ingresa el número de tu área: ")

if area == "1":
    # ==================== BIOMÉDICA ====================
    print("\n" + "=" * 70)
    print("🏥 CONVERSIONES BIOMÉDICAS")
    print("=" * 70)
    print()
    print("1. Calcular IMC (Índice de Masa Corporal)")
    print("2. Convertir temperatura (°C ↔ °F)")
    print("3. Convertir presión arterial (mmHg ↔ kPa)")
    print("4. Calcular dosis de medicamento por peso")
    print("5. Calcular frecuencia cardíaca objetivo")
    print()
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        print("\n--- Cálculo de IMC ---")
        peso = float(input("Peso (kg): "))
        altura = float(input("Altura (m): "))
        
        imc = peso / (altura ** 2)
        
        print(f"\nIMC: {imc:.2f}")
        
        if imc < 18.5:
            clasificacion = "Bajo peso"
        elif imc < 25:
            clasificacion = "Peso normal"
        elif imc < 30:
            clasificacion = "Sobrepeso"
        else:
            clasificacion = "Obesidad"
        
        print(f"Clasificación: {clasificacion}")
    
    elif opcion == "2":
        print("\n--- Conversión de Temperatura ---")
        tipo = input("¿Convertir de (C)elsius o (F)ahrenheit? ").upper()
        
        if tipo == "C":
            celsius = float(input("Temperatura en °C: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C = {fahrenheit:.2f}°F")
        else:
            fahrenheit = float(input("Temperatura en °F: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F = {celsius:.2f}°C")
    
    elif opcion == "3":
        print("\n--- Conversión de Presión Arterial ---")
        tipo = input("¿Convertir de (M)mHg o (K)Pa? ").upper()
        
        if tipo == "M":
            mmhg = float(input("Presión en mmHg: "))
            kpa = mmhg * 0.133322
            print(f"{mmhg} mmHg = {kpa:.2f} kPa")
        else:
            kpa = float(input("Presión en kPa: "))
            mmhg = kpa / 0.133322
            print(f"{kpa} kPa = {mmhg:.2f} mmHg")
    
    elif opcion == "4":
        print("\n--- Cálculo de Dosis de Medicamento ---")
        peso = float(input("Peso del paciente (kg): "))
        dosis_kg = float(input("Dosis recomendada (mg/kg): "))
        
        dosis_total = peso * dosis_kg
        
        print(f"\nDosis total recomendada: {dosis_total:.2f} mg")
    
    elif opcion == "5":
        print("\n--- Frecuencia Cardíaca Objetivo ---")
        edad = int(input("Edad del paciente: "))
        
        fcm = 220 - edad
        fc_min = fcm * 0.6
        fc_max = fcm * 0.8
        
        print(f"\nFrecuencia cardíaca máxima: {fcm} bpm")
        print(f"Zona de ejercicio moderado (60-80%): {fc_min:.0f}-{fc_max:.0f} bpm")

elif area == "2":
    # ==================== MECATRÓNICA ====================
    print("\n" + "=" * 70)
    print("🤖 CONVERSIONES DE MECATRÓNICA")
    print("=" * 70)
    print()
    print("1. Convertir ángulos (Grados ↔ Radianes)")
    print("2. Convertir velocidad angular (RPM ↔ rad/s)")
    print("3. Calcular torque")
    print("4. Convertir pulsos de encoder a distancia")
    print("5. Calcular relación de transmisión")
    print()
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        print("\n--- Conversión de Ángulos ---")
        tipo = input("¿Convertir de (G)rados o (R)adianes? ").upper()
        
        if tipo == "G":
            grados = float(input("Ángulo en grados: "))
            radianes = grados * math.pi / 180
            print(f"{grados}° = {radianes:.4f} radianes")
        else:
            radianes = float(input("Ángulo en radianes: "))
            grados = radianes * 180 / math.pi
            print(f"{radianes} rad = {grados:.4f}°")
    
    elif opcion == "2":
        print("\n--- Conversión de Velocidad Angular ---")
        tipo = input("¿Convertir de (R)PM o rad/s (S)? ").upper()
        
        if tipo == "R":
            rpm = float(input("Velocidad en RPM: "))
            rad_s = (rpm * 2 * math.pi) / 60
            print(f"{rpm} RPM = {rad_s:.4f} rad/s")
        else:
            rad_s = float(input("Velocidad en rad/s: "))
            rpm = (rad_s * 60) / (2 * math.pi)
            print(f"{rad_s} rad/s = {rpm:.2f} RPM")
    
    elif opcion == "3":
        print("\n--- Cálculo de Torque ---")
        fuerza = float(input("Fuerza aplicada (N): "))
        distancia = float(input("Distancia al eje de rotación (m): "))
        
        torque = fuerza * distancia
        
        print(f"\nTorque: {torque:.2f} N·m")
    
    elif opcion == "4":
        print("\n--- Pulsos de Encoder a Distancia ---")
        pulsos = int(input("Pulsos contados: "))
        ppr = int(input("Pulsos por revolución del encoder: "))
        diametro_cm = float(input("Diámetro de la rueda (cm): "))
        
        revoluciones = pulsos / ppr
        perimetro_cm = math.pi * diametro_cm
        distancia_cm = revoluciones * perimetro_cm
        distancia_m = distancia_cm / 100
        
        print(f"\nDistancia recorrida: {distancia_cm:.2f} cm ({distancia_m:.2f} m)")
    
    elif opcion == "5":
        print("\n--- Relación de Transmisión ---")
        dientes_conducido = int(input("Dientes del engranaje conducido: "))
        dientes_conductor = int(input("Dientes del engranaje conductor: "))
        
        relacion = dientes_conducido / dientes_conductor
        
        print(f"\nRelación de transmisión: {relacion:.2f}:1")
        print(f"Por cada vuelta del motor, el eje de salida da {1/relacion:.2f} vueltas")

elif area == "3":
    # ==================== SISTEMAS ====================
    print("\n" + "=" * 70)
    print("💻 CONVERSIONES DE SISTEMAS")
    print("=" * 70)
    print()
    print("1. Convertir unidades de almacenamiento")
    print("2. Calcular tiempo de transferencia")
    print("3. Convertir sistemas numéricos (Decimal ↔ Binario)")
    print("4. Calcular direcciones IP disponibles")
    print("5. Convertir unidades de velocidad de red")
    print()
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        print("\n--- Conversión de Almacenamiento ---")
        print("Convertir desde:")
        print("1. Bytes")
        print("2. KB")
        print("3. MB")
        print("4. GB")
        print("5. TB")
        
        desde = input("Opción: ")
        valor = float(input("Valor a convertir: "))
        
        # Convertir todo a bytes primero
        if desde == "1":
            bytes_total = valor
        elif desde == "2":
            bytes_total = valor * 1024
        elif desde == "3":
            bytes_total = valor * 1024 ** 2
        elif desde == "4":
            bytes_total = valor * 1024 ** 3
        elif desde == "5":
            bytes_total = valor * 1024 ** 4
        
        # Convertir a todas las unidades
        kb = bytes_total / 1024
        mb = kb / 1024
        gb = mb / 1024
        tb = gb / 1024
        
        print(f"\nResultado:")
        print(f"{bytes_total:.0f} Bytes")
        print(f"{kb:.2f} KB")
        print(f"{mb:.2f} MB")
        print(f"{gb:.2f} GB")
        print(f"{tb:.4f} TB")
    
    elif opcion == "2":
        print("\n--- Tiempo de Transferencia ---")
        tamaño_mb = float(input("Tamaño del archivo (MB): "))
        velocidad_mbps = float(input("Velocidad de conexión (Mbps): "))
        
        tiempo_segundos = (tamaño_mb * 8) / velocidad_mbps
        tiempo_minutos = tiempo_segundos / 60
        tiempo_horas = tiempo_minutos / 60
        
        print(f"\nTiempo de transferencia:")
        print(f"{tiempo_segundos:.2f} segundos")
        print(f"{tiempo_minutos:.2f} minutos")
        print(f"{tiempo_horas:.4f} horas")
    
    elif opcion == "3":
        print("\n--- Conversión de Sistemas Numéricos ---")
        tipo = input("¿Convertir desde (D)ecimal o (B)inario? ").upper()
        
        if tipo == "D":
            decimal = int(input("Número decimal: "))
            binario = bin(decimal)[2:]  # [2:] elimina el prefijo '0b'
            octal = oct(decimal)[2:]
            hexadecimal = hex(decimal)[2:]
            
            print(f"\nDecimal: {decimal}")
            print(f"Binario: {binario}")
            print(f"Octal: {octal}")
            print(f"Hexadecimal: {hexadecimal}")
        else:
            binario = input("Número binario: ")
            decimal = int(binario, 2)
            octal = oct(decimal)[2:]
            hexadecimal = hex(decimal)[2:]
            
            print(f"\nBinario: {binario}")
            print(f"Decimal: {decimal}")
            print(f"Octal: {octal}")
            print(f"Hexadecimal: {hexadecimal}")
    
    elif opcion == "4":
        print("\n--- Direcciones IP Disponibles ---")
        mascara = int(input("Máscara de subred (ej. 24 para /24): "))
        
        hosts = (2 ** (32 - mascara)) - 2
        
        print(f"\nDirecciones IP disponibles: {hosts}")
        print(f"Dirección de red: 1")
        print(f"Dirección de broadcast: 1")
        print(f"Hosts utilizables: {hosts}")
    
    elif opcion == "5":
        print("\n--- Velocidad de Red ---")
        tipo = input("¿Convertir desde (M)bps o M(B)ps? ").upper()
        
        if tipo == "M":
            mbps = float(input("Velocidad en Mbps (megabits): "))
            mbytes = mbps / 8
            kbps = mbps * 1000
            kbytes = mbytes * 1000
            
            print(f"\n{mbps} Mbps =")
            print(f"{mbytes:.2f} MB/s (megabytes por segundo)")
            print(f"{kbps:.0f} Kbps (kilobits por segundo)")
            print(f"{kbytes:.2f} KB/s (kilobytes por segundo)")
        else:
            mbytes = float(input("Velocidad en MB/s (megabytes): "))
            mbps = mbytes * 8
            kbps = mbps * 1000
            kbytes = mbytes * 1000
            
            print(f"\n{mbytes} MB/s =")
            print(f"{mbps:.2f} Mbps (megabits por segundo)")
            print(f"{kbps:.0f} Kbps (kilobits por segundo)")
            print(f"{kbytes:.2f} KB/s (kilobytes por segundo)")

elif area == "4":
    # ==================== INGENIERÍA ====================
    print("\n" + "=" * 70)
    print("🔧 CONVERSIONES DE INGENIERÍA")
    print("=" * 70)
    print()
    print("1. Convertir unidades de fuerza (N ↔ kgf ↔ lbf)")
    print("2. Convertir unidades de presión (Pa ↔ bar ↔ PSI)")
    print("3. Convertir unidades de energía (J ↔ kWh ↔ cal)")
    print("4. Calcular fuerza (Segunda Ley de Newton)")
    print("5. Calcular densidad")
    print()
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        print("\n--- Conversión de Fuerza ---")
        print("Convertir desde:")
        print("1. Newtons (N)")
        print("2. Kilogramos-fuerza (kgf)")
        print("3. Libras-fuerza (lbf)")
        
        desde = input("Opción: ")
        valor = float(input("Valor a convertir: "))
        
        # Convertir a Newtons primero
        if desde == "1":
            newtons = valor
        elif desde == "2":
            newtons = valor * 9.80665
        elif desde == "3":
            newtons = valor * 4.44822
        
        # Convertir a todas las unidades
        kgf = newtons / 9.80665
        lbf = newtons / 4.44822
        
        print(f"\nResultado:")
        print(f"{newtons:.2f} N (Newtons)")
        print(f"{kgf:.2f} kgf (Kilogramos-fuerza)")
        print(f"{lbf:.2f} lbf (Libras-fuerza)")
    
    elif opcion == "2":
        print("\n--- Conversión de Presión ---")
        print("Convertir desde:")
        print("1. Pascales (Pa)")
        print("2. Bar")
        print("3. PSI")
        print("4. Atmósferas (atm)")
        
        desde = input("Opción: ")
        valor = float(input("Valor a convertir: "))
        
        # Convertir a Pascales primero
        if desde == "1":
            pascales = valor
        elif desde == "2":
            pascales = valor * 100000
        elif desde == "3":
            pascales = valor * 6894.76
        elif desde == "4":
            pascales = valor * 101325
        
        # Convertir a todas las unidades
        bar = pascales / 100000
        psi = pascales / 6894.76
        atm = pascales / 101325
        kpa = pascales / 1000
        
        print(f"\nResultado:")
        print(f"{pascales:.2f} Pa (Pascales)")
        print(f"{kpa:.2f} kPa (Kilopascales)")
        print(f"{bar:.4f} bar")
        print(f"{psi:.2f} PSI")
        print(f"{atm:.4f} atm (Atmósferas)")
    
    elif opcion == "3":
        print("\n--- Conversión de Energía ---")
        print("Convertir desde:")
        print("1. Joules (J)")
        print("2. Kilovatios-hora (kWh)")
        print("3. Calorías (cal)")
        
        desde = input("Opción: ")
        valor = float(input("Valor a convertir: "))
        
        # Convertir a Joules primero
        if desde == "1":
            joules = valor
        elif desde == "2":
            joules = valor * 3600000
        elif desde == "3":
            joules = valor * 4.184
        
        # Convertir a todas las unidades
        kwh = joules / 3600000
        cal = joules / 4.184
        kcal = cal / 1000
        
        print(f"\nResultado:")
        print(f"{joules:.2f} J (Joules)")
        print(f"{kwh:.6f} kWh (Kilovatios-hora)")
        print(f"{cal:.2f} cal (Calorías)")
        print(f"{kcal:.2f} kcal (Kilocalorías)")
    
    elif opcion == "4":
        print("\n--- Cálculo de Fuerza (F = m × a) ---")
        masa = float(input("Masa (kg): "))
        aceleracion = float(input("Aceleración (m/s²): "))
        
        fuerza_n = masa * aceleracion
        fuerza_kgf = fuerza_n / 9.80665
        
        print(f"\nFuerza: {fuerza_n:.2f} N")
        print(f"Fuerza: {fuerza_kgf:.2f} kgf")
    
    elif opcion == "5":
        print("\n--- Cálculo de Densidad (ρ = m / V) ---")
        masa = float(input("Masa (kg): "))
        volumen = float(input("Volumen (m³): "))
        
        densidad = masa / volumen
        densidad_g_cm3 = densidad / 1000
        
        print(f"\nDensidad: {densidad:.2f} kg/m³")
        print(f"Densidad: {densidad_g_cm3:.3f} g/cm³")

else:
    print("\nOpción no válida")

print("\n" + "=" * 70)
print("¡Gracias por usar el Sistema de Conversión Universal!")
print("=" * 70)