# Sistema de comandos de robot móvil
def ejecutar_comando(comando, parametro=None):
    """
    Procesa comandos para control de robot
    """
    match comando.upper():
        case "FORWARD":
            velocidad = parametro if parametro else 100
            print(f"Robot avanzando a {velocidad}%")
            return {"motor_izq": velocidad, "motor_der": velocidad}
        
        case "LEFT":
            print("Robot girando a la izquierda")
            return {"motor_izq": 0, "motor_der": 100}
        
        case "STOP":
            print("Robot detenido")
            return {"motor_izq": 0, "motor_der": 0}
        
        case _:
            return {"error": "Comando inválido"}
