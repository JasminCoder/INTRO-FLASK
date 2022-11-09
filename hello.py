#1.- pipenv install flask -> py -m pipenv install flask, python -m pipenv install flask
#2.- pipenv shell -> py -m pipenv shell, python -m pipenv shell
#3.- python nombre_archivo.py -> python3 nombre_archivo.py, py nombre_archivo.py

#LO Q SE EJECUTA EN MI TERMINAL
#pipenv install flask / despues de abrir la carpeta
#pipenv shell / para activar ambiente virtual (confirmar fijandose en la terminal (arriba a la derecha) q diga pipenv)
#control c + escribir exit / para salir del ambiente virtual 



from flask import Flask, render_template #importando flask para permitirnos crear una aplicacion web
#el 1° en minuscula pq es como una carpeta, el 2° serai un objeto x eso con mayuscula

app = Flask(__name__) #Creando una nueva instancia de la clase Flask llamada "app"

@app.route('/') #El decorador '@' asocia esa ruta con la función que vamos tener inmediatamente, la ruta es la URL
def hola_mundo():
    return 'Hola Mundo!'


#nueva ruta, q se llama con la misma url / se deja como comentario, para q no salga error al repetir el nombre de la funcion
#@app.route('/hola)
#def hola():
#    return 'Hola, como estás?'    



@app.route('/hola/<nombre>') #Para mi ruta /hola/_____ cualquier cosa después de /hola/ se va a pasar como variable nombre
def hola(nombre):
    return f'<h1>Hola {nombre}, cómo estás?</h1>'



#app.route + la ruta q queremos ejecutar (hello.py)
#@app.route('/hello')
#def hello():
#En lugar de devolver una cadena, devolvemos el resultado de un render_template
    #return render_template('hola.html', nombre="Elena", cantidad=10) #enviamos info (variables (Elena)) y en el html, 
    #usando jinja hacemos la funcion {% %}


#lo mismo de lo anterior, pero sin especificar el nombre, ni la cantidad (lo ponemos en la url de google, despues 
#de hello. Quedaria asi: http://127.0.0.1:5000/hello/jasmin/4 (cualquier nombre y cualquier cantidad + enter) si no se
#pone nombre y cantidad, no va a funcionar, no mostrará nada)
@app.route('/hello/<name>/<int:numero>')
def hello(name, numero):
    #En lugar de devolver una cadena, devolvemos el resultado de un render_template
    return render_template('hola.html', nombre=name, cantidad=numero)



if __name__=="__main__": #Asegura que el archivo se está ejecutando directamente y no desde un módulo diferente
    app.run(debug=True) #Ejecuta la aplicación