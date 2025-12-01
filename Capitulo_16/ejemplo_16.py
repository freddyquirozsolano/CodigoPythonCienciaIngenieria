import pandas as pd

# Leer una hoja específica de un archivo Excel
# Debes agregar el archivo 'datos.xlsx' en el mismo directorio para que funcione
df = pd.read_excel('datos.xlsx', sheet_name='Hoja1')

# Leer todas las hojas (devuelve un diccionario de DataFrames)
dfs = pd.read_excel('datos.xlsx', sheet_name=None)

# Exportar un DataFrame a Excel
df.to_excel('resultado.xlsx', sheet_name='Resultados', index=False)

# Exportar múltiples DataFrames a un archivo Excel con varias hojas
with pd.ExcelWriter('resultado.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Hoja1', index=False)
    df2.to_excel(writer, sheet_name='Hoja2', index=False)
    df3.to_excel(writer, sheet_name='Hoja3', index=False)
