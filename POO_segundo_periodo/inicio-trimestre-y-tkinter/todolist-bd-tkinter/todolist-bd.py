import tkinter as tk
from tkinter import messagebox
import mysql.connector

# -------------------------
# Conexión a la base de datos
# -------------------------
def conectar():
    return mysql.connector.connect(
        host="localhost",   # tu host
        user="root",        # tu usuario de mysql/phpmyadmin
        password="",        # tu contraseña si tienes
        database="todolist-comba"
    )

# -------------------------
# Funciones CRUD
# -------------------------
def cargar_tareas():
    listbox.delete(0, tk.END)
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, description FROM tasks")
    for row in cursor.fetchall():
        listbox.insert(tk.END, f"{row[0]} - {row[1]}")
    conn.close()

def agregar_tarea():
    tarea = entry.get()
    if tarea.strip() == "":
        messagebox.showwarning("Error", "La tarea no puede estar vacía")
        return
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (description) VALUES (%s)", (tarea,))
    conn.commit()
    conn.close()
    entry.delete(0, tk.END)
    cargar_tareas()

def eliminar_tarea():
    try:
        seleccion = listbox.get(listbox.curselection())
        tarea_id = seleccion.split(" - ")[0]
    except:
        messagebox.showwarning("Error", "Selecciona una tarea para eliminar")
        return

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=%s", (tarea_id,))
    conn.commit()
    conn.close()
    cargar_tareas()

def consultar_tarea():
    try:
        seleccion = listbox.get(listbox.curselection())
        tarea_id = seleccion.split(" - ")[0]
    except:
        messagebox.showwarning("Error", "Selecciona una tarea para consultar")
        return

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT description FROM tasks WHERE id=%s", (tarea_id,))
    tarea = cursor.fetchone()
    conn.close()
    if tarea:
        messagebox.showinfo("Consulta", f"Tarea: {tarea[0]}")
    else:
        messagebox.showwarning("Error", "No se encontró la tarea")

# -------------------------
# Interfaz Tkinter con estilo
# -------------------------
root = tk.Tk()
root.title("To-Do List con MySQL")
root.geometry("520x450")
root.config(bg="#f4f6f9")  # Fondo general bonito (gris claro)

# -------------------------
# Caja de entrada
# -------------------------
entry = tk.Entry(
    root, 
    width=40, 
    font=("Arial", 12), 
    bg="#ffffff", 
    fg="#333333", 
    relief="solid", 
    bd=1, 
    highlightbackground="#4a90e2", 
    highlightcolor="#4a90e2", 
    highlightthickness=1
)
entry.pack(pady=10)

# -------------------------
# Botones con estilo
# -------------------------
btn_style = {
    "font": ("Arial", 11, "bold"),
    "bg": "#4a90e2",
    "fg": "white",
    "activebackground": "#357ABD",
    "activeforeground": "white",
    "relief": "flat",
    "width": 18,
    "height": 1,
    "bd": 0,
    "pady": 5
}

btn_add = tk.Button(root, text="➕ Agregar Tarea", command=agregar_tarea, **btn_style)
btn_add.pack(pady=5)

btn_delete = tk.Button(root, text="🗑 Eliminar Tarea", command=eliminar_tarea, **btn_style)
btn_delete.pack(pady=5)

btn_consult = tk.Button(root, text="🔍 Consultar Tarea", command=consultar_tarea, **btn_style)
btn_consult.pack(pady=5)

btn_reload = tk.Button(root, text="🔄 Recargar Tareas", command=cargar_tareas, **btn_style)
btn_reload.pack(pady=5)

# -------------------------
# Listbox con estilo
# -------------------------
listbox = tk.Listbox(
    root, 
    width=50, 
    height=10, 
    font=("Arial", 11), 
    bg="#ffffff", 
    fg="#333333", 
    selectbackground="#4a90e2", 
    selectforeground="white", 
    relief="solid", 
    bd=1, 
    highlightbackground="#4a90e2", 
    highlightthickness=1
)
listbox.pack(pady=15)

# -------------------------
# Cargar tareas al inicio
# -------------------------
cargar_tareas()

root.mainloop()