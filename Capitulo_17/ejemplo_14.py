import matplotlib.pyplot as plt
import numpy as np

# Simular señal ECG
def generar_ecg(duracion=5, frecuencia_muestreo=500):
    """Genera una señal ECG simulada"""
    t = np.linspace(0, duracion, duracion * frecuencia_muestreo)
    frecuencia_cardiaca = 75 / 60  # 75 bpm en Hz
    
    # Componentes del ECG
    p_wave = 0.1 * np.sin(2 * np.pi * frecuencia_cardiaca * t * 2)
    
    qrs_complex = np.zeros_like(t)
    periodo = 1 / frecuencia_cardiaca
    for i in range(int(duracion * frecuencia_cardiaca)):
        inicio = int(i * periodo * frecuencia_muestreo)
        if inicio < len(t):
            qrs_complex[inicio:inicio+20] = np.random.randn(20) * 0.3
            qrs_complex[inicio+10] = 1.0  # Pico R
    
    t_wave = 0.15 * np.sin(2 * np.pi * frecuencia_cardiaca * t * 1.5 - np.pi/4)
    ecg = p_wave + qrs_complex + t_wave + np.random.randn(len(t)) * 0.02
    
    return t, ecg

# Generar y visualizar
tiempo, ecg = generar_ecg()

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))

# Gráfico principal
ax1.plot(tiempo, ecg, 'b-', linewidth=1.5)
ax1.set_xlabel('Tiempo (s)', fontsize=12, fontweight='bold')
ax1.set_ylabel('Amplitud (mV)', fontsize=12, fontweight='bold')
ax1.set_title('Electrocardiograma (ECG)', fontsize=14, fontweight='bold')
ax1.grid(True, alpha=0.3)

# Detección de picos R
umbral = 0.5
ax1.axhline(y=umbral, color='red', linestyle='--', linewidth=1.5, 
           alpha=0.7, label=f'Umbral: {umbral} mV')

picos = []
for i in range(1, len(ecg)-1):
    if ecg[i] > umbral and ecg[i] > ecg[i-1] and ecg[i] > ecg[i+1]:
        picos.append(i)
        ax1.plot(tiempo[i], ecg[i], 'ro', markersize=8)

ax1.legend()

# Detalle de un latido
ax2.plot(tiempo[0:500], ecg[0:500], 'darkblue', linewidth=2)
ax2.set_xlabel('Tiempo (s)', fontsize=12, fontweight='bold')
ax2.set_ylabel('Amplitud (mV)', fontsize=12, fontweight='bold')
ax2.set_title('Detalle de un Latido Cardíaco', fontsize=12, fontweight='bold')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()