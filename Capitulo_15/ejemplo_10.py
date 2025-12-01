import numpy as np
# Datos de monitoreo de servidor (simulados)
np.random.seed(42)

# Métricas durante 24 horas (lecturas cada hora)
horas = np.arange(0, 24)
uso_cpu = 30 + 20 * np.sin(horas * np.pi / 12) + np.random.normal(0, 5, 24)
uso_memoria = 40 + 10 * np.sin(horas * np.pi / 12) + np.random.normal(0, 3, 24)
tiempo_respuesta = 50 + 30 * np.sin(horas * np.pi / 12) + np.random.normal(0, 8, 24)

# Análisis estadístico
print("Estadísticas de CPU:")
print(f"  Promedio: {np.mean(uso_cpu):.1f}%")
print(f"  Máximo: {np.max(uso_cpu):.1f}%")
print(f"  Mínimo: {np.min(uso_cpu):.1f}%")
print(f"  Desv. Est: {np.std(uso_cpu):.1f}%")

# Detectar picos de uso
umbral_cpu = np.mean(uso_cpu) + 2 * np.std(uso_cpu)
picos = horas[uso_cpu > umbral_cpu]
print(f"\nPicos de CPU detectados a las: {picos}:00")
