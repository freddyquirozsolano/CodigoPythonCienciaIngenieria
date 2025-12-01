# analizador_materiales.py

def agregar_prueba(pruebas):
    material = input("Material: ")
    resistencia = float(input("Resistencia (MPa): "))
    elasticidad = float(input("Módulo de elasticidad (GPa): "))
    densidad = float(input("Densidad (kg/m³): "))
    
    prueba = (material, resistencia, elasticidad, densidad)
    pruebas.append(prueba)

def analizar_materiales(pruebas):
    # Calcular ratio resistencia/peso
    ratios = [(m, r/d) for m, r, _, d in pruebas]
    
    # Encontrar mejor material
    mejor = max(ratios, key=lambda x: x[1])
    
    print(f"Mejor relación resistencia/peso:")
    print(f"Material: {mejor[0]}")
    print(f"Ratio: {mejor[1]:.4f}")

# Ejemplo
pruebas = [
    ("Acero", 250, 200, 7850),
    ("Aluminio", 310, 69, 2700),
    ("Titanio", 900, 114, 4430)
]
analizar_materiales(pruebas)
