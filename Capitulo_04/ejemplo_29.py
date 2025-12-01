# Sistema de clasificación de emergencias médicas
def clasificar_emergencia(codigo):
    """
    Clasifica emergencias según código de triaje
    Código 1: Emergencia inmediata
    Código 2: Urgencia
    Código 3: Menor urgencia
    Código 4: No urgente
    """
    match codigo:
        case 1:
            color = "ROJO"
            accion = "Atención inmediata - Riesgo vital"
            tiempo_max = "0 minutos"
        case 2:
            color = "NARANJA"
            accion = "Atención urgente - Riesgo potencial"
            tiempo_max = "10 minutos"
        case 3:
            color = "AMARILLO"
            accion = "Atención menor urgencia"
            tiempo_max = "60 minutos"
        case 4:
            color = "VERDE"
            accion = "No urgente"
            tiempo_max = "120 minutos"
        case _:
            color = "DESCONOCIDO"
            accion = "Código no válido"
            tiempo_max = "N/A"
    
    return {
        'codigo': codigo,
        'color': color,
        'accion': accion,
        'tiempo_maximo': tiempo_max
    }