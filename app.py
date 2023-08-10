from flask import Flask, render_template
from load_data import LICENCIAS,PDFS
app = Flask(__name__)

@app.route('/')
def index():
    # return "<h1>Hola Mundo! </h1>"
    data = {
        'titulo': 'Inicio',
        'logo': 'www.var.com',
        'licencias': LICENCIAS,
        'pdfs': PDFS
    }
    return render_template('index.html',data= data)

if __name__ ==  '__main__':
    app.run(debug= True) # port 5000 por defecto

# python app.py para ejecutar
