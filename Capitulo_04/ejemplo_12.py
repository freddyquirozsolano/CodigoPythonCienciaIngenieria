# Clasificador completo de IMC
print("=== CALCULADORA DE ÍNDICE DE MASA CORPORAL ===\n")

peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso / (altura ** 2)

print(f"\nIMC calculado: {imc:.2f}")
print("-" * 50)

if imc < 16:
    categoria = "Delgadez severa"
    riesgo = "ALTO"
    recomendacion = "Consultar médico urgentemente"
    color = "🔴"
elif imc < 17:
    categoria = "Delgadez moderada"
    riesgo = "MEDIO"
    recomendacion = "Aumentar ingesta calórica supervisada"
    color = "🟠"
elif imc < 18.5:
    categoria = "Delgadez leve"
    riesgo = "BAJO"
    recomendacion = "Mejorar alimentación"
    color = "🟡"
elif imc < 25:
    categoria = "Peso normal"
    riesgo = "NINGUNO"
    recomendacion = "Mantener hábitos saludables"
    color = "🟢"
elif imc < 30:
    categoria = "Sobrepeso"
    riesgo = "BAJO"
    recomendacion = "Ejercicio regular y dieta balanceada"
    color = "🟡"
elif imc < 35:
    categoria = "Obesidad clase I"
    riesgo = "MEDIO"
    recomendacion = "Programa de pérdida de peso supervisado"
    color = "🟠"
elif imc < 40:
    categoria = "Obesidad clase II"
    riesgo = "ALTO"
    recomendacion = "Intervención médica necesaria"
    color = "🔴"
else:
    categoria = "Obesidad clase III (mórbida)"
    riesgo = "MUY ALTO"
    recomendacion = "Atención médica urgente"
    color = "🔴"

print(f"\n{color} Categoría: {categoria}")
print(f"Nivel de riesgo: {riesgo}")
print(f"Recomendación: {recomendacion}")
print("-" * 50)