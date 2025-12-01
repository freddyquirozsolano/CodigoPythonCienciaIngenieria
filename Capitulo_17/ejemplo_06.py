# Datos: resultados de pruebas antes y después
categorias = ['Velocidad', 'Precisión', 'Eficiencia', 'Costo']
antes = [70, 65, 60, 80]
despues = [85, 82, 78, 75]

x = np.arange(len(categorias))
ancho = 0.35

fig, ax = plt.subplots(figsize=(12, 6))
barras1 = ax.bar(x - ancho/2, antes, ancho, label='Antes', color='lightcoral')
barras2 = ax.bar(x + ancho/2, despues, ancho, label='Después', color='lightgreen')

ax.set_xlabel('Métrica', fontsize=12)
ax.set_ylabel('Puntuación', fontsize=12)
ax.set_title('Comparación: Antes vs Después de Optimización', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(categorias)
ax.legend()
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()