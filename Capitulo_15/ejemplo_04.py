import numpy as np

angulos_grados = np.array([0, 30, 45, 60, 90])
angulos_rad = np.radians(angulos_grados)

# Funciones trigonométricas
senos = np.sin(angulos_rad)
cosenos = np.cos(angulos_rad)
tangentes = np.tan(angulos_rad)

# Funciones exponenciales y logarítmicas
datos = np.array([1, 2, 3, 4, 5])
exp_datos = np.exp(datos)      # e^x
log_datos = np.log(datos)      # ln(x)
sqrt_datos = np.sqrt(datos)    # √x

print("Ángulos (grados):", angulos_grados)
print("Senos:", senos)
print("Cosenos:", cosenos)
print("Tangentes:", tangentes)
print("Datos originales:", datos)
print("Exponenciales:", exp_datos)
print("Logaritmos:", log_datos)
print("Raíces cuadradas:", sqrt_datos)
