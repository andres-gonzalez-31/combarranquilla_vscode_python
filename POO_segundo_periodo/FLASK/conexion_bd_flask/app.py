from flask import Flask, render_template, request, redirect, url_for
from db import get_connection

app = Flask(__name__)

# Página principal (listar productos)
@app.route('/')
def index():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', productos=productos)


# Crear producto
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO productos (nombre, precio) VALUES (%s, %s)", (nombre, precio))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create.html')


# Editar producto
@app.route('/edit/<int:id_productos>', methods=['GET', 'POST'])
def edit(id_productos):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        cursor.execute("UPDATE productos SET nombre=%s, precio=%s WHERE id_productos=%s", (nombre, precio, id_productos))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    cursor.execute("SELECT * FROM productos WHERE id_productos=%s", (id_productos,))
    producto = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('edit.html', producto=producto)


# Eliminar producto
@app.route('/delete/<int:id_productos>')
def delete(id_productos):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id_productos=%s", (id_productos,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
