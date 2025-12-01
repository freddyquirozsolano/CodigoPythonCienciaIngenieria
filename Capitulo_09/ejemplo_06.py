# Función que retorna un valor
def calcular_imc(peso, altura):
    """Calcula y retorna el IMC"""
    imc = peso / (altura ** 2)
    return imc  # Devuelve el valor calculado

# Usar el valor retornado
mi_imc = calcular_imc(70, 1.75)
print(f"Tu IMC es: {mi_imc:.2f}")  # Tu IMC es: 22.86

# Puedes usar el resultado en condiciones
if mi_imc < 18.5:
    print("Clasificación: Bajo peso")
elif mi_imc < 25:
    print("Clasificación: Peso normal")
elif mi_imc < 30:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificación: Obesidad")

# O en otros cálculos
imc_ajustado = mi_imc * 1.05
print(f"IMC ajustado: {imc_ajustado:.2f}")