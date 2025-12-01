# Función con un parámetro
def saludar_persona(nombre):
    """Saluda a una persona específica por su nombre"""
    print(f"¡Hola, {nombre}! Bienvenido/a.")

# Llamar la función con diferentes argumentos
saludar_persona("María")  # ¡Hola, María! Bienvenido/a.
saludar_persona("Juan")   # ¡Hola, Juan! Bienvenido/a.
saludar_persona("Ana")    # ¡Hola, Ana! Bienvenido/a.

# Función con múltiples parámetros
def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal.
    
    Parámetros:
        peso: Peso en kilogramos (float)
        altura: Altura en metros (float)
    """
    imc = peso / (altura ** 2)
    print(f"IMC: {imc:.2f}")

# Llamar con diferentes valores
calcular_imc(70, 1.75)  # IMC: 22.86
calcular_imc(85, 1.80)  # IMC: 26.23
calcular_imc(60, 1.65)  # IMC: 22.04