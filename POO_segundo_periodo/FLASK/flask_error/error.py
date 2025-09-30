from flask import Flask, render_template_string

 

app = Flask(__name__)


 

@app.route("/")

def home():

    return "Bienvenido a mi aplicación Flask"

 

@app.route("/error")

def generar_error():

   

    return 1 / 0

 

@app.errorhandler(404)

def pagina_no_encontrada(error):

    return render_template_string("""

        <h1>404 - Página no encontrada</h1>

        <p>Lo sentimos, la página que buscas no existe.</p>

        <a href="/">Volver al inicio</a>

    """), 404

 

@app.errorhandler(500)

def error_interno(error):

    return render_template_string("""

        <h1>500 - Error interno</h1>

        <p>Ocurrió un problema en el servidor. Intenta de nuevo más tarde.</p>

        <a href="/">Volver al inicio</a>

    """), 500

 

if __name__ == "__main__":

    app.run(debug=False)
    
# se tiene que dejar en false para que los errores personalizados funcionen y los tome el errohandler por que si esta en true no los toma y muestra la pantalla de error de flask.