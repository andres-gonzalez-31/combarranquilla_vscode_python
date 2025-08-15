import tkinter as tk

class ContadorClics(tk.Tk):
    def __init__(self):  # <- Aquí está la corrección
        super().__init__()

        self.geometry("300x200")
        self.title("Contador de Clics")
        self.resizable(False, False)

        self.contador = 0

        self.etiqueta = tk.Label(self, text="Clics: 0", font=("Arial", 14))
        self.etiqueta.pack(pady=10)

        self.boton = tk.Button(self, text="Clic aquí", command=self.incrementar)
        self.boton.pack(pady=10)

    def incrementar(self):
        self.contador += 1
        self.etiqueta.config(text=f"Clics: {self.contador}")

if __name__ == "__main__":
    app = ContadorClics()
    app.mainloop()