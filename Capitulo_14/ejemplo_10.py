import sqlite3
# Conectar a base de datos (se crea si no existe)
conexion = sqlite3.connect('hospital.db')
cursor = conexion.cursor()

# Crear tabla de pacientes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pacientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,  -- ID único automático
        nombre TEXT NOT NULL,                  -- Texto, obligatorio
        edad INTEGER,                          -- Número entero
        tipo_sangre TEXT,                      -- Texto opcional
        fecha_registro TEXT                    -- Fecha como texto
    )
''')

# Confirmar cambios
conexion.commit()

# Cerrar conexión
conexion.close()

print('✓ Base de datos y tabla creadas')
