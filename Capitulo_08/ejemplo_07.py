# ASCII - Caracteres básicos (0-127)
letra = 'A'
codigo_ascii = ord(letra)  # Obtener código ASCII
print(codigo_ascii)  # 65

# Convertir código a carácter
caracter = chr(65)
print(caracter)  # 'A'

# UTF-8 - Soporte internacional
texto = "Temperatura: 25°C, España"

# Codificar a bytes
bytes_texto = texto.encode('utf-8')
print(bytes_texto)  # b'Temperatura: 25\xc2\xb0C, Espa\xc3\xb1a'

# Decodificar de bytes
texto_original = bytes_texto.decode('utf-8')
print(texto_original)  # 'Temperatura: 25°C, España'
