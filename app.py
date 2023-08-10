from flask import Flask, render_template
from load_data import LICENCIAS,PDFS,LOGO, NOMBREAPP
app = Flask(__name__)
data = {
        'nombreApp': NOMBREAPP,
        'titulo': '',
        'logo': LOGO,
        'licencias': LICENCIAS,
        'pdfs': PDFS
    }
@app.route('/')
def index():
    # return "<h1>Hola Mundo! </h1>"
    data['titulo'] =  'Inicio'
    return render_template('login.html',data= data)

@app.route('/login')
def login():
    data['titulo'] = 'Login de MyApp'
    return render_template('login.html',data= data)

@app.route('/home')
def home():
    data['titulo'] = 'Datos Cargados'
    return render_template("home.html",data= data)

@app.route('/asociados')
def asociados():
    data['titulo'] = 'PDF Asociacos'
    return render_template("asociados.html",data= data)



if __name__ ==  '__main__':
    app.run(debug= True) # port 5000 por defecto

# python app.py para ejecutar
