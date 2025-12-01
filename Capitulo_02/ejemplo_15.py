# Verificando tipos de datos
edad = 25
temperatura = 36.5
nombre = "Ana"
esta_activo = True

print(type(edad))          # <class 'int'>
print(type(temperatura))   # <class 'float'>
print(type(nombre))        # <class 'str'>
print(type(esta_activo))   # <class 'bool'>

# Ejemplo práctico
valor = 42
if type(valor) == int:
    print("Es un número entero")