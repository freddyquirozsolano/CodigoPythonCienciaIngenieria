paciente = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Lima'}

# Operador in
if 'nombre' in paciente:
    print(f"Nombre: {paciente['nombre']}")

if 'email' not in paciente:
    print('No hay email registrado')
