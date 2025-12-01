import pandas as pd

# Leer CSV básico
# Debes agregar el archivo 'datos.csv' en el mismo directorio para que funcione
df = pd.read_csv('datos.csv')

# Leer CSV con opciones comunes
df = pd.read_csv(
    'datos.csv',
    sep=';',                       # Separador diferente
    encoding='utf-8',              # Codificación
    skiprows=2,                    # Saltar primeras 2 filas
    usecols=['columna1', 'columna2'],  # Solo ciertas columnas
    parse_dates=['fecha'],         # Convertir a datetime
    na_values=['N/A', 'missing']   # Valores que representan NaN
)

# Exportar a CSV
df.to_csv('resultado.csv', index=False, encoding='utf-8')

# Exportar con opciones (formato de decimales y separador)
df.to_csv(
    'resultado.csv',
    sep=';',
    index=False,
    float_format='%.2f'            # Formato de decimales
)
