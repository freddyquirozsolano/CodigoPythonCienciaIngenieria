import logging

# Configuración simple
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log'
)

# Usar logging
logging.debug('Mensaje de debug')
logging.info('Aplicación iniciada')
logging.warning('Advertencia: Memoria al 80%')
logging.error('Error al conectar a base de datos')
logging.critical('Sistema crítico falló')
