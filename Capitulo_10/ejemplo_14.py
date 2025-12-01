# Archivo: main.py
# Diferentes formas de importar desde paquetes

# Forma 1: Importar módulo completo
import ingenieria.biomedica.signos_vitales as sv

imc = sv.calcular_imc(70, 1.75)
print(f"IMC: {imc:.2f}")

# Forma 2: Importar función específica
from ingenieria.biomedica.signos_vitales import calcular_fcm

fcm = calcular_fcm(30)
print(f"FCM: {fcm} bpm")

# Forma 3: Importar desde __init__.py
import ingenieria

# Si __init__.py importó los módulos, puedes usar:
# resultado = ingenieria.signos_vitales.calcular_imc(70, 1.75)

# Forma 4: Importar todo el subpaquete
from ingenieria import biomedica

# Ahora puedes usar:
# biomedica.signos_vitales.calcular_imc(70, 1.75)