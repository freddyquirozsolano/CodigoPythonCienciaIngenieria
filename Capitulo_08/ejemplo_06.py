import re

# Validar email
def validar_email(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(patron, email))

print(validar_email('juan@ejemplo.com'))  # True
print(validar_email('invalido'))          # False

# Extraer números de teléfono
texto = "Contacto: 555-1234 o 555-5678"
telefonos = re.findall(r'\d{3}-\d{4}', texto)
print(telefonos)  # ['555-1234', '555-5678']

# Validar formato de presión arterial
def validar_presion(presion):
    patron = r'^\d{2,3}/\d{2,3}$'
    return bool(re.match(patron, presion))

print(validar_presion('120/80'))   # True
print(validar_presion('120-80'))   # False
