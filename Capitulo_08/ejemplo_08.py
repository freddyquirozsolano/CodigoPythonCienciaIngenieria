# Parser de mensajes HL7 simplificado
mensaje_hl7 = """
MSH|^~\&|SISTEMA|HOSPITAL|LAB|HOSPITAL|20250104120000||ORU^R01|MSG001|P|2.5
PID|1||12345||LOPEZ^MARIA^||19800315|F|||
OBR|1||LAB001|CBC^HEMOGRAMA^
OBX|1|NM|WBC^LEUCOCITOS^||7.5|10^9/L|4.0-11.0|N|||F
OBX|2|NM|RBC^ERITROCITOS^||4.8|10^12/L|4.5-5.5|N|||F
"""

def parsear_hl7(mensaje):
    lineas = mensaje.strip().split('\n')
    datos = {}
    
    for linea in lineas:
        campos = linea.split('|')
        tipo = campos[0]
        
        if tipo == 'PID':  # Datos del paciente
            nombre_completo = campos[5].split('^')
            datos['apellido'] = nombre_completo[0]
            datos['nombre'] = nombre_completo[1]
            datos['fecha_nacimiento'] = campos[7]
            datos['sexo'] = campos[8]
        
        elif tipo == 'OBX':  # Resultados
            if 'resultados' not in datos:
                datos['resultados'] = []
            
            test_info = campos[3].split('^')
            resultado = {
                'codigo': test_info[0],
                'nombre': test_info[1],
                'valor': campos[5],
                'unidad': campos[6],
                'rango': campos[7]
            }
            datos['resultados'].append(resultado)
    
    return datos

# Procesar mensaje
info_paciente = parsear_hl7(mensaje_hl7)
print(f"Paciente: {info_paciente['nombre']} {info_paciente['apellido']}")
print(f"Resultados: {len(info_paciente['resultados'])} tests")
