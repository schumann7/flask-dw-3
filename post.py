from flask import Flask, request

app = Flask(__name__)

alunos = [
    {"id": 1, "nome": "vito"},
    {"id": 2, "nome": "basza"},
    {"id": 3, "nome": "schumann"},
    {"id": 4, "nome": "leonardo"},
    {"id": 5, "nome": "haroldo"},
]

@app.route("/", methods=["GET"])
def helloWorld():
    return "Hello, World!"

@app.route("/alunos", methods=["GET"])
def get_alunos():
    return alunos

@app.route("/alunosid/<int:id>", methods="GET")
def get_alunos_by_id(id):
    for aluno in alunos:
        if aluno["id"] == id:
            return aluno
    return {}


@app.route("/alunos", methods=["POST"])
def post_route():
    dados = request.get_json()
    alunos.append({"nome": dados["nome"]})
    return {"mensagem": "ok"}

@app.route("/alunos", methods=["DELETE"])
def delete_route():
    return {'metodo': 'delete'}