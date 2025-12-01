import tkinter as tk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Mi Primera Aplicación")
ventana.geometry("400x300")

# Agregar una etiqueta
etiqueta = tk.Label(ventana, text="¡Hola, Mundo!", font=("Arial", 20))
etiqueta.pack(pady=20)

# Agregar un botón
def saludar():
    etiqueta.config(text="¡Botón presionado!")

boton = tk.Button(ventana, text="Presióname", command=saludar)
boton.pack()

# Iniciar el loop de la aplicación
ventana.mainloop()