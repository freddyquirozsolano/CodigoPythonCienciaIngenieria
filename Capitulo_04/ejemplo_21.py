# Sistema de clasificación de pacientes en emergencias
print("=== SISTEMA DE TRIAJE HOSPITALARIO ===\n")

# Signos vitales
presion_sistolica = int(input("Presión sistólica (mmHg): "))
frecuencia_cardiaca = int(input("Frecuencia cardíaca (bpm): "))
frecuencia_respiratoria = int(input("Frecuencia respiratoria (rpm): "))
temperatura = float(input("Temperatura (°C): "))
nivel_conciencia = input("Nivel de conciencia (alerta/confuso/inconsciente): ").lower()
dolor = int(input("Nivel de dolor (0-10): "))

print("\n" + "=" * 60)
print("EVALUACIÓN DE PRIORIDAD")
print("=" * 60)

# Categoría 1: Resucitación (Rojo) - Inmediato
if nivel_conciencia == "inconsciente":
    categoria = "CATEGORÍA 1: RESUCITACIÓN"
    color = "🔴"
    tiempo_espera = "INMEDIATO"
    accion = "Atención médica urgente - Sala de trauma"
elif presion_sistolica < 90 or frecuencia_cardiaca > 130 or frecuencia_respiratoria > 30:
    categoria = "CATEGORÍA 1: RESUCITACIÓN"
    color = "🔴"
    tiempo_espera = "INMEDIATO"
    accion = "Signos vitales críticos - Intervención inmediata"

# Categoría 2: Emergencia (Naranja) - 10 minutos
elif dolor >= 8:
    categoria = "CATEGORÍA 2: EMERGENCIA"
    color = "🟠"
    tiempo_espera = "10 minutos"
    accion = "Dolor severo - Evaluación prioritaria"
elif temperatura > 39.5 or temperatura < 35:
    categoria = "CATEGORÍA 2: EMERGENCIA"
    color = "🟠"
    tiempo_espera = "10 minutos"
    accion = "Temperatura crítica - Atención rápida"
elif presion_sistolica > 180 or frecuencia_cardiaca > 120:
    categoria = "CATEGORÍA 2: EMERGENCIA"
    color = "🟠"
    tiempo_espera = "10 minutos"
    accion = "Signos vitales alterados - Evaluación pronta"

# Categoría 3: Urgencia (Amarillo) - 30 minutos
elif dolor >= 5:
    categoria = "CATEGORÍA 3: URGENCIA"
    color = "🟡"
    tiempo_espera = "30 minutos"
    accion = "Dolor moderado - Evaluación oportuna"
elif temperatura > 38.5:
    categoria = "CATEGORÍA 3: URGENCIA"
    color = "🟡"
    tiempo_espera = "30 minutos"
    accion = "Fiebre - Evaluación necesaria"
elif nivel_conciencia == "confuso":
    categoria = "CATEGORÍA 3: URGENCIA"
    color = "🟡"
    tiempo_espera = "30 minutos"
    accion = "Alteración de conciencia - Evaluación"

# Categoría 4: Menor urgencia (Verde) - 60 minutos
elif dolor >= 3:
    categoria = "CATEGORÍA 4: MENOR URGENCIA"
    color = "🟢"
    tiempo_espera = "60 minutos"
    accion = "Dolor leve - Evaluación programada"
elif temperatura > 37.5:
    categoria = "CATEGORÍA 4: MENOR URGENCIA"
    color = "🟢"
    tiempo_espera = "60 minutos"
    accion = "Fiebre leve - Evaluación de rutina"

# Categoría 5: No urgente (Azul) - 120 minutos
else:
    categoria = "CATEGORÍA 5: NO URGENTE"
    color = "🔵"
    tiempo_espera = "120 minutos"
    accion = "Condición estable - Consulta general"

print(f"{color} {categoria}")
print(f"Tiempo de espera máximo: {tiempo_espera}")
print(f"Acción: {accion}")
print("=" * 60)