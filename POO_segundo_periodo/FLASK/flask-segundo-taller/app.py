from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/condicionales')    
def condicionales():
    
        return render_template('index.html', equipo="bogota")

# @app.route('/formulario', methods=['GET','POST'])    
# def formulario():
#         if request.method == 'POST':
#                 nombre = request.form ['nombre']
#                 correo = request.form ['correo']
#                 return render_template('response.html', nombre=nombre, correo=correo)
#         return render_template('form.html')

@app.route('/suma', methods=['GET','POST'])    
def suma():
        if request.method == 'POST':
                primero = request.form ['primero']
                segundo = request.form ['segundo']
                
                primero = int(primero)
                segundo = int(segundo)
                
                total = primero + segundo 
                return render_template('suma.html', total=total)
        return render_template('suma.html')
    
    
if __name__== '__main__':
    app.run(debug=True)