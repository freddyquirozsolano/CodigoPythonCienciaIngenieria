# Lectura de archivos DICOM
import pydicom
import numpy as np

# Leer archivo DICOM
ds = pydicom.dcmread('imagen_ct.dcm')

# Información del paciente
print(f"Nombre del paciente: {ds.PatientName}")
print(f"ID del paciente: {ds.PatientID}")
print(f"Fecha del estudio: {ds.StudyDate}")

# Información de la imagen
print(f"\nModalidad: {ds.Modality}")
print(f"Dimensiones: {ds.Rows} x {ds.Columns}")

# Acceder a los datos de píxeles
imagen = ds.pixel_array
print(f"Valores de píxeles (min/max): {imagen.min()} / {imagen.max()}")

# Visualizar con matplotlib
import matplotlib.pyplot as plt
plt.imshow(imagen, cmap='gray')
plt.title(f"Imagen DICOM - {ds.Modality}")
plt.colorbar()
plt.show()