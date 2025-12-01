# split() - dividir string en lista
datos_csv = "Juan,45,O+,120/80"
campos = datos_csv.split(',')
print(campos)  # ['Juan', '45', 'O+', '120/80']

# splitlines() - dividir por líneas
log = "ERROR: Conexión perdida\nWARNING: Batería baja\nINFO: Sistema OK"
lineas = log.splitlines()
print(lineas)  # ['ERROR: Conexión perdida', 'WARNING: Batería baja', 'INFO: Sistema OK']

# join() - unir lista en string
palabras = ['Python', 'para', 'Ingeniería']
frase = ' '.join(palabras)
print(frase)  # 'Python para Ingeniería'

# Útil para crear CSV
datos = ['María', '32', 'A+', '118/75']
linea_csv = ','.join(datos)
print(linea_csv)  # 'María,32,A+,118/75'
