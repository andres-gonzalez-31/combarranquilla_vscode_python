from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# Lista para almacenar los datos
datos = []

@app.route("/")
def index():
    return """
    <h1>Menú principal</h1>
    <ul>
        <li><a href='/registros'>Registros</a></li>
        <li><a href='/usuarios'>Usuarios</a></li>
    </ul>
    """

@app.route("/registros", methods=["GET", "POST"])
def registros():
    if request.method == "POST":
        nombre = request.form["nombre"]
        correo = request.form["correo"]
        edad = request.form["edad"]
        # Guardamos los datos directamente en la lista
        datos.append({
            "nombre": nombre,
            "correo": correo,
            "edad": edad
        })
        return redirect(url_for("usuarios"))

    return """
        <h2>Formulario de Registro</h2>
        <form method="POST">
            Nombre: <input type="text" name="nombre" required><br><br>
            Correo: <input type="email" name="correo" required><br><br>
            Edad: <input type="number" name="edad" required><br><br>
            <button type="submit">Enviar</button>
        </form>
        <a href='/'>Volver al menú</a>
    """

@app.route("/usuarios", methods=["GET"])
def usuarios():
    rows = ""
    for idx, usuario in enumerate(datos):
        rows += f"""
        <tr>
            <td>{usuario['nombre']}</td>
            <td>{usuario['correo']}</td>
            <td>{usuario['edad']}</td>
            <td><a href='/usuario/{idx}'>Ver Detalles</a></td>
        </tr>
        """
    
    return f"""
        <h2>Usuarios Registrados</h2>
        <table border="1">
            <tr>
                <th>Nombre</th>
                <th>Correo</th>
                <th>Edad</th>
                <th>Detalles</th>
            </tr>
            {rows}
        </table><br>
        <a href='/'>Volver al menú</a><br>
        <a href='/registros'>Registrar otro usuario</a>
    """

@app.route("/usuario/<int:idx>")
def usuario_detalle(idx):
    if 0 <= idx < len(datos):
        usuario = datos[idx]
        return f"""
            <h2>Detalle del Usuario</h2>
            <p><strong>Nombre:</strong> {usuario['nombre']}</p>
            <p><strong>Correo:</strong> {usuario['correo']}</p>
            <p><strong>Edad:</strong> {usuario['edad']}</p>
            <a href='/usuarios'>Volver a la lista</a>
        """
    else:
        return "<h2>Usuario no encontrado</h2><a href='/usuarios'>Volver</a>"

if __name__ == '__main__':
    app.run(debug=True)
