# Sistema de gestión de pacientes
pacientes = {
    'P001': {
        'nombre': 'María López',
        'edad': 45,
        'tipo_sangre': 'O+',
        'alergias': {'penicilina', 'polen'},
        'medicamentos': ['aspirina', 'metformina']
    },
    'P002': {
        'nombre': 'Juan Pérez',
        'edad': 32,
        'tipo_sangre': 'A+',
        'alergias': {'mariscos', 'penicilina'},
        'medicamentos': ['ibuprofeno']
    }
}

# Buscar alergias comunes
alergias_comunes = pacientes['P001']['alergias'] & pacientes['P002']['alergias']
print(f"Alergias comunes: {alergias_comunes}")

# Agregar nueva visita
pacientes['P001']['ultima_visita'] = '2025-01-15'
pacientes['P001']['diagnostico'] = 'Hipertensión controlada'
