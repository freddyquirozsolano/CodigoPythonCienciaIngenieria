# Analizador de logs de servidor
import re
from collections import Counter

log_ejemplo = """
2025-01-04 10:23:45 [INFO] Usuario juan@ejemplo.com login exitoso desde 192.168.1.100
2025-01-04 10:24:12 [ERROR] Conexión a base de datos falló
2025-01-04 10:25:33 [WARNING] Memoria al 85%
2025-01-04 10:26:01 [ERROR] Timeout en API externa
2025-01-04 10:27:15 [INFO] Usuario maria@ejemplo.com login exitoso desde 192.168.1.101
2025-01-04 10:28:00 [ERROR] Puerto 8080 no disponible
"""

def analizar_logs(log_text):
    lineas = log_text.strip().split('\n')
    
    # Contadores
    niveles = []
    ips = []
    errores = []
    
    # Patrones regex
    patron_nivel = r'\[(\w+)\]'
    patron_ip = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    
    for linea in lineas:
        # Extraer nivel
        match_nivel = re.search(patron_nivel, linea)
        if match_nivel:
            niveles.append(match_nivel.group(1))
            
            if match_nivel.group(1) == 'ERROR':
                errores.append(linea)
        
        # Extraer IPs
        ips_encontradas = re.findall(patron_ip, linea)
        ips.extend(ips_encontradas)
    
    # Análisis
    conteo_niveles = Counter(niveles)
    conteo_ips = Counter(ips)
    
    return {
        'total_lineas': len(lineas),
        'por_nivel': dict(conteo_niveles),
        'ips_unicas': len(set(ips)),
        'ip_mas_comun': conteo_ips.most_common(1)[0] if ips else None,
        'errores': errores
    }

# Analizar
resultados = analizar_logs(log_ejemplo)
print(f"Total de líneas: {resultados['total_lineas']}")
print(f"Errores: {resultados['por_nivel'].get('ERROR', 0)}")
print(f"IPs únicas: {resultados['ips_unicas']}")
