# Clasificador de peso corporal
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso / (altura ** 2)

print(f"\nTu IMC es: {imc:.2f}")

# Clasificación simple
if imc < 18.5:
    print("Clasificación: Bajo peso")
    print("Recomendación: Consultar con nutricionista")
else:
    print("Clasificación: Peso adecuado o superior")
    print("Recomendación: Mantener hábitos saludables")