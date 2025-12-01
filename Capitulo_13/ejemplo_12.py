import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='signos_vitales.log'
)

class MonitorSignosVitales:
    def __init__(self, paciente_id):
        self.paciente_id = paciente_id
        logging.info(f'Monitor iniciado para paciente {paciente_id}')
    
    def registrar_presion(self, sistolica, diastolica):
        try:
            sistolica = float(sistolica)
            diastolica = float(diastolica)
            
            if sistolica < 0 or diastolica < 0:
                raise ValueError('Valores no pueden ser negativos')
            
            if sistolica > 180 or diastolica > 120:
                logging.warning(f'ALERTA: Hipertensión crisis - {sistolica}/{diastolica}')
                return 'CRÍTICO'
            elif sistolica > 140 or diastolica > 90:
                logging.info(f'Presión elevada: {sistolica}/{diastolica}')
                return 'ELEVADA'
            else:
                logging.info(f'Presión normal: {sistolica}/{diastolica}')
                return 'NORMAL'
        
        except ValueError as e:
            logging.error(f'Error en datos de presión: {e}')
            return 'ERROR'
        except Exception as e:
            logging.critical(f'Error inesperado: {e}', exc_info=True)
            return 'ERROR'

# Uso
monitor = MonitorSignosVitales('P001')
print(monitor.registrar_presion(120, 80))  # NORMAL
print(monitor.registrar_presion(150, 95))  # ELEVADA
print(monitor.registrar_presion('abc', 80))  # ERROR
