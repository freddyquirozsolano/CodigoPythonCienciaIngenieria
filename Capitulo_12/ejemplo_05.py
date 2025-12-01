class Vector3D:
    """Clase que representa un vector en 3D"""
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        """Representación legible para usuarios"""
        return f"Vector({self.x}, {self.y}, {self.z})"
    
    def __repr__(self):
        """Representación para desarrolladores"""
        return f"Vector3D({self.x}, {self.y}, {self.z})"
    
    def __add__(self, otro):
        """Suma de vectores con operador +"""
        return Vector3D(
            self.x + otro.x,
            self.y + otro.y,
            self.z + otro.z
        )
    
    def __sub__(self, otro):
        """Resta de vectores con operador -"""
        return Vector3D(
            self.x - otro.x,
            self.y - otro.y,
            self.z - otro.z
        )
    
    def __mul__(self, escalar):
        """Multiplicación por escalar"""
        return Vector3D(
            self.x * escalar,
            self.y * escalar,
            self.z * escalar
        )
    
    def __eq__(self, otro):
        """Comparación de igualdad con =="""
        return (self.x == otro.x and 
                self.y == otro.y and 
                self.z == otro.z)
    
    def __len__(self):
        """Longitud del vector (magnitud)"""
        import math
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __getitem__(self, indice):
        """Acceso por índice: vector[0] -> x"""
        if indice == 0:
            return self.x
        elif indice == 1:
            return self.y
        elif indice == 2:
            return self.z
        else:
            raise IndexError("Índice fuera de rango")
    
    def __setitem__(self, indice, valor):
        """Modificación por índice: vector[0] = 5"""
        if indice == 0:
            self.x = valor
        elif indice == 1:
            self.y = valor
        elif indice == 2:
            self.z = valor
        else:
            raise IndexError("Índice fuera de rango")

# Uso natural de operadores
v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)

print(v1)              # Vector(1, 2, 3)
print(v1 + v2)         # Vector(5, 7, 9)
print(v1 * 2)          # Vector(2, 4, 6)
print(v1 == v2)        # False
print(len(v1))         # 3.7416...
print(v1[0])           # 1
v1[1] = 10
print(v1)              # Vector(1, 10, 3)