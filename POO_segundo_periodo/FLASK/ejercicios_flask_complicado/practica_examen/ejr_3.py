from flask import Flask, request, redirect, url_for
import random
import datetime

app = Flask(__name__)

# -------------------- MENÚ --------------------
@app.route("/")
def index():
    return """
    <h1>Ejercicios Flask Avanzados</h1>
    <ul>
        <li><a href='/binario'>1. Convertir número a binario</a></li>
        <li><a href='/mayusculas'>2. Convertir texto a mayúsculas</a></li>
        <li><a href='/adivinar'>3. Juego: Adivina el número</a></li>
        <li><a href='/fecha'>4. Mostrar fecha y hora actual</a></li>
        <li><a href='/vocales'>5. Contar vocales en un texto</a></li>
        <li><a href='/redireccion'>6. Redirección de ruta</a></li>
        <li><a href='/reversa'>7. Invertir un texto</a></li>
        <li><a href='/tabla_ascii'>8. Código ASCII de un texto</a></li>
        <li><a href='/moneda'>9. Lanzar moneda</a></li>
        <li><a href='/temperatura'>10. Convertir Celsius a Fahrenheit</a></li>
    </ul>
    """

@app.route("/binario", methods=["GET", "POST"])
def binario():
    if request.method == "POST":
        n = int(request.form["n"])
        return f"<h2>El número {n} en binario es: {bin(n)[2:]}</h2><a href='/binario'>Volver</a>"
    return """
        <h2>Convertir a Binario</h2>
        <form method="POST">
            Número: <input type="number" name="n">
            <button type="submit">Convertir</button>
        </form>
        <a href='/'>Volver</a>
    """

@app.route("/mayusculas", methods=["GET", "POST"])
def mayusculas():
    if request.method == "POST":
        texto = request.form["texto"]
        return f"<h2>Resultado: {texto.upper()}</h2><a href='/mayusculas'>Volver</a>"
    return """
        <h2>Convertir a MAYÚSCULAS</h2>
        <form method="POST">
            Texto: <input type="text" name="texto">
            <button type="submit">Convertir</button>
        </form>
        <a href='/'>Volver</a>
    """

numero_secreto = random.randint(1, 10)

@app.route("/adivinar", methods=["GET", "POST"])
def adivinar():
    global numero_secreto
    if request.method == "POST":
        intento = int(request.form["n"])
        if intento == numero_secreto:
            numero_secreto = random.randint(1, 10)  # reinicia
            return "<h2>¡Correcto! 🎉</h2><a href='/adivinar'>Jugar otra vez</a>"
        elif intento < numero_secreto:
            return "<h2>Muy bajo ⬇️</h2><a href='/adivinar'>Intentar de nuevo</a>"
        else:
            return "<h2>Muy alto ⬆️</h2><a href='/adivinar'>Intentar de nuevo</a>"
    return """
        <h2>Adivina el número (1-10)</h2>
        <form method="POST">
            Intento: <input type="number" name="n">
            <button type="submit">Probar</button>
        </form>
        <a href='/'>Volver</a>
    """

@app.route("/fecha")
def fecha():
    ahora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return f"<h2>Fecha y hora actual: {ahora}</h2><a href='/'>Volver</a>"


@app.route("/vocales", methods=["GET", "POST"])
def vocales():
    if request.method == "POST":
        texto = request.form["texto"].lower()
        contador = sum(1 for c in texto if c in "aeiou")
        return f"<h2>El texto tiene {contador} vocales</h2><a href='/vocales'>Volver</a>"
    return """
        <h2>Contar vocales</h2>
        <form method="POST">
            Texto: <input type="text" name="texto">
            <button type="submit">Contar</button>
        </form>
        <a href='/'>Volver</a>
    """

@app.route("/redireccion")
def redireccion():
    return redirect(url_for("fecha"))

@app.route("/reversa", methods=["GET", "POST"])
def reversa():
    if request.method == "POST":
        texto = request.form["texto"]
        return f"<h2>Texto invertido: {texto[::-1]}</h2><a href='/reversa'>Volver</a>"
    return """
        <h2>Invertir texto</h2>
        <form method="POST">
            Texto: <input type="text" name="texto">
            <button type="submit">Invertir</button>
        </form>
        <a href='/'>Volver</a>
    """


@app.route("/tabla_ascii", methods=["GET", "POST"])
def tabla_ascii():
    if request.method == "POST":
        texto = request.form["texto"]
        filas = "".join([f"<tr><td>{c}</td><td>{ord(c)}</td></tr>" for c in texto])
        return f"""
            <h2>Tabla ASCII</h2>
            <table border=1>
                <tr><th>Carácter</th><th>Código</th></tr>
                {filas}
            </table>
            <a href='/tabla_ascii'>Volver</a>
        """
    return """
        <h2>Convertir texto a ASCII</h2>
        <form method="POST">
            Texto: <input type="text" name="texto">
            <button type="submit">Convertir</button>
        </form>
        <a href='/'>Volver</a>
    """

@app.route("/moneda")
def moneda():
    resultado = random.choice(["Cara", "Sello"])
    return f"<h2>Resultado: {resultado}</h2><a href='/moneda'>Volver a lanzar</a><br></br><a href='/'>Volver</a>"


@app.route("/temperatura", methods=["GET", "POST"])
def temperatura():
    if request.method == "POST":
        c = float(request.form["c"])
        f = (c * 9/5) + 32
        return f"<h2>{c}°C = {f:.2f}°F</h2><a href='/temperatura'>Volver</a>"
    return """
        <h2>Convertir Celsius a Fahrenheit</h2>
        <form method="POST">
            °C: <input type="number" step="0.1" name="c">
            <button type="submit">Convertir</button>
        </form>
        <a href='/'>Volver</a>
    """

if __name__ == "__main__":
    app.run(debug=True)
