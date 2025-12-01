# Programa: Configuración de servomotor
print("=== CONFIGURACIÓN DE SERVOMOTOR ===")
print()

# Obtener parámetros
numero_servo = int(input("Número de servomotor (1-8): "))
angulo_objetivo = int(input("Ángulo objetivo (0-180°): "))
velocidad = float(input("Velocidad de movimiento (°/s): "))
activar = input("¿Activar servomotor? (S/N): ").upper()

# Convertir respuesta a booleano
servo_activo = (activar == "S")

# Calcular tiempo estimado
angulo_actual = 90  # Posición inicial típica
diferencia_angulo = abs(angulo_objetivo - angulo_actual)
tiempo_estimado = diferencia_angulo / velocidad

# Mostrar configuración
print("\n=== CONFIGURACIÓN CONFIRMADA ===")
print(f"Servo #{numero_servo}")
print(f"Ángulo objetivo: {angulo_objetivo}°")
print(f"Velocidad: {velocidad}°/s")
print(f"Tiempo estimado: {tiempo_estimado:.2f} segundos")
print(f"Estado: {'ACTIVO' if servo_activo else 'INACTIVO'}")