# Separador de miles con coma
poblacion = 1234567890
print(f"Población mundial: {poblacion:,}")  # 1,234,567,890

# Porcentajes
fraccion = 0.856
print(f"Porcentaje: {fraccion:.1%}")        # 85.6%

# Combinando formato
precio = 1234.5
print(f"Precio: ${precio:,.2f}")            # $1,234.50

# Sistema binario, octal, hexadecimal
numero = 42
print(f"Binario: {numero:b}")               # 101010
print(f"Octal: {numero:o}")                 # 52
print(f"Hexadecimal: {numero:x}")           # 2a
print(f"Hexadecimal (mayúsculas): {numero:X}")  # 2A