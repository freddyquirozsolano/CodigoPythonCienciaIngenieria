class Temperatura:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter para celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, valor):
        """Setter con validación"""
        if valor < -273.15:
            raise ValueError("Temperatura por debajo del cero absoluto")
        self._celsius = valor
    
    @property
    def fahrenheit(self):
        """Propiedad calculada"""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, valor):
        """Setter que actualiza celsius"""
        self.celsius = (valor - 32) * 5/9
    
    @property
    def kelvin(self):
        """Propiedad calculada (solo lectura)"""
        return self._celsius + 273.15
    
    def __str__(self):
        return f"{self.celsius:.2f}°C = {self.fahrenheit:.2f}°F = {self.kelvin:.2f}K"

# Uso natural como atributos
temp = Temperatura(25)
print(temp.celsius)     # 25
print(temp.fahrenheit)  # 77.0
print(temp.kelvin)      # 298.15

temp.fahrenheit = 100  # Modifica celsius automáticamente
print(temp.celsius)    # 37.78

# Validación automática
try:
    temp.celsius = -300  # ValueError
except ValueError as e:
    print(f"Error: {e}")