from flask import Flask, request

app = Flask(__name__)

# -------------------- MENÚ PRINCIPAL --------------------
@app.route("/")
def index():
    return """
    <h1>Menú Ejercicios Flask</h1>
    <ul>
        <li><a href='/tabla'>Ejercicio 1: Tabla de Multiplicar</a></li>
        <li><a href='/primos'>Ejercicio 2: Verificar Primo</a></li>
        <li><a href='/mayor'>Ejercicio 3: Mayor de Tres Números</a></li>
        <li><a href='/factorial'>Ejercicio 4: Factorial</a></li>
        <li><a href='/pares'>Ejercicio 5: Números Pares hasta N</a></li>
        <li><a href='/fibonacci'>Ejercicio 6: Serie Fibonacci</a></li>
        <li><a href='/calificaciones'>Ejercicio 7: Promedio de Calificaciones</a></li>
        <li><a href='/asteriscos'>Ejercicio 8: Triángulo con * </a></li>
        <li><a href='/impares'>Ejercicio 9: Impares entre dos números</a></li>
        <li><a href='/tabla_html'>Ejercicio 10: Generar Tabla HTML</a></li>
    </ul>
    """

# -------------------- EJ 1: TABLA MULTIPLICAR --------------------
@app.route("/tabla", methods=["GET", "POST"])
def tabla():
    if request.method == "POST":
        n = int(request.form["n"])
        filas = ""
        for i in range(1, 11):
            filas += f"<li>{n} x {i} = {n*i}</li>"
        return f"<h2>Tabla del {n}</h2><ul>{filas}</ul><a href='/tabla'>Volver</a>"
    return """
        <h2>Tabla de Multiplicar</h2>
        <form method="POST">
            Número: <input type="number" name="n" required>
            <button type="submit">Generar</button>
        </form>
        <a href='/'>Volver a menu</a>
    """

# -------------------- EJ 2: PRIMO --------------------
@app.route("/primos", methods=["GET", "POST"])
def primos():
    if request.method == "POST":
        n = int(request.form["n"])
        es_primo = True
        if n < 2:
            es_primo = False
        else:
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    es_primo = False
                    break
        return f"<h2>{n} {'es primo ✅' if es_primo else 'NO es primo ❌'}</h2><a href='/primos'>Volver</a>"
    return """
        <h2>Verificar Primo</h2>
        <form method="POST">
            Número: <input type="number" name="n" required>
            <button type="submit">Verificar</button>
        </form>
        <a href='/'>Volver a menu</a>
    """

# -------------------- EJ 3: MAYOR DE TRES --------------------
@app.route("/mayor", methods=["GET", "POST"])
def mayor():
    if request.method == "POST":
        nums = [int(request.form["n1"]), int(request.form["n2"]), int(request.form["n3"])]
        return f"<h2>El mayor es: {max(nums)}</h2><a href='/mayor'>Volver</a>"
    return """
        <h2>Mayor de tres números</h2>
        <form method="POST">
            N1: <input type="number" name="n1"><br>
            N2: <input type="number" name="n2"><br>
            N3: <input type="number" name="n3"><br>
            <button type="submit">Calcular</button>
        </form>
    """

# -------------------- EJ 4: FACTORIAL --------------------
@app.route("/factorial", methods=["GET", "POST"])
def factorial():
    if request.method == "POST":
        n = int(request.form["n"])
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return f"<h2>Factorial de {n} = {fact}</h2><a href='/factorial'>Volver</a>"
    return """
        <h2>Factorial</h2>
        <form method="POST">
            Número: <input type="number" name="n" required>
            <button type="submit">Calcular</button>
        </form>
    """

# -------------------- EJ 5: PARES --------------------
@app.route("/pares", methods=["GET", "POST"])
def pares():
    if request.method == "POST":
        n = int(request.form["n"])
        lista = [str(i) for i in range(2, n+1, 2)]
        return f"<h2>Pares hasta {n}:</h2><p>{', '.join(lista)}</p><a href='/pares'>Volver</a>"
    return """
        <h2>Pares hasta N</h2>
        <form method="POST">
            Número: <input type="number" name="n" required>
            <button type="submit">Generar</button>
        </form>
    """

# -------------------- EJ 6: FIBONACCI --------------------
@app.route("/fibonacci", methods=["GET", "POST"])
def fibonacci():
    if request.method == "POST":
        n = int(request.form["n"])
        serie = [0, 1]
        while len(serie) < n:
            serie.append(serie[-1] + serie[-2])
        return f"<h2>Fibonacci ({n} términos):</h2><p>{serie}</p><a href='/fibonacci'>Volver</a>"
    return """
        <h2>Serie Fibonacci</h2>
        <form method="POST">
            Términos: <input type="number" name="n" required>
            <button type="submit">Generar</button>
        </form>
    """

# -------------------- EJ 7: PROMEDIO --------------------
@app.route("/calificaciones", methods=["GET", "POST"])
def calificaciones():
    if request.method == "POST":
        notas = [float(request.form[f"n{i}"]) for i in range(1, 6)]
        promedio = sum(notas) / 5
        estado = "Aprobado ✅" if promedio >= 3.0 else "Reprobado ❌"
        return f"<h2>Promedio: {promedio:.2f} - {estado}</h2><a href='/calificaciones'>Volver</a>"
    return """
        <h2>Promedio de 5 calificaciones</h2>
        <form method="POST">
            Nota 1: <input type="number" step="0.1" name="n1"><br>
            Nota 2: <input type="number" step="0.1" name="n2"><br>
            Nota 3: <input type="number" step="0.1" name="n3"><br>
            Nota 4: <input type="number" step="0.1" name="n4"><br>
            Nota 5: <input type="number" step="0.1" name="n5"><br>
            <button type="submit">Calcular</button>
        </form>
    """

# -------------------- EJ 8: TRIÁNGULO --------------------
@app.route("/asteriscos", methods=["GET", "POST"])
def asteriscos():
    if request.method == "POST":
        n = int(request.form["n"])
        tri = ""
        for i in range(1, n+1):
            tri += "*" * i + "<br>"
        return f"<h2>Triángulo</h2><pre>{tri}</pre><a href='/asteriscos'>Volver</a>"
    return """
        <h2>Triángulo de asteriscos</h2>
        <form method="POST">
            Filas: <input type="number" name="n" required>
            <button type="submit">Generar</button>
        </form>
    """

# -------------------- EJ 9: IMPARES --------------------
@app.route("/impares", methods=["GET", "POST"])
def impares():
    if request.method == "POST":
        a = int(request.form["a"])
        b = int(request.form["b"])
        lista = [str(i) for i in range(a, b+1) if i % 2 != 0]
        return f"<h2>Impares entre {a} y {b}:</h2><p>{', '.join(lista)}</p><a href='/impares'>Volver</a>"
    return """
        <h2>Impares entre dos números</h2>
        <form method="POST">
            Inicio: <input type="number" name="a"><br>
            Fin: <input type="number" name="b"><br>
            <button type="submit">Generar</button>
        </form>
    """

# -------------------- EJ 10: TABLA HTML --------------------
@app.route("/tabla_html", methods=["GET", "POST"])
def tabla_html():
    if request.method == "POST":
        n = int(request.form["n"])
        filas = ""
        for i in range(1, n+1):
            filas += f"<tr><td>{i}</td><td>{i**2}</td></tr>"
        return f"""
            <h2>Tabla de Números y Cuadrados</h2>
            <table border=1>
                <tr><th>Número</th><th>Cuadrado</th></tr>
                {filas}
            </table>
            <a href='/tabla_html'>Volver</a>
        """
    return """
        <h2>Tabla de cuadrados</h2>
        <form method="POST">
            N: <input type="number" name="n" required>
            <button type="submit">Generar</button>
        </form>
    """

# -------------------- MAIN --------------------
if __name__ == "__main__":
    app.run(debug=True)
