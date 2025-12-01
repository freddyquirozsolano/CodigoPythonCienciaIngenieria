def registrar_paciente(nombre, edad, ciudad="Desconocida", seguro=False):
    """Registra información de un paciente"""
    print(f"Paciente: {nombre}")
    print(f"Edad: {edad} años")
    print(f"Ciudad: {ciudad}")
    print(f"Seguro médico: {'Sí' if seguro else 'No'}")
    print("-" * 40)

# Argumentos posicionales (deben ir en orden)
registrar_paciente("Ana García", 30)

# Argumentos con nombre (keyword arguments)
registrar_paciente(nombre="Carlos Ruiz", edad=45, ciudad="Lima", seguro=True)

# Mezclar ambos (posicionales primero, luego keywords)
registrar_paciente("María López", 28, ciudad="Bogotá")

# También puedes cambiar el orden con keywords
registrar_paciente(edad=35, nombre="Pedro Sánchez", seguro=True)