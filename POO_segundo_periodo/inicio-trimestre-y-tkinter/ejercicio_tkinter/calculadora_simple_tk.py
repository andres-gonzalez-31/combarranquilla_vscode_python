import tkinter as tk

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora Simple")
        self.geometry("300x250")  # Aumentamos el tamaño para el nuevo botón
        self.resizable(False, False)

        frame_entradas = tk.Frame(self)
        frame_entradas.pack(pady=10 )

        self.entrada1 = tk.Entry(frame_entradas, width=10)
        self.entrada1.pack(side=tk.LEFT, padx=5)

        self.entrada2 = tk.Entry(frame_entradas, width=10)
        self.entrada2.pack(side=tk.LEFT, padx=5)

        frame_botones = tk.Frame(self)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="+", command=self.sumar).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botones, text="-", command=self.restar).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botones, text="*", command=self.multiplicar).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botones, text="/", command=self.dividir).pack(side=tk.LEFT, padx=5)

        tk.Button(self, text="Limpiar", command=self.limpiar).pack(pady=10)

        self.etiqueta_resultado = tk.Label(self, text="Resultado: ", font=("Arial", 12))
        self.etiqueta_resultado.pack(pady=10)

    def obtener_numeros(self):
        """Intenta obtener los números de las cajas de texto y maneja errores."""
        try:
            num1 = float(self.entrada1.get())
            num2 = float(self.entrada2.get())
            return num1, num2
        except ValueError:
            self.etiqueta_resultado.config(text="Error: Ingresa números válidos")
            return None, None

    def sumar(self):
        num1, num2 = self.obtener_numeros()
        if num1 is not None and num2 is not None:
            resultado = num1 + num2
            self.etiqueta_resultado.config(text=f"Resultado: {resultado}")

    def restar(self):
        num1, num2 = self.obtener_numeros()
        if num1 is not None and num2 is not None:
            resultado = num1 - num2
            self.etiqueta_resultado.config(text=f"Resultado: {resultado}")

    def multiplicar(self):
        num1, num2 = self.obtener_numeros()
        if num1 is not None and num2 is not None:
            resultado = num1 * num2
            self.etiqueta_resultado.config(text=f"Resultado: {resultado}")

    def dividir(self):
        num1, num2 = self.obtener_numeros()
        if num1 is not None and num2 is not None:
            if num2 != 0:
                resultado = num1 / num2
                self.etiqueta_resultado.config(text=f"Resultado: {resultado}")
            else:
                self.etiqueta_resultado.config(text="Error: División por cero")

    def limpiar(self):
        """Borra el contenido de las entradas y reinicia la etiqueta de resultado."""
        self.entrada1.delete(0, tk.END) 
        self.entrada2.delete(0, tk.END)  
        self.etiqueta_resultado.config(text="Resultado: ")

if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()