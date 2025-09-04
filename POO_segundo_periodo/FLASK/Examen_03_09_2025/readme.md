## Question

- 1. ¿Que diferencia hay entre una ruta GET y una ruta POST?

>R//  el metodo GET solicita los datos  a diferencia del POST que envia los datos.

- 2. ¿Que sucede si dos funciones diferentes tienen la misma ruta en flask?

>R//  esto hace que mande error. 


- 3. ¿Que funcion de flask se utiliza para renderizar una plantilla html ?

>R// primero se descarga su paquete que es render_templates y luego eso hace que al momentode retornar algo antes de mandar la la vista que quieres renderizar le colocas render_template. ej:

```
@app.route('/')    
def condicionales():
    
        return render_template('index.html')
```

- 4. ¿Que ventaja tiene separar la logica python de las vistas en html?
  
>R// garantiza el uso de buenas practicas  y una buen recuerso de presentar un codigo limpio y ordenado

- 5. Que atributos del elemento form define como se envian los datos al servidor? 

>R//  se utiliza el el elemento **methods**

- 6. EXPLICA: con un ejemplo como acceder en flask a un valor enviado desde un formulario

>R//  para hacerle una peticion al formulario desde flask se deberia usar el **request.form**.
```
from flask import Flask, request

app=Flask(__name__)

@app.route('/formulario',methods=['GET','POST'])
def formulario():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        return f"<h2>Gracias {nombre,apellido}adios</p><a href='/formulario'>Volver</a>"
    return """
        <h2> Formulario de ejemplo</h2>
        <form method="POST">
            Nombre: <input type="text" name="nombre" required><br><br>
            apellido:<input type="text" name="apellido" required><br><br>
            <button type="submit">Enviar</button>
        </form>
    """
```
