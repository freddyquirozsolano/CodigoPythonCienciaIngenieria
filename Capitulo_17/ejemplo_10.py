import matplotlib.pyplot as plt
import numpy as np

# Datos
x = np.linspace(0, 10, 100)

# Crear figura con 2x2 subplots
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Subplot 1: Línea
axs[0, 0].plot(x, np.sin(x), 'b-')
axs[0, 0].set_title('Señal Sinusoidal')
axs[0, 0].grid(True, alpha=0.3)

# Subplot 2: Coseno
axs[0, 1].plot(x, np.cos(x), 'r-')
axs[0, 1].set_title('Señal Cosenoidal')
axs[0, 1].grid(True, alpha=0.3)

# Subplot 3: Scatter
axs[1, 0].scatter(x, np.sin(x) + np.random.randn(100)*0.1, alpha=0.5)
axs[1, 0].set_title('Dispersión')
axs[1, 0].grid(True, alpha=0.3)

# Subplot 4: Histograma
axs[1, 1].hist(np.random.randn(1000), bins=30, color='green', alpha=0.7)
axs[1, 1].set_title('Distribución Normal')
axs[1, 1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()