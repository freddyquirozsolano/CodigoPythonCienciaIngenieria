robot = {
    'modelo': 'RX-200',
    'velocidad_max': 2.5
}

# Agregar nueva clave-valor
robot['peso'] = 15.5  # kg
robot['sensores'] = ['ultrasonico', 'infrarrojo', 'camara']

# Modificar valor existente
robot['velocidad_max'] = 3.0  # Actualizar

print(robot)
# {'modelo': 'RX-200', 'velocidad_max': 3.0, 'peso': 15.5,
#  'sensores': ['ultrasonico', 'infrarrojo', 'camara']}

#Eliminar Elementos
config = {
    'host': 'localhost',
    'puerto': 8080,
    'debug': True,
    'timeout': 30
}

# del: eliminar por clave
del config['debug']

# pop(): eliminar y retornar valor
timeout_valor = config.pop('timeout')  # 30
print(timeout_valor)  # 30

# pop() con valor predeterminado
ssl = config.pop('ssl', False)  # False (no existía)

# popitem(): eliminar último par agregado (Python 3.7+)
ultimo = config.popitem()

# clear(): vaciar diccionario
config.clear()
print(config)  # {}
