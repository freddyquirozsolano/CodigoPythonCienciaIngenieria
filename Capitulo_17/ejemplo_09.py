import matplotlib.pyplot as plt
import numpy as np

# Datos: distribución normal
datos = np.random.normal(100, 15, 1000)  # media=100, std=15, 1000 muestras

plt.figure(figsize=(10, 6))
plt.hist(datos, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel('Valor', fontsize=12)
plt.ylabel('Frecuencia', fontsize=12)
plt.title('Distribución de Datos', fontsize=14)
plt.grid(axis='y', alpha=0.3)

# Agregar línea de media
media = np.mean(datos)
plt.axvline(media, color='red', linestyle='--', linewidth=2, label=f'Media: {media:.2f}')
plt.legend()

plt.tight_layout()
plt.show()