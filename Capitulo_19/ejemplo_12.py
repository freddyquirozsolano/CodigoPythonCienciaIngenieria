class MonitorSignosVitales:
    """
    Sistema de monitoreo de signos vitales de pacientes.
    
    Esta clase proporciona funcionalidad para registrar, almacenar y
    analizar signos vitales como frecuencia cardíaca, presión arterial
    y temperatura corporal.
    
    Attributes:
        paciente_id (str): Identificador único del paciente.
        historial (list): Lista de lecturas de signos vitales.
        alertas_activas (list): Lista de alertas generadas.
    
    Example:
        >>> monitor = MonitorSignosVitales("P001", "Juan Pérez")
        >>> monitor.registrar_fc(75)
        >>> monitor.obtener_promedio_fc()
        75.0
    """
    
    def __init__(self, paciente_id, nombre):
        """
        Inicializa un nuevo monitor de signos vitales.
        
        Args:
            paciente_id (str): Identificador único del paciente.
            nombre (str): Nombre completo del paciente.
        """
        self.paciente_id = paciente_id
        self.nombre = nombre
        self.historial = []
        self.alertas_activas = []
    
    def registrar_fc(self, frecuencia):
        """
        Registra una lectura de frecuencia cardíaca.
        
        Args:
            frecuencia (int): Frecuencia cardíaca en bpm.
        
        Raises:
            ValueError: Si la frecuencia está fuera del rango válido (30-200).
        """
        if not 30 <= frecuencia <= 200:
            raise ValueError("Frecuencia cardíaca fuera de rango válido")
        
        self.historial.append({
            'tipo': 'fc',
            'valor': frecuencia,
            'timestamp': datetime.now()
        })
        
        # Generar alerta si es necesario
        if frecuencia > 100 or frecuencia < 60:
            self.alertas_activas.append(f"FC anormal: {frecuencia} bpm")