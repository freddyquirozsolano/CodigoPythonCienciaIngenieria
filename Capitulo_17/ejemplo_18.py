import matplotlib.pyplot as plt
import numpy as np

# Crear un gráfico
fig, ax = plt.subplots(figsize=(10, 6))
x = np.linspace(0, 10, 100)
ax.plot(x, np.sin(x), 'b-', linewidth=2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Gráfico de Ejemplo')
ax.grid(True)

# Guardar en diferentes formatos
plt.savefig('grafico.png', dpi=300, bbox_inches='tight')  # PNG alta calidad
plt.savefig('grafico.pdf', bbox_inches='tight')           # PDF vectorial
plt.savefig('grafico.svg', bbox_inches='tight')           # SVG vectorial
plt.savefig('grafico.jpg', dpi=300, bbox_inches='tight', quality=95)  # JPEG

plt.show()