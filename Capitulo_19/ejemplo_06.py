import tkinter as tk

ventana = tk.Tk()
ventana.title("Layout con pack()")

tk.Label(ventana, text="Superior", bg="lightblue").pack(side=tk.TOP, fill=tk.X)
tk.Label(ventana, text="Inferior", bg="lightgreen").pack(side=tk.BOTTOM, fill=tk.X)
tk.Label(ventana, text="Izquierda", bg="yellow").pack(side=tk.LEFT, fill=tk.Y)
tk.Label(ventana, text="Derecha", bg="orange").pack(side=tk.RIGHT, fill=tk.Y)
tk.Label(ventana, text="Centro", bg="pink").pack(expand=True, fill=tk.BOTH)

ventana.mainloop()