from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Crear malla
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Graficar superficie
surf = ax.plot_surface(X, Y, Z, cmap='coolwarm', alpha=0.8,
                       linewidth=0, antialiased=True)

ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_zlabel('Z', fontsize=12)
ax.set_title('Función 3D: sin(√(x² + y²))', fontsize=14, fontweight='bold')
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

plt.show()