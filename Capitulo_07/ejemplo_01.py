# Diccionario vacío
mi_diccionario = {}
# O usando dict()
otro_diccionario = dict()

# Diccionario con datos
paciente = {
    'nombre': 'María López',
    'edad': 45,
    'tipo_sangre': 'O+',
    'diabetico': False
}

# Diccionario con diferentes tipos de claves
mixto = {
    'texto': 'valor',
    42: 'número como clave',
    (1, 2): 'tupla como clave'
}

# Imprimir los diccionarios
print("Diccionario vacío:", mi_diccionario)
print("Diccionario con datos:", paciente)
print("Diccionario con diferentes tipos de claves:", mixto)