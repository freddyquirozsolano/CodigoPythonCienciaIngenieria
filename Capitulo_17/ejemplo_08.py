# Datos multidimensionales
n = 100
x = np.random.rand(n)
y = np.random.rand(n)
colores = np.random.rand(n)  # Color basado en una tercera variable
tamaños = 1000 * np.random.rand(n)  # Tamaño basado en una cuarta variable

plt.figure(figsize=(12, 8))
scatter = plt.scatter(x, y, c=colores, s=tamaños, alpha=0.5, 
                     cmap='viridis', edgecolors='black', linewidth=1)
plt.colorbar(scatter, label='Intensidad')
plt.xlabel('Posición X', fontsize=12)
plt.ylabel('Posición Y', fontsize=12)
plt.title('Gráfico de Dispersión Multidimensional', fontsize=14)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()