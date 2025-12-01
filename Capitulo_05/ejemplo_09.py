# Secuencia de movimiento de robot manipulador
print("=== SECUENCIA DE MOVIMIENTO DEL ROBOT ===\n")

# Posiciones objetivo para cada articulación (en grados)
secuencia = [
    [0, 0, 0, 0],      # Posición inicial
    [45, 30, 60, 0],   # Alcanzar objeto
    [45, 60, 90, 90],  # Levantar
    [90, 60, 90, 90],  # Girar
    [90, 30, 60, 90],  # Bajar
    [90, 30, 60, 0],   # Soltar
    [0, 0, 0, 0]       # Volver a posición inicial
]

nombres_articulaciones = ["Base", "Hombro", "Codo", "Muñeca"]

print("Ejecutando secuencia de movimiento...\n")

for paso, posiciones in enumerate(secuencia, 1):
    print(f"Paso {paso}:")
    
    for articulacion, angulo in enumerate(posiciones):
        nombre = nombres_articulaciones[articulacion]
        print(f"  {nombre}: {angulo}°")
    
    # Simular tiempo de movimiento
    print(f"  → Moviendo servomotores...")
    
    # Verificar límites
    for i, angulo in enumerate(posiciones):
        if angulo < 0 or angulo > 180:
            print(f"  ⚠️ ADVERTENCIA: Ángulo fuera de límites en {nombres_articulaciones[i]}")
    
    print()

print("✓ Secuencia completada exitosamente")