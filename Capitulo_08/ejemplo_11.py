# Procesador de datos de pruebas de materiales
datos_csv = """
Material,Resistencia_MPa,Elasticidad_GPa,Densidad_kg/m3,Costo_USD/kg
Acero_A36,250,200,7850,0.80
Aluminio_6061,310,69,2700,2.50
Titanio_Grade5,900,114,4430,15.00
Fibra_Carbono,3500,230,1600,50.00
"""

def procesar_csv_materiales(csv_text):
    lineas = csv_text.strip().split('\n')
    encabezados = lineas[0].split(',')
    
    materiales = []
    for linea in lineas[1:]:
        valores = linea.split(',')
        material = {
            'nombre': valores[0],
            'resistencia': float(valores[1]),
            'elasticidad': float(valores[2]),
            'densidad': float(valores[3]),
            'costo': float(valores[4])
        }
        # Calcular relación resistencia/peso
        material['ratio_resistencia_peso'] = material['resistencia'] / material['densidad']
        materiales.append(material)
    
    return materiales

# Procesar y analizar
materiales = procesar_csv_materiales(datos_csv)

# Encontrar el mejor material por ratio resistencia/peso
mejor = max(materiales, key=lambda m: m['ratio_resistencia_peso'])
print(f"Mejor relación resistencia/peso: {mejor['nombre']}")
print(f"Ratio: {mejor['ratio_resistencia_peso']:.4f}")
