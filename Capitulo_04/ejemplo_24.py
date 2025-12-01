# Sistema de clasificación de tipo de sangre
tipo_sangre = "O+"

match tipo_sangre:
    case "O+":
        print("Donante universal para tipos positivos")
    case "O-":
        print("Donante universal para todos los tipos")
    case "AB+":
        print("Receptor universal")
    case "A+" | "A-":
        print("Tipo A")
    case "B+" | "B-":
        print("Tipo B")
    case _:
        print("Tipo de sangre no reconocido")
