# Archivo: programa_principal.py
import biomedicas

# Usar las funciones del módulo
peso = 70
altura = 1.75

imc = biomedicas.calcular_imc(peso, altura)
clasificacion = biomedicas.clasificar_imc(imc)

print(f"Peso: {peso} kg")
print(f"Altura: {altura} m")
print(f"IMC: {imc:.2f}")
print(f"Clasificación: {clasificacion}")
print(f"\nMódulo versión: {biomedicas.VERSION}")

# También puedes importar funciones específicas
from biomedicas import calcular_fcm

edad = 30
fcm = calcular_fcm(edad)
print(f"\nEdad: {edad} años")
print(f"Frecuencia cardíaca máxima: {fcm} bpm")