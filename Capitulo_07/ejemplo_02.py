paciente = {
    'nombre': 'María López',
    'edad': 45,
    'tipo_sangre': 'O+'
}

# Acceder por clave
nombre = paciente['nombre']  # 'María López'
edad = paciente['edad']  # 45
print(nombre, edad)

# Método get() - más seguro
nombre = paciente.get('nombre')  # 'María López'
altura = paciente.get('altura', 'No disponible')  # 'No disponible'
print(nombre, altura)