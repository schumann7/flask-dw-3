from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def helloWorld():
    return {'mensagem' : 'Hello World',
            'olaMundo' : 'oi'}

@app.route("/", methods=["POST"])
def post_route():
    return {'metodo' : 'post'}

@app.route("/", methods=["DELETE"])
def delete():
    return {'metodo' : 'delete'}

@app.route("/Schumann")
def schumann():
    return {'nome':'Gabriel'}

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/texto")
def text():
    return 'Exemplo texto'