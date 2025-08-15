import tkinter as tk
from tkinter import ttk

class CambiadorDeColor(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Cambiar Color de Fondo")
        self.geometry("300x150")
        self.resizable(False, False)

        # Diccionario de colores (el nombre del color como clave y el valor hexadecimal como valor)
        self.colores = {
            "Rojo": "red",
            "Verde": "green",
            "Azul": "blue",
            "Amarillo": "yellow",
            "Naranja": "orange",
            "Morado": "purple",
            "Gris": "gray",
            "Blanco": "white",
            "Negro": "black"
        }

        # Etiqueta de instrucción
        tk.Label(self, text="Selecciona un color:", font=("Arial", 12)).pack(pady=10)

        # Combobox
        self.combo_colores = ttk.Combobox(self, values=list(self.colores.keys()), state="readonly")
        self.combo_colores.pack(pady=10)
        self.combo_colores.set("Rojo")  # Establece un color por defecto

        # Vincular el evento de selección del Combobox a la función cambiar_color
        self.combo_colores.bind("<<ComboboxSelected>>", self.cambiar_color)

    def cambiar_color(self, event):
        """Cambia el color de fondo de la ventana según la selección del Combobox."""
        color_seleccionado = self.combo_colores.get()
        color_hex = self.colores[color_seleccionado]
        
        self.config(bg=color_hex)
        
if __name__ == "__main__":
    app = CambiadorDeColor()
    app.mainloop()