import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
tiempo = np.linspace(0, 10, 100)
señal = np.sin(tiempo)

# Crear gráfico
plt.figure(figsize=(10, 6))
plt.plot(tiempo, señal)
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Señal Sinusoidal')
plt.grid(True)
plt.show()