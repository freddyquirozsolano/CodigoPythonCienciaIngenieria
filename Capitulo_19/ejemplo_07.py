import tkinter as tk

ventana = tk.Tk()
ventana.title("Layout con grid()")

# Formulario de registro
tk.Label(ventana, text="Nombre:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
tk.Entry(ventana).grid(row=0, column=1, padx=10, pady=5)

tk.Label(ventana, text="Email:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
tk.Entry(ventana).grid(row=1, column=1, padx=10, pady=5)

tk.Label(ventana, text="Edad:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
tk.Entry(ventana).grid(row=2, column=1, padx=10, pady=5)

tk.Button(ventana, text="Registrar").grid(row=3, column=0, columnspan=2, pady=10)

ventana.mainloop()