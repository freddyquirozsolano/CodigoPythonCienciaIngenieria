# Ejemplo de LEGB
x = "global"  # Scope global

def externa():
    x = "enclosing"  # Scope enclosing
    
    def interna():
        x = "local"  # Scope local
        print(f"Dentro de interna: {x}")
    
    interna()
    print(f"Dentro de externa: {x}")

externa()
print(f"Global: {x}")

# Salida:
# Dentro de interna: local
# Dentro de externa: enclosing
# Global: global