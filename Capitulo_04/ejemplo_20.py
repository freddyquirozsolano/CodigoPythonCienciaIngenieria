# Decisiones anidadas básicas
edad = 20
tiene_licencia = True

if edad >= 18:
    print("Es mayor de edad")
    if tiene_licencia:
        print("Puede conducir")
    else:
        print("Necesita obtener licencia")
else:
    print("Es menor de edad")
    print("No puede conducir")

# Ejemplo más complejo
calificacion = 85
asistencia = 90

if calificacion >= 70:
    print("Aprobado")
    if asistencia >= 80:
        if calificacion >= 90:
            print("Calificación final: A")
        else:
            print("Calificación final: B")
    else:
        print("Calificación reducida por baja asistencia")
        print("Calificación final: C")
else:
    print("Reprobado")