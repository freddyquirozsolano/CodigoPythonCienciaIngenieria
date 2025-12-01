def verificar_edad(edad):
    """Verifica si una persona es mayor de edad"""
    if edad >= 18:
        return "Mayor de edad"
        print("Este mensaje nunca se imprime")  # Código inalcanzable
    else:
        return "Menor de edad"
    
    print("Este tampoco")  # Nunca se ejecuta

resultado = verificar_edad(20)
print(resultado)  # Mayor de edad