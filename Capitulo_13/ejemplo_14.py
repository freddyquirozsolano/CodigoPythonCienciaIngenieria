import logging
import json

class ProcesadorArchivos:
    def __init__(self):
        self.archivos_procesados = 0
        self.errores = []
    
    def procesar_json(self, ruta_archivo):
        archivo = None
        try:
            logging.info(f'Procesando archivo: {ruta_archivo}')
            archivo = open(ruta_archivo, 'r', encoding='utf-8')
            datos = json.load(archivo)
            self.archivos_procesados += 1
            logging.info(f'Archivo procesado exitosamente')
            return datos
        
        except FileNotFoundError:
            error_msg = f'Archivo no encontrado: {ruta_archivo}'
            logging.error(error_msg)
            self.errores.append(error_msg)
            return None
        
        except json.JSONDecodeError as e:
            error_msg = f'JSON inválido en {ruta_archivo}: {e}'
            logging.error(error_msg)
            self.errores.append(error_msg)
            return None
        
        finally:
            if archivo:
                archivo.close()
                logging.debug('Archivo cerrado')
