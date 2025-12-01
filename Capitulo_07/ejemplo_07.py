sensores = {'temp', 'presion', 'humedad'}

# Agregar elemento
sensores.add('luz')
print(sensores)  # {'temp', 'presion', 'humedad', 'luz'}

# Agregar múltiples elementos
sensores.update(['sonido', 'movimiento'])

# Eliminar elemento
sensores.remove('temp')  # Error si no existe
sensores.discard('temp')  # No genera error si no existe

# Verificar pertenencia
if 'presion' in sensores:
    print('Sensor de presión disponible')
