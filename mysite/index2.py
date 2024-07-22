from flask import Flask, render_template  # llamar al framework

app = Flask(__name__)  # guarda en una variable la ruta de inicio de la app

# Rutas de procesamiento (direccionan a algun lugar)
@app.route('/')    # método que crea una url
def home():        # función  que devuelve información al navegador
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/cursos')
def cursos():
    return render_template("cursos.html")

@app.route('/nosotros')
def nosotros():
    return render_template("nosotros.html")


@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/valid')
def valid():
    return render_template("valid.html")

@app.route('/alumnos')
def alumnos():
    return render_template("alumnos.html")

@app.route('/profile')
def profile():
    return render_template("profile.html")

# validamos si estamos en el archivo principal para que siempre se quede
# escuchando una peticion del usuario y si se cumple ejecuta el app.run
if __name__ == '__main__':
    app.run(debug=True) # avisamos que estamos en un entorno de prueba
                        # y se actualiza el servidor automaticamente
