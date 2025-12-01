import numpy as np
# Cinemática directa de brazo robótico 2D
def cinematica_directa(theta1, theta2, L1, L2):
    """
    Calcula la posición del efector final
    theta1, theta2: ángulos de las articulaciones (grados)
    L1, L2: longitudes de los eslabones
    """
    # Convertir a radianes
    theta1_rad = np.radians(theta1)
    theta2_rad = np.radians(theta2)

    # Posición del codo (articulación 1)
    x1 = L1 * np.cos(theta1_rad)
    y1 = L1 * np.sin(theta1_rad)

    # Posición del efector final
    x2 = x1 + L2 * np.cos(theta1_rad + theta2_rad)
    y2 = y1 + L2 * np.sin(theta1_rad + theta2_rad)

    return np.array([x2, y2])

# Probar con diferentes configuraciones
L1, L2 = 1.0, 0.8  # metros

# Configuraciones de ángulos
configs = [(45, 30), (90, 0), (0, 90), (60, -45)]

for theta1, theta2 in configs:
    pos = cinematica_directa(theta1, theta2, L1, L2)
    print(f"θ1={theta1}°, θ2={theta2}° -> x={pos[0]:.3f}, y={pos[1]:.3f}")
