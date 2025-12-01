import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Rectangle

# Waypoints de la trayectoria
waypoints = np.array([
    [0, 0], [2, 1], [4, 3], [5, 5], [7, 4],
    [9, 5], [10, 7], [8, 9], [6, 10], [4, 9], [2, 8], [1, 6]
])

# Interpolar para trayectoria suave
from scipy.interpolate import splprep, splev
tck, u = splprep([waypoints[:, 0], waypoints[:, 1]], s=0, k=3)
u_new = np.linspace(0, 1, 300)
traj_x, traj_y = splev(u_new, tck)

# Crear figura
fig = plt.figure(figsize=(16, 12))

# Subplot 1: Trayectoria 2D
ax1 = plt.subplot(2, 2, 1)
ax1.plot(traj_x, traj_y, 'b-', linewidth=3, alpha=0.7, label='Trayectoria')
ax1.scatter(waypoints[:, 0], waypoints[:, 1], c='red', s=200, 
           marker='o', edgecolors='darkred', linewidths=2, 
           label='Waypoints', zorder=5)

# Numerar waypoints
for i, (x, y) in enumerate(waypoints):
    ax1.text(x, y, str(i), ha='center', va='center', 
            fontsize=10, fontweight='bold', color='white', zorder=6)

# Posición actual del robot
pos_actual = len(traj_x) // 2
ax1.plot(traj_x[pos_actual], traj_y[pos_actual], 'go', 
        markersize=15, label='Robot', zorder=7)

# Obstáculos
obstaculo1 = Rectangle((3, 6), 2, 1.5, facecolor='gray', alpha=0.5, 
                       edgecolor='black', linewidth=2)
obstaculo2 = Circle((7, 2), 0.8, facecolor='gray', alpha=0.5, 
                   edgecolor='black', linewidth=2)
ax1.add_patch(obstaculo1)
ax1.add_patch(obstaculo2)

ax1.set_xlabel('Posición X (m)', fontsize=12, fontweight='bold')
ax1.set_ylabel('Posición Y (m)', fontsize=12, fontweight='bold')
ax1.set_title('Trayectoria del Robot Móvil', fontsize=14, fontweight='bold')
ax1.legend(loc='upper left')
ax1.grid(True, alpha=0.3)
ax1.set_aspect('equal')
ax1.set_xlim(-1, 11)
ax1.set_ylim(-1, 11)

# Subplot 2: Velocidad vs Tiempo
ax2 = plt.subplot(2, 2, 2)
tiempo = np.linspace(0, 30, len(traj_x))
dx = np.gradient(traj_x)
dy = np.gradient(traj_y)
velocidad = np.sqrt(dx**2 + dy**2) * 10

ax2.plot(tiempo, velocidad, 'purple', linewidth=2)
ax2.fill_between(tiempo, 0, velocidad, alpha=0.3, color='purple')
ax2.set_xlabel('Tiempo (s)', fontsize=12, fontweight='bold')
ax2.set_ylabel('Velocidad (m/s)', fontsize=12, fontweight='bold')
ax2.set_title('Perfil de Velocidad', fontsize=14, fontweight='bold')
ax2.grid(True, alpha=0.3)

vel_max = np.max(velocidad)
ax2.axhline(y=vel_max, color='red', linestyle='--', 
           label=f'Vel. Máx: {vel_max:.2f} m/s')
ax2.legend()

plt.tight_layout()
plt.show()