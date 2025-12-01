# Archivo: demo_modulo.py
"""Módulo de demostración"""

def saludar(nombre):
    return f"Hola, {nombre}!"

# Este código solo se ejecuta si ejecutas este archivo directamente
if __name__ == "__main__":
    print("Ejecutando demo_modulo.py directamente")
    print(saludar("María"))
else:
    print("demo_modulo.py fue importado como módulo")

# Comportamiento:
# Si ejecutas: python demo_modulo.py
#   Salida: Ejecutando demo_modulo.py directamente
#           Hola, María!

# Si importas: import demo_modulo
#   Salida: demo_modulo.py fue importado como módulo