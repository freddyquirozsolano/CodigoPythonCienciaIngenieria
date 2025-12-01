import numpy as np

# Operaciones aritméticas básicas
temperaturas_c = np.array([20, 25, 30, 35, 40])

# Convertir a Fahrenheit
temperaturas_f = temperaturas_c * 9/5 + 32
print(temperaturas_f)  # [68.  77.  86.  95. 104.]

# Operaciones entre arrays
velocidades = np.array([1.5, 2.0, 2.5, 3.0])  # m/s
tiempos = np.array([10, 15, 20, 25])          # segundos
distancias = velocidades * tiempos
print(distancias)  # [15. 30. 50. 75.] metros
