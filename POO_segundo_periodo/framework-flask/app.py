from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')    
def inicio():
    
        return render_template('index.html')
    
@app.route('/onepiece')    
def contacto():
    
        return render_template('onepiece.html')
    
@app.route('/argentina')    
def servicio():
    
        return render_template('argentina.html')


@app.route('/brasil')    
def estudiantes():
    
        return render_template('brasil.html')

@app.route('/cursos')    
def curso():
    
        return " 11a-11b "
    

@app.route('/saludo/<nombre>')    
def saludo(nombre):
    
        return f"hola,{nombre.capitalize()} bienvenido a flask"
    

    
if __name__== '__main__':
    app.run(debug=True)