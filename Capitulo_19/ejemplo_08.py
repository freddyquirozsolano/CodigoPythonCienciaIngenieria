import tkinter as tk

ventana = tk.Tk()
ventana.title("Layout con place()")
ventana.geometry("400x300")

tk.Label(ventana, text="Posición absoluta", bg="lightblue").place(x=100, y=50)
tk.Button(ventana, text="Botón").place(x=150, y=100, width=100, height=30)

ventana.mainloop()