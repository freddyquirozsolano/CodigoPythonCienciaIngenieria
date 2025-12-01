from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Datos: espiral 3D
t = np.linspace(0, 20, 1000)
x = np.sin(t)
y = np.cos(t)
z = t

ax.plot(x, y, z, 'b-', linewidth=2)
ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_zlabel('Z', fontsize=12)
ax.set_title('Espiral 3D', fontsize=14, fontweight='bold')

plt.show()