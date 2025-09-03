from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h1>Menú principal</h1>
    <ul>
      <li><a href='/ejercicio1'>Ejercicio 1: Calcular Nota</a></li>
      <li><a href='/ejercicio2'>Ejercicio 2: Ordenar Números</a></li>
    </ul>
    """

# -------------------- EJERCICIO 1 --------------------
@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":
        try:
            n1 = float(request.form["n1"])
            n2 = float(request.form["n2"])
            n3 = float(request.form["n3"])
            # Cálculo del promedio ponderado
            promedio = (n1 * 0.3) + (n2 * 0.3) + (n3 * 0.4)
            if promedio >= 4.0:
                resultado = "✅ Aprobó"
            else: 
                resultado="❌ No aprobó"
            return f"""
                <h2>Resultado</h2>
                <p>Promedio: {promedio:.2f}</p>
                <p>{resultado}</p>
                <a href='/ejercicio1'>Volver</a>
            """
        except:
            return "<p>Error: ingrese valores válidos</p><a href='/ejercicio1'>Volver</a>"

    return """
        <h2>Ejercicio 1: Calcular Nota</h2>
        <form method="POST">
            Nota 1 (30%): <input type="number" step="0.1" name="n1" required><br><br>
            Nota 2 (30%): <input type="number" step="0.1" name="n2" required><br><br>
            Nota Final (40%): <input type="number" step="0.1" name="n3" required><br><br>
            <button type="submit">Calcular</button>
        </form>
        <a href='/'>Volver al menú</a>
    """
# -------------------- EJERCICIO 2 --------------------
@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    if request.method == "POST":
        try:
            nums = [
                float(request.form["n1"]),
                float(request.form["n2"]),
                float(request.form["n3"])
            ]
            nums.sort()
            return f"""
                <h2>Resultado</h2>
                <p>Números ordenados: {nums}</p>
                <a href='/ejercicio2'>Volver</a>
            """
        except:
            return "<p>Error: ingrese valores válidos</p><a href='/ejercicio2'>Volver</a>"

    return """
        <h2>Ejercicio 2: Ordenar Números</h2>
        <form method="POST">
            Número 1: <input type="number" step="any" name="n1" required><br><br>
            Número 2: <input type="number" step="any" name="n2" required><br><br>
            Número 3: <input type="number" step="any" name="n3" required><br><br>
            <button type="submit">Ordenar</button>
        </form>
        <a href='/'>Volver al menú</a>
    """


if __name__ == "__main__":
    app.run(debug=True)
