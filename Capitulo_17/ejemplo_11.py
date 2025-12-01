fig, ax = plt.subplots(figsize=(12, 7))

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Líneas personalizadas
ax.plot(x, y1, color='#FF6B6B', linewidth=2.5, linestyle='-', 
        marker='o', markersize=4, markevery=10, label='Señal 1')
ax.plot(x, y2, color='#4ECDC4', linewidth=2.5, linestyle='--', 
        marker='s', markersize=4, markevery=10, label='Señal 2')

# Títulos y etiquetas
ax.set_xlabel('Tiempo (s)', fontsize=14, fontweight='bold')
ax.set_ylabel('Amplitud', fontsize=14, fontweight='bold')
ax.set_title('Análisis de Señales Temporales', fontsize=16, 
             fontweight='bold', pad=20)

# Leyenda personalizada
ax.legend(loc='upper right', fontsize=12, frameon=True, 
         shadow=True, fancybox=True)

# Grid personalizado
ax.grid(True, linestyle=':', alpha=0.5, linewidth=0.8)

plt.tight_layout()
plt.show()