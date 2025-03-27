from flask import Flask, request
import uuid

app = Flask(__name__)

lista_calculos = []

@app.route("/soma", methods= ["POST"])
def samrnum():
    dados_recebidos = request.get_json()
    numero1 = dados_recebidos ['numero1']
    numero2 = dados_recebidos ['numero2']
    resultado = numero1 + numero2
    lista_calculos.append({
        'id': str(uuid.uuid4()),
        'numero1' : numero1,
        'numero2' : numero2,
        'resultado' : resultado })
    
    return {'resultado': resultado}

@app.route('/calculos', methods= ['GET'])
def calculos():
    return lista_calculos



'''como podemos excluir um calculo da lista?'''
@app.route('/deletar/<id>', methods=['DELETE'])
def deletar_item(id):
    global lista_calculos
    lista_calculos = [d for d in lista_calculos if d.get('id') !=id]

    return{}

@app.route('/editar/<id>', methods=['PUT'])
def editar_item(id):
     global lista_calculos
     dados_recebidos = request.get_json()
     numero1 = dados_recebidos['numero1']
     numero2 = dados_recebidos['numero2']

     lista_temp = []
     for calculo in lista_calculos:
         if calculo['id'] == id:
            resultado = numero1 + numero2
            lista_calculos.append({
                'id': str(uuid.uuid4()),
                'numero1' : numero1,
                'numero2' : numero2,
                'resultado' : resultado })
         else:
             lista_temp.append(calculo)
     lista_calculos = lista_temp
     return{}
