sensores = ["temperatura", "presión"]

# append(): agregar al final
sensores.append("humedad")
print(sensores)  # ['temperatura', 'presión', 'humedad']

# insert(): agregar en posición específica
sensores.insert(1, "velocidad")  # Insertar en índice 1
print(sensores)  # ['temperatura', 'velocidad', 'presión', 'humedad']

# extend(): agregar múltiples elementos
sensores.extend(["luz", "sonido"])
print(sensores)  # ['temperatura', 'velocidad', 'presión', 'humedad', 'luz', 'sonido']
