import logging

class ControlRobot:
    def __init__(self, robot_id):
        self.robot_id = robot_id
        self.posicion = {'x': 0, 'y': 0}
        self.bateria = 100
        logging.info(f'Robot {robot_id} inicializado')
    
    def mover(self, x, y, velocidad):
        try:
            if self.bateria < 10:
                raise RuntimeError('Batería crítica')
            
            if velocidad < 0 or velocidad > 3:
                raise ValueError('Velocidad fuera de rango (0-3)')
            
            self.posicion['x'] = x
            self.posicion['y'] = y
            self.bateria -= 5
            
            logging.info(f'Movimiento: ({x}, {y}) a {velocidad} m/s')
            
            if self.bateria < 20:
                logging.warning(f'Batería baja: {self.bateria}%')
            
            return True
        
        except (ValueError, RuntimeError) as e:
            logging.error(f'Error en movimiento: {e}')
            return False
        finally:
            logging.debug(f'Posición: {self.posicion}, Batería: {self.bateria}%')
