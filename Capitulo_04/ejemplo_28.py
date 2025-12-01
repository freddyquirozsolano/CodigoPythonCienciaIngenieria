# Clasificar temperatura corporal
temperatura = 37.8

match temperatura:
    case temp if temp < 36:
        print("Hipotermia")
    case temp if 36 <= temp < 37.5:
        print("Temperatura normal")
    case temp if 37.5 <= temp < 38:
        print("Febrícula")
    case temp if temp >= 38:
        print("Fiebre")
