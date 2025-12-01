import tkinter as tk
from tkinter import messagebox

class CalculadoraIMC:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("🏥 Calculadora de IMC")
        self.ventana.geometry("400x350")
        self.ventana.resizable(False, False)
        
        # Configurar estilo
        self.ventana.configure(bg='#f0f0f0')
        
        # Título
        titulo = tk.Label(
            self.ventana,
            text="Calculadora de Índice de Masa Corporal",
            font=("Arial", 14, "bold"),
            bg='#f0f0f0'
        )
        titulo.pack(pady=20)
        
        # Frame para inputs
        frame_inputs = tk.Frame(self.ventana, bg='#f0f0f0')
        frame_inputs.pack(pady=10)
        
        # Peso
        tk.Label(
            frame_inputs,
            text="Peso (kg):",
            font=("Arial", 11),
            bg='#f0f0f0'
        ).grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
        
        self.entry_peso = tk.Entry(frame_inputs, font=("Arial", 11), width=15)
        self.entry_peso.grid(row=0, column=1, padx=10, pady=10)
        
        # Altura
        tk.Label(
            frame_inputs,
            text="Altura (m):",
            font=("Arial", 11),
            bg='#f0f0f0'
        ).grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)
        
        self.entry_altura = tk.Entry(frame_inputs, font=("Arial", 11), width=15)
        self.entry_altura.grid(row=1, column=1, padx=10, pady=10)
        
        # Botón calcular
        btn_calcular = tk.Button(
            self.ventana,
            text="Calcular IMC",
            command=self.calcular_imc,
            font=("Arial", 12, "bold"),
            bg='#4CAF50',
            fg='white',
            cursor='hand2',
            width=20,
            height=2
        )
        btn_calcular.pack(pady=20)
        
        # Resultado
        self.label_resultado = tk.Label(
            self.ventana,
            text="",
            font=("Arial", 12),
            bg='#f0f0f0'
        )
        self.label_resultado.pack(pady=10)
        
        self.label_clasificacion = tk.Label(
            self.ventana,
            text="",
            font=("Arial", 11, "italic"),
            bg='#f0f0f0'
        )
        self.label_clasificacion.pack()
    
    def calcular_imc(self):
        try:
            peso = float(self.entry_peso.get())
            altura = float(self.entry_altura.get())
            
            # Validaciones
            if peso <= 0 or altura <= 0:
                messagebox.showerror("Error", "Los valores deben ser positivos")
                return
            
            if altura > 3:
                messagebox.showwarning("Advertencia", "Altura parece incorrecta. ¿Ingresaste en metros?")
            
            # Calcular IMC
            imc = peso / (altura ** 2)
            
            # Clasificación
            if imc < 18.5:
                clasificacion = "Bajo peso"
                color = "#FFA500"  # Naranja
            elif imc < 25:
                clasificacion = "Peso normal"
                color = "#4CAF50"  # Verde
            elif imc < 30:
                clasificacion = "Sobrepeso"
                color = "#FF9800"  # Naranja oscuro
            else:
                clasificacion = "Obesidad"
                color = "#F44336"  # Rojo
            
            # Mostrar resultados
            self.label_resultado.config(
                text=f"Tu IMC es: {imc:.2f}",
                font=("Arial", 14, "bold")
            )
            
            self.label_clasificacion.config(
                text=f"Clasificación: {clasificacion}",
                fg=color,
                font=("Arial", 12, "bold")
            )
            
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos")

# Ejecutar aplicación
if __name__ == "__main__":
    ventana = tk.Tk()
    app = CalculadoraIMC(ventana)
    ventana.mainloop()