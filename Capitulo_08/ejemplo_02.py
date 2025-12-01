# Cambiar mayúsculas/minúsculas
comando = "ACTIVAR MOTOR"

print(comando.lower())       # 'activar motor'
print(comando.upper())       # 'ACTIVAR MOTOR'
print(comando.capitalize())  # 'Activar motor'
print(comando.title())       # 'Activar Motor'
print(comando.swapcase())    # 'activar motor'

# strip() - eliminar espacios al inicio/final
dato = "  25.5  "
print(dato.strip())   # '25.5'
print(dato.lstrip())  # '25.5  ' (solo izquierda)
print(dato.rstrip())  # '  25.5' (solo derecha)

# replace() - reemplazar texto
mensaje = "Paciente en sala 101"
nuevo = mensaje.replace('101', '202')
print(nuevo)  # 'Paciente en sala 202'
