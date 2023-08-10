from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hola Mundo! </h1>"

if __name__ ==  '__main__':
    app.run(debug= True) # port 5000 por defecto

# python app.py para ejecutar
