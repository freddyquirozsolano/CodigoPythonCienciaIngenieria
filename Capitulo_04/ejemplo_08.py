# Sistema de navegación del robot
objetivo_x = float(input("Coordenada X objetivo: "))
posicion_actual_x = float(input("Posición X actual: "))

diferencia = objetivo_x - posicion_actual_x

print(f"\nAnálisis de trayectoria:")

if diferencia > 0:
    print("Dirección: Avanzar hacia la derecha")
    print(f"Distancia: {diferencia:.2f} metros")
    print("Comando: Girar motores en sentido horario")
else:
    print("Dirección: Avanzar hacia la izquierda")
    print(f"Distancia: {abs(diferencia):.2f} metros")
    print("Comando: Girar motores en sentido antihorario")