# Datos ingresados como texto
edad_texto = "45"
peso_texto = "70.5"
altura_texto = "1.75"

# Convertir a números para cálculos
edad = int(edad_texto)
peso = float(peso_texto)
altura = float(altura_texto)

# Calcular IMC
imc = peso / (altura ** 2)
print(f"Edad: {edad} años")
print(f"IMC: {imc:.2f}")

# Convertir resultado a texto para reporte
imc_reporte = str(round(imc, 2))
reporte = "El IMC del paciente es: " + imc_reporte