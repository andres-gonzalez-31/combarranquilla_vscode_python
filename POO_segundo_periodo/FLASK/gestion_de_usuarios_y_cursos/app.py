from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Conexión a la base de datos
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',         
        password='', 
        database='instituto'
    )

# Página de inicio
@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT c.id, c.nombre, COUNT(e.id) FROM cursos c LEFT JOIN estudiantes e ON c.id = e.curso_id GROUP BY c.id")
    cursos = cur.fetchall()
    conn.close()
    return render_template('index.html', cursos=cursos)

# De aqui para abajo esta todo lo relacionado con los CURSOS tanto la pagina de cuantos cursos hay, agregar, editar y eliminar. 

@app.route('/cursos')
def listar_cursos():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM cursos")
    cursos = cur.fetchall()
    conn.close()
    return render_template('cursos.html', cursos=cursos)

@app.route('/cursos/agregar', methods=['GET','POST'])
def agregar_curso():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO cursos (nombre, descripcion) VALUES (%s, %s)", (nombre, descripcion))
        conn.commit()
        conn.close()
        return redirect(url_for('listar_cursos'))
    return render_template('agregar_curso.html')

@app.route('/cursos/editar/<int:id>', methods=['GET', 'POST'])
def editar_curso(id):
    conn = get_db_connection()
    cur = conn.cursor()
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        cur.execute("UPDATE cursos SET nombre=%s, descripcion=%s WHERE id=%s", (nombre, descripcion, id))
        conn.commit()
        conn.close()
        return redirect(url_for('listar_cursos'))
    else:
        cur.execute("SELECT * FROM cursos WHERE id=%s", (id,))
        curso = cur.fetchone()
        conn.close()
        return render_template('editar_curso.html', curso=curso)

@app.route('/cursos/eliminar/<int:id>')
def eliminar_curso(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM cursos WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('listar_cursos'))

# De aqui para abajo esta todo lo relacionado con ESTUDIANTES lo mismo que arriba, listar, agregar, editar y eliminar..

@app.route('/estudiantes')
def listar_estudiantes():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT e.id, e.nombre, e.correo, c.nombre
        FROM estudiantes e LEFT JOIN cursos c ON e.curso_id = c.id
    """)
    estudiantes = cur.fetchall()

    cur.execute("SELECT * FROM cursos")
    cursos = cur.fetchall()

    conn.close()
    return render_template('estudiantes.html', estudiantes=estudiantes, cursos=cursos)

@app.route('/estudiantes/agregar', methods=['GET','POST'])
def agregar_estudiante():
    conn = get_db_connection()
    cur = conn.cursor()
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        curso_id = request.form['curso_id']
        cur.execute("INSERT INTO estudiantes (nombre, correo, curso_id) VALUES (%s, %s, %s)",
                    (nombre, correo, curso_id))
        conn.commit()
        conn.close()
        return redirect(url_for('listar_estudiantes'))
    else:
        cur.execute("SELECT * FROM cursos")
        cursos = cur.fetchall()
        conn.close()
        return render_template('agregar_estudiante.html', cursos=cursos)

@app.route('/estudiantes/editar/<int:id>', methods=['GET', 'POST'])
def editar_estudiante(id):
    conn = get_db_connection()
    cur = conn.cursor()
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        curso_id = request.form['curso_id']
        cur.execute("UPDATE estudiantes SET nombre=%s, correo=%s, curso_id=%s WHERE id=%s",
                    (nombre, correo, curso_id, id))
        conn.commit()
        conn.close()
        return redirect(url_for('listar_estudiantes'))
    else:
        cur.execute("SELECT * FROM estudiantes WHERE id=%s", (id,))
        estudiante = cur.fetchone()
        cur.execute("SELECT * FROM cursos")
        cursos = cur.fetchall()
        conn.close()
        return render_template('editar_estudiante.html', estudiante=estudiante, cursos=cursos)

@app.route('/estudiantes/eliminar/<int:id>')
def eliminar_estudiante(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM estudiantes WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('listar_estudiantes'))

# Ejecutar
if __name__ == '__main__':
    app.run(debug=True)
