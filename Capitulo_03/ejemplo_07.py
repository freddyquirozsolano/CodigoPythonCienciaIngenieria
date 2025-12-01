# Alineación: < (izquierda), > (derecha), ^ (centro)
nombre = "Python"

print(f"{nombre:<15}")    # Python          (izquierda, 15 caracteres)
print(f"{nombre:>15}")    #         Python  (derecha, 15 caracteres)
print(f"{nombre:^15}")    #     Python      (centro, 15 caracteres)

# Con relleno personalizado
print(f"{nombre:*<15}")   # Python*********
print(f"{nombre:->15}")   # ---------Python
print(f"{nombre:=^15}")   # ====Python=====

# Alineación de números
numero = 42
print(f"{numero:>10}")    #         42
print(f"{numero:0>10}")   # 0000000042 (relleno con ceros)

# Crear tablas alineadas
print(f"{'Nombre':<15} {'Edad':>5} {'Peso':>6}")
print(f"{'Juan':<15} {25:>5} {70.5:>6.1f}")
print(f"{'María':<15} {30:>5} {65.0:>6.1f}")