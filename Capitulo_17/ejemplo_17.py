import matplotlib.pyplot as plt
import numpy as np

# Análisis de viga simplemente apoyada
longitud = 10  # metros
carga = 5      # kN/m

x = np.linspace(0, longitud, 200)
R1 = R2 = (carga * longitud) / 2

# Diagramas
V = R1 - carga * x  # Fuerza cortante
M = R1 * x - (carga * x**2) / 2  # Momento flector

# Crear figura
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14, 12))
fig.suptitle('Análisis Estructural de Viga', fontsize=16, fontweight='bold')

# Diagrama de Fuerza Cortante
ax1.plot(x, V, 'b-', linewidth=2.5)
ax1.fill_between(x, 0, V, alpha=0.3, color='blue')
ax1.axhline(y=0, color='black', linewidth=0.8)
ax1.set_ylabel('Fuerza Cortante (kN)', fontweight='bold')
ax1.set_title('Diagrama de Fuerza Cortante (V)', fontweight='bold')
ax1.grid(True, alpha=0.3)

V_max = np.max(V)
V_min = np.min(V)
ax1.plot(x[np.argmax(V)], V_max, 'ro', markersize=10)
ax1.plot(x[np.argmin(V)], V_min, 'ro', markersize=10)

# Diagrama de Momento Flector
ax2.plot(x, M, 'r-', linewidth=2.5)
ax2.fill_between(x, 0, M, alpha=0.3, color='red')
ax2.axhline(y=0, color='black', linewidth=0.8)
ax2.set_ylabel('Momento Flector (kN·m)', fontweight='bold')
ax2.set_title('Diagrama de Momento Flector (M)', fontweight='bold')
ax2.grid(True, alpha=0.3)

M_max = np.max(M)
x_max = x[np.argmax(M)]
ax2.plot(x_max, M_max, 'go', markersize=12)
ax2.text(x_max, M_max + 5, f'M máx = {M_max:.2f} kN·m\nen x = {x_max:.2f} m', 
        ha='center', fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

# Diagrama de Deflexión (simplificado)
E = 200e9  # Módulo de elasticidad (Pa)
I = 1e-4   # Momento de inercia (m^4)
deflexion_max = (5 * carga * 1000 * longitud**4) / (384 * E * I)
deflexion = -(deflexion_max / (longitud/2)**4) * (x - longitud/2)**4 + deflexion_max
deflexion *= 1000  # convertir a mm

ax3.plot(x, -deflexion, 'purple', linewidth=2.5)
ax3.fill_between(x, 0, -deflexion, alpha=0.3, color='purple')
ax3.axhline(y=0, color='black', linewidth=0.8)
ax3.set_xlabel('Posición (m)', fontweight='bold')
ax3.set_ylabel('Deflexión (mm)', fontweight='bold')
ax3.set_title('Diagrama de Deflexión (δ)', fontweight='bold')
ax3.grid(True, alpha=0.3)
ax3.invert_yaxis()

plt.tight_layout()
plt.show()