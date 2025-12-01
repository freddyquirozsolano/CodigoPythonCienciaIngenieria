# Sistema de caché para aplicación web
cache = {}

def obtener_datos(clave):
    '''Obtener datos con caché'''
    if clave in cache:
        print(f'✓ Datos encontrados en caché: {clave}')
        return cache[clave]
    else:
        print(f'✗ Cargando desde base de datos: {clave}')
        # Simular carga de base de datos
        datos = f'Contenido de {clave}'
        cache[clave] = datos
        return datos

# Estadísticas de caché
stats = {
    'hits': 0,
    'misses': 0,
    'total_requests': 0
}

# Limpiar caché
def limpiar_cache():
    cache.clear()
    print('Caché limpiado')

