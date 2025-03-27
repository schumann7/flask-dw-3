from flask import Flask, request
from uuid import uuid4 as uuid

app = Flask(__name__)

historico = []

@app.route("/", methods=["GET"])
def helloWorld():
    return {"mensagem": "Hello, world!"}

@app.route("/soma", methods=["POST"])
def somar():
    dados_recebidos = request.get_json()
    num1 = dados_recebidos['num1']
    num2 = dados_recebidos['num2']
    resultado = num1 + num2
    id = str(uuid())
    historico.append({
        'id':id,
        f"{num1} + {num2} = ":resultado 
        })
    return {"resultado": resultado}

@app.route("/historico", methods=["GET"])
def get_historico():
    return historico

@app.route("/deletar/<id>", methods=["DELETE"])
def deletar(id):
    global historico
    historico = [d for d in historico if d.get('id') != id]
    return  "Deletado com sucesso"

@app.route("/editar/<id>", methods=["PUT"])
def editar(id):
    global historico
    dados = request.get_json()
    num1 = dados["num1"]
    num2 = dados["num2"]

    lista_temp = []
    for calculo in historico:
        if calculo['id'] == id:
            resultado = num1 + num2
            lista_temp.append({
                "id":id,
                f"{num1} + {num2} = ":resultado 
            })
        else:
            lista_temp.append(calculo)
    historico = lista_temp
    return {}