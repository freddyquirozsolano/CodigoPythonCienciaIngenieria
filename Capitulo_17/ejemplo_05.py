import matplotlib.pyplot as plt
import numpy as np

# Datos: rendimiento de diferentes sensores
sensores = ['Temp', 'Presión', 'Humedad', 'Luz', 'Sonido']
precisión = [98.5, 95.2, 97.8, 92.3, 89.7]

plt.figure(figsize=(10, 6))
plt.bar(sensores, precisión, color='steelblue', edgecolor='black', alpha=0.7)
plt.xlabel('Tipo de Sensor', fontsize=12)
plt.ylabel('Precisión (%)', fontsize=12)
plt.title('Precisión de Sensores', fontsize=14, fontweight='bold')
plt.ylim(85, 100)
plt.grid(axis='y', alpha=0.3)

# Agregar valores sobre las barras
for i, v in enumerate(precisión):
    plt.text(i, v + 0.5, f'{v:.1f}%', ha='center', fontweight='bold')

plt.tight_layout()
plt.show()