class ConfiguracionSistema:
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.configuraciones = {}
        return cls._instancia
    
    def establecer(self, clave, valor):
        self.configuraciones[clave] = valor
    
    def obtener(self, clave):
        return self.configuraciones.get(clave)

# Uso
config1 = ConfiguracionSistema()
config2 = ConfiguracionSistema()
config1.establecer('tema', 'oscuro')
print(config2.obtener('tema'))  # 'oscuro' - es la misma instancia