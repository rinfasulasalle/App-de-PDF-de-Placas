import os
from flask import Flask, render_template, send_from_directory
from load_data import LICENCIAS,PDFS,LOGO, NOMBREAPP
app = Flask(__name__)
data = {
        'nombreApp': NOMBREAPP,
        'titulo': 'Default',
        'logo': LOGO,
        'licencias': LICENCIAS,
        'pdfs': PDFS
    }
# Directorio donde se encuentran los archivos PDF
pdf_directorio = os.path.join(app.root_path, 'pdf')
# --------------------------------------
@app.route('/')
def index():
    pdf_files = [pdf for pdf in os.listdir(pdf_directorio) if pdf.endswith('.pdf')]
    return render_template('login.html',data=data, pdf_files=pdf_files)

@app.route('/download/<filename>')
def download_pdf(filename):
    if filename.endswith('.pdf'):
        return send_from_directory(pdf_directorio, filename, as_attachment=True)

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
