from flask import Flask, request

app = Flask(__name__)

# -------------------- MENÚ PRINCIPAL --------------------
@app.route("/") 
def index():
    return """
    <h1>Menú principal</h1>
    <ul>
      <li><a href='/ejercicio1'>Ejercicio 1: Calcular Nota</a></li>
      <li><a href='/ejercicio2'>Ejercicio 2: Ordenar Números</a></li>
      <li><a href='/ejercicio3'>Ejercicio 3: Calculadora</a></li>
      <li><a href='/ejercicio4'>Ejercicio 4: Contador de Palabras</a></li>
      <li><a href='/ejercicio5'>Ejercicio 5: Tabla de Multiplicar</a></li>
      <li><a href='/ejercicio6'>Ejercicio 6: Conversor de Monedas</a></li>
      <li><a href='/ejercicio7'>Ejercicio 7: IMC (Índice de Masa Corporal)</a></li>
      <li><a href='/ejercicio8'>Ejercicio 8: Formulario de Contacto</a></li>
      <li><a href='/ejercicio9'>Ejercicio 9: Portafolio Simple</a></li>
      <li><a href='/ejercicio10'>Ejercicio 10: Generador de Cuadrados</a></li>
    </ul>
    """

# -------------------- EJERCICIO 1: Calcular Nota --------------------
@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":
        try:
            n1 = float(request.form["n1"])
            n2 = float(request.form["n2"])
            n3 = float(request.form["n3"])
            promedio = (n1 * 0.3) + (n2 * 0.3) + (n3 * 0.4)
            resultado = "✅ Aprobó" if promedio >= 3.0 else "❌ No aprobó"
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
            Nota 1: <input type="number" step="0.1" name="n1" required><br><br>
            Nota 2: <input type="number" step="0.1" name="n2" required><br><br>
            Nota 3: <input type="number" step="0.1" name="n3" required><br><br>
            <button type="submit">Calcular</button>
        </form>
        <a href='/'>Volver al menú</a>
    """

# -------------------- EJERCICIO 2: Ordenar Números --------------------
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

# -------------------- EJERCICIO 3: Calculadora --------------------
@app.route("/ejercicio3", methods=["GET", "POST"])
def ejercicio3():
    if request.method == "POST":
        try:
            n1 = float(request.form["n1"])
            n2 = float(request.form["n2"])
            op = request.form["op"]
            if op == "suma":
                res = n1 + n2
            elif op == "resta":
                res = n1 - n2
            elif op == "multi":
                res = n1 * n2
            else:
                res = n1 / n2 if n2 != 0 else "Error (división por cero)"
            return f"<h2>Resultado: {res}</h2><a href='/ejercicio3'>Volver</a>"
        except:
            return "<p>Error en los datos</p><a href='/ejercicio3'>Volver</a>"
    return """
        <h2>Ejercicio 3: Calculadora</h2>
        <form method="POST">
            Número 1: <input type="number" step="any" name="n1" required><br><br>
            Número 2: <input type="number" step="any" name="n2" required><br><br>
            Operación:
            <select name="op">
                <option value="suma">Sumar</option>
                <option value="resta">Restar</option>
                <option value="multi">Multiplicar</option>
                <option value="div">Dividir</option>
            </select><br><br>
            <button type="submit">Calcular</button>
        </form>
        <a href='/'>Volver al menú</a>
    """

# -------------------- EJERCICIO 4: Contador de Palabras --------------------
@app.route("/ejercicio4", methods=["GET", "POST"])
def ejercicio4():
    if request.method == "POST":
        texto = request.form["texto"]
        palabras = len(texto.split())
        return f"<h2>El texto tiene {palabras} palabras</h2><a href='/ejercicio4'>Volver</a>"
    return """
        <h2>Ejercicio 4: Contador de Palabras</h2>
        <form method="POST">
            <textarea name="texto" rows="4" cols="40" required></textarea><br><br>
            <button type="submit">Contar</button>
        </form>
        <a href='/'>Volver al menú</a>
    """

# -------------------- EJERCICIO 5: Tabla de Multiplicar --------------------
@app.route("/ejercicio5", methods=["GET", "POST"])
def ejercicio5():
    if request.method == "POST":
        try:
            num = int(request.form["num"])
            tabla = "".join([f"<li>{num} x {i} = {num*i}</li>" for i in range(1, 11)])
            return f"<h2>Tabla del {num}</h2><ul>{tabla}</ul><a href='/ejercicio5'>Volver</a>"
        except:
            return "<p>Error</p><a href='/ejercicio5'>Volver</a>"
    return """
        <h2>Ejercicio 5: Tabla de Multiplicar</h2>
        <form method="POST">
            Número: <input type="number" name="num" required><br><br>
            <button type="submit">Generar</button>
        </form>
        <a href='/'>Volver al menú</a>
    """

# -------------------- EJERCICIO 6: Conversor de Monedas --------------------
@app.route("/ejercicio6", methods=["GET", "POST"])
def ejercicio6():
    if request.method == "POST":
        try:
            pesos = float(request.form["pesos"])
            dolares = pesos / 4000  # tasa fija ejemplo
            return f"<h2>{pesos} COP = {dolares:.2f} USD</h2><a href='/ejercicio6'>Volver</a>"
        except:
            return "<p>Error</p><a href='/ejercicio6'>Volver</a>"
    return """
        <h2>Ejercicio 6: Conversor de Monedas</h2>
        <form method="POST">
            Pesos colombianos: <input type="number" step="any" name="pesos" required><br><br>
            <button type="submit">Convertir</button>
        </form>
        <a href='/'>Volver al menú</a>
    """

# -------------------- EJERCICIO 7: IMC --------------------
@app.route("/ejercicio7", methods=["GET", "POST"])
def ejercicio7():
    if request.method == "POST":
        try:
            peso = float(request.form["peso"])
            altura = float(request.form["altura"])
            imc = peso / (altura ** 2)
            estado = "Normal" if 18.5 <= imc < 25 else "Fuera de rango"
            return f"<h2>IMC: {imc:.2f} ({estado})</h2><a href='/ejercicio7'>Volver</a>"
        except:
            return "<p>Error</p><a href='/ejercicio7'>Volver</a>"
    return """
        <h2>Ejercicio 7: Índice de Masa Corporal</h2>
        <form method="POST">
            Peso (kg): <input type="number" step="any" name="peso" required><br><br>
            Altura (m): <input type="number" step="any" name="altura" required><br><br>
            <button type="submit">Calcular</button>
        </form>
        <a href='/'>Volver al menú</a>
    """

# -------------------- EJERCICIO 8: Formulario de Contacto --------------------
@app.route("/ejercicio8", methods=["GET", "POST"])
def ejercicio8():
    if request.method == "POST":
        nombre = request.form["nombre"]
        mensaje = request.form["mensaje"]
        return f"<h2>Gracias {nombre}, recibimos tu mensaje:</h2><p>{mensaje}</p><a href='/ejercicio8'>Volver</a>"
    return """
        <h2>Ejercicio 8: Formulario de Contacto</h2>
    <form method="POST">
            Nombre: <input type="text" name="nombre" required><br><br>
            Mensaje:<br><textarea name="mensaje" required></textarea><br><br>
            <button type="submit">Enviar</button>
        </form>
        <a href='/'>Volver al menú</a>
    """

# -------------------- EJERCICIO 9: Portafolio Simple --------------------
@app.route("/ejercicio9")
def ejercicio9():
    return """
        <h2>Ejercicio 9: Portafolio</h2>
        <h3>Mi Nombre</h3>
        <p>Desarrollador Web | Python | Flask</p>
        <ul>
            <li>Proyecto 1: Calculadora en Flask</li>
            <li>Proyecto 2: CRUD de Usuarios</li>
            <li>Proyecto 3: API con Flask</li>
        </ul>
        <a href='/'>Volver al menú</a>
    """

# -------------------- EJERCICIO 10: Generador de Cuadrados --------------------
@app.route("/ejercicio10", methods=["GET", "POST"])
def ejercicio10():
    if request.method == "POST":
        try:
            n = int(request.form["n"])
            lista = [i**2 for i in range(1, n+1)]
            return f"<h2>Cuadrados hasta {n}</h2><p>{lista}</p><a href='/ejercicio10'>Volver</a>"
        except:
            return "<p>Error</p><a href='/ejercicio10'>Volver</a>"
    return """
        <h2>Ejercicio 10: Generador de Cuadrados</h2>
        <form method="POST">
            Número: <input type="number" name="n" required><br><br>
            <button type="submit">Generar</button>
        </form>
        <a href='/'>Volver al menú</a>
    """

# -------------------- MAIN --------------------
if __name__ == "__main__":
    app.run(debug=True)
