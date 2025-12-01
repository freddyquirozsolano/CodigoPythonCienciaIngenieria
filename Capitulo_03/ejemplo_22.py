# Guardar historial de paciente
def guardar_paciente(nombre, edad, tipo_sangre, historial):
    with open(f"paciente_{nombre.replace(' ', '_')}.txt", "w") as archivo:
        archivo.write(f"HISTORIAL MÉDICO\n")
        archivo.write(f"{'=' * 50}\n\n")
        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Edad: {edad} años\n")
        archivo.write(f"Tipo de sangre: {tipo_sangre}\n")
        archivo.write(f"\nConsultas:\n")
        archivo.write(f"{'-' * 50}\n")
        for consulta in historial:
            archivo.write(f"Fecha: {consulta['fecha']}\n")
            archivo.write(f"Diagnóstico: {consulta['diagnostico']}\n")
            archivo.write(f"Tratamiento: {consulta['tratamiento']}\n")
            archivo.write(f"\n")

# Ejemplo de uso
historial_paciente = [
    {
        "fecha": "2025-10-15",
        "diagnostico": "Hipertensión leve",
        "tratamiento": "Enalapril 10mg"
    },
    {
        "fecha": "2025-11-03",
        "diagnostico": "Control rutinario",
        "tratamiento": "Continuar medicación"
    }
]

guardar_paciente("Ana García", 45, "O+", historial_paciente)

# Leer y mostrar historial
with open("paciente_Ana_García.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)