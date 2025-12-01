def calcular_dosis(peso, concentracion, dosis_por_kg):
    """
    Calcula la dosis de medicamento necesaria para un paciente.
    
    Args:
        peso (float): Peso del paciente en kilogramos.
        concentracion (float): Concentración del medicamento en mg/ml.
        dosis_por_kg (float): Dosis requerida por kilogramo de peso en mg/kg.
    
    Returns:
        dict: Diccionario con 'dosis_total' (mg) y 'volumen' (ml).
    
    Raises:
        ValueError: Si algún parámetro es negativo o cero.
    
    Examples:
        >>> calcular_dosis(70, 10, 5)
        {'dosis_total': 350.0, 'volumen': 35.0}
    
    Note:
        Esta función asume una relación lineal entre peso y dosis.
        Siempre consultar con un profesional médico.
    """
    if peso <= 0 or concentracion <= 0 or dosis_por_kg <= 0:
        raise ValueError("Todos los parámetros deben ser positivos")
    
    dosis_total = peso * dosis_por_kg
    volumen = dosis_total / concentracion
    
    return {
        'dosis_total': dosis_total,
        'volumen': volumen
    }