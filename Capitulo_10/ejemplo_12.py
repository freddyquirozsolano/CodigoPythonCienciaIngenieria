# Archivo: ingenieria/__init__.py
"""
Paquete de ingeniería multidisciplinaria.
Incluye módulos para biomédica, mecatrónica y sistemas.
"""

__version__ = "1.0.0"
__author__ = "Tu Nombre"

# Importar elementos principales para facilitar acceso
from .biomedica import signos_vitales
from .mecatronica import cinematica
from .sistemas import validadores

# Lista de módulos que se importan con "from ingenieria import *"
__all__ = ['biomedica', 'mecatronica', 'sistemas']

print(f"Paquete ingenieria v{__version__} cargado")