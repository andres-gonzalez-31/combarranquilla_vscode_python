import tkinter as tk
from tkinter import messagebox
import mysql.connector


# ------------- conexion a MYSQL ----------------

def conectar():
    return mysql.connector.connect(
        host ="localhost",
        user="root",
        password="",
        database="testdb"
    )


# -------------- guardar datos en la base ----------------

def guardar_datos():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    correo = entry_correo.get()
    
    if not nombre or not edad or not correo:
        messagebox.showwarning("campos vacios","por favor completa todos los campos")
        return
    
    try:
        conn = conectar()
        cursor = conn.cursor()
        sql = "INSERT INTO personas (nombre, edad, correo) VALUES (%s, %s, %s)"
        valores = (nombre, edad, correo)
        cursor.execute(sql,valores)
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Exito","Datos guardados correctamente.")
        
        entry_nombre.delete(0,tk.END)
        entry_edad.delete(0,tk.END)
        entry_correo.delete(0,tk.END)
    except mysql.connector.Error as err:
        messagebox.showerror("error", f"error al guardar los datos: {err}")

# ----------- funcion eliminar datos ------------------
def eliminar_datos():
    nombre = entry_nombre.get()
    
    if not nombre:
        messagebox.showwarning("campos vacios","por favor completa todos los campos")
        return
    
    try:
        conn = conectar()
        cursor = conn.cursor()
        sql = "DELETE FROM personas WHERE nombre = %s"
        cursor.execute(sql,(nombre,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Exito"," dato eliminado correctamente.")
        
        entry_nombre.delete(0,tk.END)
    except mysql.connector.Error as err:
        messagebox.showerror("error", f"error al eliminar los datos: {err}")


# ---------------  funcion consultar datos -------------------------

def consultar_datos():
    nombre = entry_nombre.get()
    
    if not nombre:
        messagebox.showwarning("campos vacios","por favor completa todos los campos")
        return  
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM personas WHERE nombre = %s",(nombre))
        conn.commit()
        conn.close()
        messagebox.showinfo("Exito"," dato consultado correctamente.")
        
        entry_nombre.get()
    except mysql.connector.Error as err:
        messagebox.showerror("error", f"error al eliminar los datos: {err}")
        
    

ventana = tk.Tk()
ventana.title("formato de registro")
ventana.geometry("300x250")

tk.Label(ventana, text="nombre:").pack(pady=5)
entry_nombre = tk.Entry(ventana, width=30)
entry_nombre.pack()

tk.Label(ventana, text="edad:").pack(pady=5)
entry_edad = tk.Entry(ventana, width=30)
entry_edad.pack()

tk.Label(ventana, text="correo:").pack(pady=5)
entry_correo = tk.Entry(ventana, width=30)
entry_correo.pack()


bnt_guardar = tk.Button(ventana, text="guardar", command=guardar_datos, bg="green", fg="white")
bnt_guardar.pack( pady=15)
bnt_eliminar = tk.Button(ventana, text="eliminar", command=eliminar_datos, bg="red", fg="white")
bnt_eliminar.pack( pady=15,)
bnt_consultar = tk.Button(ventana, text="consultar", command=consultar_datos, bg="red", fg="white")
bnt_consultar.pack( pady=15,)


label_resultado = tk.Label(ventana, text="consultar", command font=("Arial", 12))
label_resultado.pack(pady=10)


ventana.mainloop()