import matplotlib.pyplot as plt
import numpy as np

# Datos: relación entre dos variables
x = np.random.randn(100)
y = 2 * x + np.random.randn(100) * 0.5

plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.6, s=50, color='royalblue', edgecolors='black')
plt.xlabel('Variable X', fontsize=12)
plt.ylabel('Variable Y', fontsize=12)
plt.title('Gráfico de Dispersión: Relación entre X e Y', fontsize=14)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()