import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

# Simular métricas de sistema
horas = 24
tiempo = np.arange(0, horas)

cpu = 30 + 20 * np.sin(tiempo/3) + np.random.randn(horas) * 5
cpu = np.clip(cpu, 0, 100)

ram = 45 + 15 * np.sin(tiempo/4 + 1) + np.random.randn(horas) * 4
ram = np.clip(ram, 0, 100)

disco = 60 + np.linspace(0, 5, horas) + np.random.randn(horas) * 2
disco = np.clip(disco, 0, 100)

network = 50 + 30 * np.sin(tiempo/2) + np.random.randn(horas) * 10
network = np.clip(network, 0, 150)

# Crear dashboard
fig = plt.figure(figsize=(18, 12))
fig.suptitle('Dashboard de Monitoreo de Sistema - Últimas 24 Horas', 
            fontsize=18, fontweight='bold', y=0.98)

gs = GridSpec(2, 3, figure=fig, hspace=0.3, wspace=0.3)

# CPU Usage
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(tiempo, cpu, 'royalblue', linewidth=2)
ax1.fill_between(tiempo, 0, cpu, alpha=0.3, color='royalblue')
ax1.axhline(y=80, color='red', linestyle='--', alpha=0.5, label='Umbral')
ax1.set_ylabel('CPU (%)', fontweight='bold')
ax1.set_title('Uso de CPU', fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.legend()
ax1.set_ylim(0, 100)

cpu_actual = cpu[-1]
color_cpu = 'red' if cpu_actual > 80 else 'orange' if cpu_actual > 60 else 'green'
ax1.text(0.95, 0.95, f'{cpu_actual:.1f}%', 
        transform=ax1.transAxes, fontsize=14, fontweight='bold',
        va='top', ha='right', color=color_cpu)

# RAM Usage
ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(tiempo, ram, 'green', linewidth=2)
ax2.fill_between(tiempo, 0, ram, alpha=0.3, color='green')
ax2.axhline(y=80, color='red', linestyle='--', alpha=0.5)
ax2.set_ylabel('RAM (%)', fontweight='bold')
ax2.set_title('Uso de Memoria RAM', fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.set_ylim(0, 100)

ram_actual = ram[-1]
color_ram = 'red' if ram_actual > 80 else 'orange' if ram_actual > 60 else 'green'
ax2.text(0.95, 0.95, f'{ram_actual:.1f}%', 
        transform=ax2.transAxes, fontsize=14, fontweight='bold',
        va='top', ha='right', color=color_ram)

# Disco Usage (gauge)
ax3 = fig.add_subplot(gs[0, 2])
disco_actual = disco[-1]

theta = np.linspace(0, np.pi, 100)
r = np.ones(100)
ax3.fill_between(theta, 0, r, color='lightgray', alpha=0.3)

nivel = disco_actual / 100 * np.pi
ax3.fill_between(theta[theta <= nivel], 0, 1, 
                color='red' if disco_actual > 80 else 'orange' if disco_actual > 60 else 'green')

ax3.set_xlim(0, np.pi)
ax3.set_ylim(0, 1.2)
ax3.axis('off')
ax3.text(np.pi/2, 0.5, f'{disco_actual:.1f}%', 
        fontsize=20, fontweight='bold', ha='center', va='center')
ax3.set_title('Uso de Disco', fontweight='bold')

# Network Traffic
ax4 = fig.add_subplot(gs[1, :])
ax4.plot(tiempo, network, 'purple', linewidth=2.5, label='Tráfico de Red')
ax4.fill_between(tiempo, 0, network, alpha=0.2, color='purple')
ax4.set_xlabel('Tiempo (horas)', fontweight='bold')
ax4.set_ylabel('Tráfico (MB/s)', fontweight='bold')
ax4.set_title('Tráfico de Red', fontweight='bold')
ax4.grid(True, alpha=0.3)
ax4.legend()

plt.tight_layout()
plt.show()