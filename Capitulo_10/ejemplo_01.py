# Forma 1: Importar el módulo completo
import math

resultado = math.sqrt(16)  # Usar con nombre del módulo
print(resultado)  # 4.0
print(math.pi)  # 3.141592653589793

# Forma 2: Importar con alias (nombre más corto)
import math as m

resultado = m.sqrt(25)
print(resultado)  # 5.0

# Forma 3: Importar elementos específicos
from math import sqrt, pi

resultado = sqrt(36)  # Usar directamente sin prefijo
print(resultado)  # 6.0
print(pi)  # 3.141592653589793

# Forma 4: Importar todo (NO RECOMENDADO)
from math import *

# Ahora todas las funciones están disponibles directamente
resultado = cos(0)  # Puede causar conflictos de nombres