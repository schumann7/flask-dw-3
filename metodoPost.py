from flask import Flask, request

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
    historico.append({f"{num1} + {num2}": resultado})
    return {"resultado": resultado}

@app.route("/somados", methods=["GET"])
def somados():
    dados_recebidos = request.get_json()
    num1 = dados_recebidos['num1']
    num2 = dados_recebidos['num2']
    return {"Número 1 = ": num1, "Número 2 = ": num2}

@app.route("/historico", methods=["GET"])
def get_historico():
    return historico