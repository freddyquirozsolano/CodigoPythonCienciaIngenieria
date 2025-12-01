class Material:
    '''Clase para gestionar propiedades de materiales de ingeniería'''
    
    def __init__(self, nombre, densidad, resistencia, modulo_elasticidad):
        self.nombre = nombre
        self.densidad = densidad  # kg/m³
        self.resistencia = resistencia  # MPa
        self.modulo_elasticidad = modulo_elasticidad  # GPa
        self.costo_por_kg = 0.0
    
    def establecer_costo(self, costo):
        '''Establecer costo por kilogramo'''
        self.costo_por_kg = costo
        return f'Costo de {self.nombre}: ${costo:.2f}/kg'
    
    def calcular_peso(self, volumen):
        '''Calcular peso dado un volumen (m³)'''
        peso = self.densidad * volumen
        return f'{self.nombre}: {peso:.2f} kg para {volumen} m³'
    
    def calcular_costo_total(self, volumen):
        '''Calcular costo total para un volumen dado'''
        peso = self.densidad * volumen
        costo = peso * self.costo_por_kg
        return costo
    
    def calcular_resistencia_peso(self):
        '''Calcular relación resistencia/peso (MPa/(kg/m³))'''
        ratio = self.resistencia / self.densidad
        return ratio
    
    def comparar_con(self, otro_material):
        '''Comparar este material con otro'''
        ratio_self = self.calcular_resistencia_peso()
        ratio_otro = otro_material.calcular_resistencia_peso()
        
        resultado = f'''
Comparación: {self.nombre} vs {otro_material.nombre}
{self.nombre}:
  - Resistencia: {self.resistencia} MPa
  - Densidad: {self.densidad} kg/m³
  - Ratio R/P: {ratio_self:.4f}
{otro_material.nombre}:
  - Resistencia: {otro_material.resistencia} MPa
  - Densidad: {otro_material.densidad} kg/m³
  - Ratio R/P: {ratio_otro:.4f}
'''
        return resultado
    
    def __str__(self):
        return f'{self.nombre}: Resistencia={self.resistencia}MPa, Densidad={self.densidad}kg/m³'

# Uso de la clase
acero = Material('Acero A36', 7850, 250, 200)
aluminio = Material('Aluminio 6061', 2700, 310, 69)

acero.establecer_costo(0.80)
aluminio.establecer_costo(2.50)

print(acero.calcular_peso(0.1))  # 0.1 m³
print(acero.comparar_con(aluminio))
