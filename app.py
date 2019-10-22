from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__, template_folder='templates')

terreno_list = ['Ladera','Planicie','Cenagoso','Desértico']

@app.route('/lista',methods=['GET'])
def lista():
    predios_list = requests.get('http://127.0.0.1:5000/predio').json()
    return render_template('lista.html',predio=predios_list)

@app.route('/formulario',methods=['GET'])
def formulario():
    return render_template('formulario.html',terreno=terreno_list)

@app.route('/guardarPredio',methods=['POST'])
def guardarPredio():
    predio = dict(request.values)
    predio['area'] = float(predio['area'])
    requests.post('http://localhost:5000/predio', json=predio)
    return(lista())