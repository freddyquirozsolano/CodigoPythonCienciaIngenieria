def calcular_dosis(peso_kg, medicamento, concentracion_mg_ml=10):
    """
    Calcula la dosis de medicamento para un paciente.
    
    Esta función calcula la dosis en mililitros basándose en el peso
    del paciente, el medicamento recetado y su concentración.
    
    Parámetros:
        peso_kg (float): Peso del paciente en kilogramos
        medicamento (str): Nombre del medicamento
        concentracion_mg_ml (float, opcional): Concentración del medicamento
            en mg/ml. Por defecto es 10 mg/ml
    
    Retorna:
        float: Dosis calculada en mililitros
    
    Ejemplo:
        >>> calcular_dosis(70, "Paracetamol", 10)
        7.0
        >>> calcular_dosis(50, "Ibuprofeno", 20)
        2.5
    
    Notas:
        - Esta es una implementación simplificada
        - Siempre consultar con un profesional médico
        - La fórmula usa: (peso * 0.1) / concentración
    """
    dosis_mg = peso_kg * 0.1  # Fórmula simplificada
    dosis_ml = dosis_mg / concentracion_mg_ml
    return dosis_ml

# Acceder a la documentación
help(calcular_dosis)  # Muestra el docstring formateado
print(calcular_dosis.__doc__)  # Muestra el texto del docstring