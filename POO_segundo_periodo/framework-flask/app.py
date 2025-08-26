from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')    
def inicio():
    
        return render_template('index.html')
    
@app.route('/contacto')    
def contacto():
    
        return "¡pagina de contacto "
    
@app.route('/servicio')    
def servicio():
    
        return " luz,agua,gas "


@app.route('/estudiantes')    
def estudiantes():
    
        return " colegios"

@app.route('/cursos')    
def curso():
    
        return " 11a-11b "
    

@app.route('/saludo/<nombre>')    
def saludo(nombre):
    
        return f"hola,{nombre.capitalize()} bienvenido a flask"
    

    
if __name__== '__main__':
    app.run(debug=True)