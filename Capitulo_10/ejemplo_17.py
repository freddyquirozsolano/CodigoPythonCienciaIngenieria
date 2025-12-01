# Instalar paquetes biomédicos
pip install numpy scipy matplotlib
pip install biopython  # Biología computacional
pip install pydicom  # Imágenes médicas DICOM
pip install scikit-learn  # Machine learning
pip install pandas  # Análisis de datos

# Ejemplo de uso
import numpy as np
import matplotlib.pyplot as plt

# Simular ECG
tiempo = np.linspace(0, 2, 1000)
ecg = np.sin(2 * np.pi * 1.2 * tiempo) + 0.5 * np.sin(2 * np.pi * 0.5 * tiempo)

plt.plot(tiempo, ecg)
plt.title('Señal ECG Simulada')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.show()