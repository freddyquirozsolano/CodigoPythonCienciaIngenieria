# Clasificar coordenadas
punto = (0, 5)

match punto:
    case (0, 0):
        print("Origen")
    case (0, y):
        print(f"Sobre el eje Y en y={y}")
    case (x, 0):
        print(f"Sobre el eje X en x={x}")
    case (x, y):
        print(f"Punto en ({x}, {y})")
