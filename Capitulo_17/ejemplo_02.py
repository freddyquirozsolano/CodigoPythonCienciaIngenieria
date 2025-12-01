import matplotlib.pyplot as plt
import numpy as np

# Datos
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 2, 4, 6, 8, 10])

# Crear el gráfico
plt.plot(x, y)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Mi Primer Gráfico')
plt.grid(True)

# Mostrar el gráfico
plt.show()