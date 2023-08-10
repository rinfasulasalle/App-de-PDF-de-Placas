from flask import Flask, render_template
from load_data import LICENCIAS,PDFS,LOGO
app = Flask(__name__)

@app.route('/')
def index():
    # return "<h1>Hola Mundo! </h1>"
    data = {
        'titulo': 'Inicio',
        'logo': LOGO,
        'licencias': LICENCIAS,
        'pdfs': PDFS
    }
    return render_template('index.html',data= data)

@app.route('/login')
def login():
    data = {
        'titulo': 'Login de MyApp',
        'logo': LOGO,
        'licencias': LICENCIAS,
        'pdfs': PDFS
    }
    return render_template('login.html',data= data)

@app.route('/home')
def home():
    data = {
        'titulo': 'PDFS Asociados',
        'logo': LOGO,
        'licencias': LICENCIAS,
        'pdfs': PDFS
    }
    return render_template("home.html",data= data)
if __name__ ==  '__main__':
    app.run(debug= True) # port 5000 por defecto

# python app.py para ejecutar
