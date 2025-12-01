# Convertir a entero
numero_str = "42"
numero_int = int(numero_str)    # "42" → 42
flotante = 3.14
entero = int(flotante)           # 3.14 → 3 (pierde decimales)

# Convertir a float
entero = 42
flotante = float(entero)         # 42 → 42.0
texto = "3.14"
numero = float(texto)            # "3.14" → 3.14

# Convertir a string
edad = 25
edad_str = str(edad)             # 25 → "25"
pi = 3.14159
pi_str = str(pi)                 # 3.14159 → "3.14159"

# Convertir a booleano
numero = 1
es_verdadero = bool(numero)      # 1 → True
cero = 0
es_falso = bool(cero)            # 0 → False