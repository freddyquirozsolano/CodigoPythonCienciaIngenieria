# sistema_signos_vitales.py

def analizar_paciente(nombre, edad, peso, altura, fc, ps, pd):
    """
    Realiza análisis completo de signos vitales de un paciente.
    """
    print("=" * 60)
    print(f"REPORTE DE SIGNOS VITALES - {nombre}")
    print("=" * 60)
    
    # IMC
    imc = peso / (altura ** 2)
    if imc < 18.5:
        clasificacion = "Bajo peso"
    elif imc < 25:
        clasificacion = "Peso normal"
    elif imc < 30:
        clasificacion = "Sobrepeso"
    else:
        clasificacion = "Obesidad"
    print(f"\nIMC: {imc:.2f} - {clasificacion}")
    
    # Frecuencia cardíaca
    fcm = 220 - edad
    zona_min = int(fcm * 0.6)
    zona_max = int(fcm * 0.7)
    print(f"\nFrecuencia cardíaca: {fc} bpm")
    print(f"FCM teórica: {fcm} bpm")
    print(f"Zona de ejercicio: {zona_min}-{zona_max} bpm")
    
    # Presión arterial
    print(f"\nPresión arterial: {ps}/{pd} mmHg")
    if ps > 140 or pd > 90:
        print("⚠️ ALERTA: Presión arterial elevada")
    elif ps < 90 or pd < 60:
        print("⚠️ ALERTA: Presión arterial baja")
    else:
        print("✓ Presión arterial normal")
    
    print("=" * 60)

# Uso
analizar_paciente(
    nombre="María López",
    edad=45,
    peso=70,
    altura=1.65,
    fc=78,
    ps=125,
    pd=82
)