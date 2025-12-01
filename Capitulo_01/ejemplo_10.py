# calculadora_biomedica.py
# Calculadora para Ingeniería Biomédica

print("=" * 60)
print("🏥 CALCULADORA BIOMÉDICA")
print("=" * 60)
print()

# Menú de opciones
print("Selecciona una operación:")
print("1. Calcular IMC (Índice de Masa Corporal)")
print("2. Calcular Frecuencia Cardíaca Máxima")
print("3. Calcular Dosis de Medicamento")
print("4. Convertir Temperatura (°C a °F)")
print()

opcion = input("Ingresa el número de opción: ")

if opcion == "1":
    print("\n--- Cálculo de IMC ---")
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    imc = peso / (altura ** 2)
    print(f"Tu IMC es: {imc:.2f}")
    
    # Interpretación
    if imc < 18.5:
        print("Clasificación: Bajo peso")
    elif imc < 25:
        print("Clasificación: Peso normal")
    elif imc < 30:
        print("Clasificación: Sobrepeso")
    else:
        print("Clasificación: Obesidad")

elif opcion == "2":
    print("\n--- Frecuencia Cardíaca Máxima ---")
    edad = int(input("Edad: "))
    fcm = 220 - edad
    print(f"Tu frecuencia cardíaca máxima es: {fcm} bpm")
    print(f"Zona de ejercicio (60-80%): {fcm*0.6:.0f}-{fcm*0.8:.0f} bpm")

elif opcion == "3":
    print("\n--- Dosis de Medicamento ---")
    peso = float(input("Peso del paciente (kg): "))
    dosis_por_kg = float(input("Dosis por kg (mg/kg): "))
    dosis_total = peso * dosis_por_kg
    print(f"Dosis total: {dosis_total:.2f} mg")

elif opcion == "4":
    print("\n--- Conversión de Temperatura ---")
    celsius = float(input("Temperatura en °C: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit:.2f}°F")

else:
    print("Opción no válida")

print("\n¡Gracias por usar la calculadora biomédica!")