import tkinter as tk
from tkinter import messagebox

class ListaDeTareas(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Lista de Tareas")
        self.geometry("350x300")
        self.resizable(False, False)

        frame_principal = tk.Frame(self)
        frame_principal.pack(pady=10)

        self.lista_tareas = tk.Listbox(
            frame_principal,
            width=40,
            height=10,
            bg="white",
            fg="black",
            font=("Arial", 10),
            selectbackground="#a6a6a6",
            activestyle="none"
        )
        self.lista_tareas.pack(side=tk.LEFT, fill=tk.BOTH)

        scrollbar = tk.Scrollbar(frame_principal)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.lista_tareas.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.lista_tareas.yview)

        self.entrada_tarea = tk.Entry(self, width=40)
        self.entrada_tarea.pack(pady=10)
        self.entrada_tarea.bind("<Return>", self.agregar_tarea) # Permite agregar con la tecla Enter

        frame_botones = tk.Frame(self)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar Tarea", command=self.agregar_tarea).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botones, text="Eliminar Tarea", command=self.eliminar_tarea).pack(side=tk.LEFT, padx=5)

    def agregar_tarea(self, event=None):
        """Agrega la tarea de la caja de texto a la lista."""
        tarea = self.entrada_tarea.get()
        if tarea:
            self.lista_tareas.insert(tk.END, tarea)
            self.entrada_tarea.delete(0, tk.END) 
        else:
            messagebox.showwarning("Advertencia", "Debes escribir una tarea.")

    def eliminar_tarea(self):
        """Elimina la tarea seleccionada de la lista."""
        try:
            indice_seleccionado = self.lista_tareas.curselection()
            if indice_seleccionado:
                self.lista_tareas.delete(indice_seleccionado[0])
            else:
                messagebox.showwarning("Advertencia", "Debes seleccionar una tarea para eliminar.")
        except IndexError:
            messagebox.showwarning("Advertencia", "No hay tareas para eliminar.")

if __name__ == "__main__":
    app = ListaDeTareas()
    app.mainloop()