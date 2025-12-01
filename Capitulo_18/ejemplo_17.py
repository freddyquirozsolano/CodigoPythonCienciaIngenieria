# Análisis de ingeniería con SciPy
import numpy as np
from scipy import optimize, integrate, signal, interpolate
import matplotlib.pyplot as plt

print("=== OPTIMIZACIÓN ===")
# Encontrar mínimo de función
def costo_produccion(x):
    """Función de costo: C(x) = x^2 - 10x + 25"""
    return x**2 - 10*x + 25

resultado = optimize.minimize_scalar(costo_produccion)
print(f"Producción óptima: {resultado.x:.2f} unidades")
print(f"Costo mínimo: ${resultado.fun:.2f}")

print("\n=== INTEGRACIÓN NUMÉRICA ===")
# Calcular área bajo la curva
def fuerza(t):
    """Fuerza variable en el tiempo"""
    return 100 * np.sin(t) + 50

trabajo, error = integrate.quad(fuerza, 0, np.pi)
print(f"Trabajo realizado: {trabajo:.2f} J")

print("\n=== INTERPOLACIÓN ===")
# Datos experimentales de resistencia vs temperatura
temps = np.array([0, 25, 50, 75, 100])
resistencias = np.array([100, 110, 125, 145, 170])

# Crear función de interpolación
f_interp = interpolate.interp1d(temps, resistencias, kind='cubic')

# Predecir resistencia a 37°C
temp_nueva = 37
resist_predicha = f_interp(temp_nueva)
print(f"Resistencia a {temp_nueva}°C: {resist_predicha:.2f} Ω")

print("\n=== PROCESAMIENTO DE SEÑALES ===")
# Filtro paso-bajo para eliminar ruido
t = np.linspace(0, 1, 1000)
señal_limpia = np.sin(2 * np.pi * 5 * t)  # 5 Hz
ruido = 0.5 * np.sin(2 * np.pi * 50 * t)  # 50 Hz
señal_ruidosa = señal_limpia + ruido

# Diseñar filtro Butterworth
orden = 4
frecuencia_corte = 10  # Hz
frecuencia_muestreo = 1000
b, a = signal.butter(orden, frecuencia_corte, 
                     fs=frecuencia_muestreo, btype='low')

# Aplicar filtro
señal_filtrada = signal.filtfilt(b, a, señal_ruidosa)

print(f"Señal procesada con filtro de orden {orden}")
print(f"Frecuencia de corte: {frecuencia_corte} Hz")