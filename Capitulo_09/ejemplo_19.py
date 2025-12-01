# sistemas.py - Biblioteca de funciones para sistemas

import re
import hashlib

def validar_email(email):
    """
    Valida si un email tiene formato correcto.
    
    Args:
        email (str): Dirección de email a validar
    
    Returns:
        bool: True si el formato es válido
    """
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(patron, email))

def validar_password(password, min_length=8):
    """
    Valida la fortaleza de una contraseña.
    
    Args:
        password (str): Contraseña a validar
        min_length (int): Longitud mínima requerida
    
    Returns:
        tuple: (es_valida, mensaje)
    """
    if len(password) < min_length:
        return False, f"Mínimo {min_length} caracteres"
    if not re.search(r'[A-Z]', password):
        return False, "Debe contener mayúscula"
    if not re.search(r'[a-z]', password):
        return False, "Debe contener minúscula"
    if not re.search(r'[0-9]', password):
        return False, "Debe contener número"
    return True, "Contraseña válida"

def convertir_bytes(bytes_cantidad, unidad='MB'):
    """
    Convierte bytes a diferentes unidades.
    
    Args:
        bytes_cantidad (int): Cantidad en bytes
        unidad (str): Unidad destino ('KB', 'MB', 'GB', 'TB')
    
    Returns:
        float: Cantidad convertida
    """
    unidades = {
        'KB': 1024,
        'MB': 1024 ** 2,
        'GB': 1024 ** 3,
        'TB': 1024 ** 4
    }
    return bytes_cantidad / unidades.get(unidad, 1)

def validar_ipv4(ip):
    """
    Valida si una dirección IPv4 es válida.
    
    Args:
        ip (str): Dirección IP a validar
    
    Returns:
        bool: True si es válida
    """
    patron = r'^(\d{1,3}\.){3}\d{1,3}$'
    if not re.match(patron, ip):
        return False
    octetos = ip.split('.')
    return all(0 <= int(octeto) <= 255 for octeto in octetos)

# Ejemplo de uso
if __name__ == "__main__":
    print(f"Email válido: {validar_email('usuario@ejemplo.com')}")
    print(f"IP válida: {validar_ipv4('192.168.1.1')}")
    
    valida, msg = validar_password("MiPassword123")
    print(f"Contraseña: {msg}")