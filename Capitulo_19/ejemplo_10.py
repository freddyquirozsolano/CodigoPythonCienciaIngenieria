import tkinter as tk
from tkinter import ttk
import math

class PanelControlRobot:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("🤖 Control de Robot")
        self.ventana.geometry("600x500")
        
        # Variables
        self.velocidad = tk.IntVar(value=0)
        self.angulo = tk.IntVar(value=0)
        self.robot_x = 300
        self.robot_y = 250
        
        # Panel de controles
        frame_controles = tk.LabelFrame(
            self.ventana,
            text="Controles",
            font=("Arial", 12, "bold"),
            padx=20,
            pady=20
        )
        frame_controles.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        
        # Velocidad
        tk.Label(frame_controles, text="Velocidad:", font=("Arial", 10)).pack(anchor=tk.W)
        self.scale_velocidad = tk.Scale(
            frame_controles,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            variable=self.velocidad,
            length=200,
            command=self.actualizar_info
        )
        self.scale_velocidad.pack(pady=5)
        
        # Ángulo
        tk.Label(frame_controles, text="Ángulo:", font=("Arial", 10)).pack(anchor=tk.W, pady=(10, 0))
        self.scale_angulo = tk.Scale(
            frame_controles,
            from_=0,
            to=360,
            orient=tk.HORIZONTAL,
            variable=self.angulo,
            length=200,
            command=self.actualizar_info
        )
        self.scale_angulo.pack(pady=5)
        
        # Botones de control
        frame_botones = tk.Frame(frame_controles)
        frame_botones.pack(pady=20)
        
        tk.Button(
            frame_botones,
            text="⬆️ Adelante",
            command=self.mover_adelante,
            width=12
        ).grid(row=0, column=1, pady=5)
        
        tk.Button(
            frame_botones,
            text="⬅️ Izquierda",
            command=self.girar_izquierda,
            width=12
        ).grid(row=1, column=0, padx=5)
        
        tk.Button(
            frame_botones,
            text="⏹️ Detener",
            command=self.detener,
            bg='#f44336',
            fg='white',
            width=12
        ).grid(row=1, column=1)
        
        tk.Button(
            frame_botones,
            text="➡️ Derecha",
            command=self.girar_derecha,
            width=12
        ).grid(row=1, column=2, padx=5)
        
        tk.Button(
            frame_botones,
            text="⬇️ Atrás",
            command=self.mover_atras,
            width=12
        ).grid(row=2, column=1, pady=5)
        
        # Canvas para visualización
        self.canvas = tk.Canvas(
            self.ventana,
            width=400,
            height=400,
            bg='white',
            relief=tk.SUNKEN,
            borderwidth=2
        )
        self.canvas.pack(side=tk.RIGHT, padx=10, pady=10)
        
        # Dibujar robot inicial
        self.robot_id = self.canvas.create_oval(
            self.robot_x-15, self.robot_y-15,
            self.robot_x+15, self.robot_y+15,
            fill='blue',
            outline='black',
            width=2
        )
        
        # Dirección del robot
        self.direccion_id = self.canvas.create_line(
            self.robot_x, self.robot_y,
            self.robot_x, self.robot_y-25,
            fill='red',
            width=3,
            arrow=tk.LAST
        )
        
        # Información
        self.label_info = tk.Label(
            frame_controles,
            text="Velocidad: 0%\nÁngulo: 0°\nPosición: (300, 250)",
            font=("Courier", 10),
            justify=tk.LEFT,
            bg='#f0f0f0',
            relief=tk.SUNKEN,
            padx=10,
            pady=10
        )
        self.label_info.pack(pady=20, fill=tk.X)
    
    def actualizar_info(self, event=None):
        info = f"Velocidad: {self.velocidad.get()}%\n"
        info += f"Ángulo: {self.angulo.get()}°\n"
        info += f"Posición: ({int(self.robot_x)}, {int(self.robot_y)})"
        self.label_info.config(text=info)
        self.actualizar_direccion()
    
    def actualizar_direccion(self):
        angulo_rad = math.radians(self.angulo.get())
        fin_x = self.robot_x + 25 * math.sin(angulo_rad)
        fin_y = self.robot_y - 25 * math.cos(angulo_rad)
        self.canvas.coords(
            self.direccion_id,
            self.robot_x, self.robot_y,
            fin_x, fin_y
        )
    
    def mover_adelante(self):
        angulo_rad = math.radians(self.angulo.get())
        distancia = self.velocidad.get() / 5
        self.robot_x += distancia * math.sin(angulo_rad)
        self.robot_y -= distancia * math.cos(angulo_rad)
        self.actualizar_robot()
    
    def mover_atras(self):
        angulo_rad = math.radians(self.angulo.get())
        distancia = self.velocidad.get() / 5
        self.robot_x -= distancia * math.sin(angulo_rad)
        self.robot_y += distancia * math.cos(angulo_rad)
        self.actualizar_robot()
    
    def girar_izquierda(self):
        nuevo_angulo = (self.angulo.get() - 15) % 360
        self.angulo.set(nuevo_angulo)
        self.actualizar_info()
    
    def girar_derecha(self):
        nuevo_angulo = (self.angulo.get() + 15) % 360
        self.angulo.set(nuevo_angulo)
        self.actualizar_info()
    
    def detener(self):
        self.velocidad.set(0)
        self.actualizar_info()
    
    def actualizar_robot(self):
        # Mantener dentro de límites
        self.robot_x = max(20, min(380, self.robot_x))
        self.robot_y = max(20, min(380, self.robot_y))
        
        self.canvas.coords(
            self.robot_id,
            self.robot_x-15, self.robot_y-15,
            self.robot_x+15, self.robot_y+15
        )
        self.actualizar_direccion()
        self.actualizar_info()

# Ejecutar
if __name__ == "__main__":
    ventana = tk.Tk()
    app = PanelControlRobot(ventana)
    ventana.mainloop()